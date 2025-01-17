import asyncio
import aiohttp
import argparse
import urllib.parse
import os
import json
import re
from datetime import datetime
from fs import filesize
from functools import lru_cache
from typing import List, Dict, Optional
import time
from aiohttp import ClientTimeout
from tenacity import retry, stop_after_attempt, wait_exponential
from filetrees import FileTreeManager, CourseData, create_course_data

file_tree_manager = FileTreeManager()

class GitHubAPIClient:
    def __init__(self, owner: str, repo: str, token: str):
        self.owner = owner
        self.repo = repo
        self.token = token
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.commit_cache = {}
        self.batch_size = 100  # GitHub API allows up to 100 items per page
        self.has_commit_error = False

    async def fetch_content(self, session: aiohttp.ClientSession, url: str) -> Dict:
        timeout = ClientTimeout(total=30)
        async with session.get(url, headers=self.headers, timeout=timeout) as response:
            if response.status == 200:
                return await response.json()
            raise Exception(f"Failed to fetch {url}: {response.status}")

    async def get_repo_commit_sha(self) -> Optional[str]:
        try:
            commits_url = f'https://api.github.com/repos/{self.owner}/{self.repo}/commits'

            # connector = aiohttp.TCPConnector(ssl=False)
            async with aiohttp.ClientSession() as session:
                async with session.get(
                        commits_url,
                        headers=self.headers,
                        timeout=ClientTimeout(total=30)
                ) as response:
                    if response.status == 200:
                        commits_data = await response.json()
                        if commits_data and len(commits_data) > 0:
                            commit_sha = commits_data[0]['sha']
                            return commit_sha
                        else:
                            self.has_commit_error = True
                            return None
        except Exception as e:
            self.has_commit_error = True
            print(f"{self.repo} REST API query commit sha failed: {e}")
            return None

    async def get_file_date_rest_api(self, session: aiohttp.ClientSession, path: str) -> str:
        """使用 REST API 获取单个文件的最后提交日期"""
        try:
            commits_url = f'https://api.github.com/repos/{self.owner}/{self.repo}/commits'
            params = {
                'path': path,
                'per_page': 1
            }

            # connector = aiohttp.TCPConnector(ssl=False)
            async with aiohttp.ClientSession() as session:
                async with session.get(
                        commits_url,
                        headers=self.headers,
                        params=params,
                        timeout=ClientTimeout(total=30)
                ) as response:
                    if response.status == 200:
                        commits_data = await response.json()
                        if commits_data and len(commits_data) > 0:
                            commit_date = commits_data[0]['commit']['committer']['date']
                            dt = datetime.fromisoformat(commit_date.replace('Z', '+00:00'))
                            return dt.strftime('%Y/%m/%d')
                    self.has_commit_error = True
                    return "Unknown"
        except Exception as e:
            self.has_commit_error = True
            print(f"{self.repo} REST API fallback failed for {path}: {e}")
            return "Unknown"

    async def get_commits_batch(self, session: aiohttp.ClientSession, paths: List[str]) -> Dict[str, str]:
        """批量获取多个文件的提交信息"""
        results = {}

        # 构建批量查询
        queries = []
        for i, path in enumerate(paths):
            queries.append(f"""
            file_{i}: repository(owner: "{self.owner}", name: "{self.repo}") {{
                object(expression: "HEAD") {{
                    ... on Commit {{
                        blame(path: "{path}") {{
                            ranges {{
                                commit {{
                                    committedDate
                                }}
                            }}
                        }}
                    }}
                }}
            }}
            """)

        # 合并所有查询
        query = "query {\n" + "\n".join(queries) + "\n}"

        url = "https://api.github.com/graphql"
        try:
            async with session.post(url, headers=self.headers, json={"query": query}) as response:
                if response.status == 200:
                    data = await response.json()

                    # 处理返回的数据
                    for i, path in enumerate(paths):
                        try:
                            file_data = data.get("data", {}).get(f"file_{i}", {})
                            blame_data = (file_data.get("object", {})
                                          .get("blame", {})
                                          .get("ranges", [{}])[0]
                                          .get("commit", {})
                                          .get("committedDate"))

                            if blame_data:
                                dt = datetime.fromisoformat(blame_data.replace('Z', '+00:00'))
                                results[path] = dt.strftime('%Y/%m/%d')
                            else:
                                # GraphQL 查询失败，尝试 REST API
                                print(f"GraphQL query returned no data for {path}, trying REST API...")
                                results[path] = await self.get_file_date_rest_api(session, path)
                        except (KeyError, IndexError) as e:
                            print(f"Error processing path {path} with GraphQL, trying REST API: {e}")
                            results[path] = await self.get_file_date_rest_api(session, path)
                else:
                    print(f"GraphQL query failed with status: {response.status}, falling back to REST API")
                    # GraphQL 整体失败，对所有文件使用 REST API
                    for path in paths:
                        results[path] = await self.get_file_date_rest_api(session, path)
        except Exception as e:
            print(f"Failed to execute GraphQL query: {e}, falling back to REST API")
            # 发生异常，对所有文件使用 REST API
            for path in paths:
                results[path] = await self.get_file_date_rest_api(session, path)

        return results

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def list_files_in_repo(self, session: aiohttp.ClientSession, path='') -> List[Dict]:

        # # Create a TCPConnector with verify_ssl=False
        # connector = aiohttp.TCPConnector(ssl=False)
        #
        # # Create a new session with the connector if one isn't provided
        # # if not session:
        # session = aiohttp.ClientSession(connector=connector)

        paths = []
        url = f'https://api.github.com/repos/{self.owner}/{self.repo}/contents/{path}'

        try:
            contents = await self.fetch_content(session, url)
            directories = []
            files_to_process = []

            for content in contents:
                if content['type'] == 'file':
                    if (any(content['path'].endswith(ext) for ext in ('.pdf', '.zip', '.rar', '.7z', '.docx', '.doc',
                                                                      '.ipynb', '.pptx', '.apkg', '.mp4', '.csv',
                                                                      '.xlsx', 'txt',
                                                                      'png', 'jpg', 'jpeg', 'gif', 'webp',
                                                                      '.md')) and
                            not (content['path'].endswith('README.md') or content['path'].endswith('tag.txt') or
                                 content['path'].endswith('LICENSE'))):
                        files_to_process.append({
                            'path': content['path'],
                            'size': filesize.traditional(int(content['size']))
                        })
                elif content['type'] == 'dir' and not (content['path'].endswith(".github")):
                    directories.append(content['path'])

            # 批量获取文件的最后修改日期
            if files_to_process:
                file_dates = await self.get_commits_batch(session, [f['path'] for f in files_to_process])
                for file in files_to_process:
                    file['date'] = file_dates.get(file['path'], 'Unknown')
                paths.extend(files_to_process)

            # 处理目录
            if directories:
                tasks = [self.list_files_in_repo(session, directory) for directory in directories]
                results = await asyncio.gather(*tasks)
                for result in results:
                    paths.extend(result)

        except Exception as e:
            self.has_commit_error = True
            print(f"{self.repo} Error processing {url}: {str(e)}")

        return paths

    async def judge_filetree_cache(self):
        try:
            commit_sha = await self.get_repo_commit_sha()

            if file_tree_data := file_tree_manager.search(self.repo):
                if commit_sha == file_tree_data['last_commit_sha']:
                    pass
                else:
                    result_content = await self.save_files_list()
                    file_tree_manager.update(self.repo, create_course_data(result_content, commit_sha, self.has_commit_error))
            else:
                result_content = await self.save_files_list()
                file_tree_manager.add(self.repo, create_course_data(result_content, commit_sha, self.has_commit_error))
        except Exception as e:
            print(f"File tree cache error: {str(e)}")

    async def save_files_list(self) -> str:
        async with aiohttp.ClientSession() as session:
            start_time = time.time()
            paths = await self.list_files_in_repo(session)
            end_time = time.time()

            print(f"{self.repo} Retrieved {len(paths)} files in {end_time - start_time:.2f} seconds")

            result_content = await self.create_hugo_shortcode(paths)
            return result_content
            # with open(f'{self.repo}_cards.txt', 'w', encoding="utf-8") as file:
            #     file.write(result_content)

    async def create_hugo_shortcode(self, file_paths: List[Dict[str, str]]) -> str:
        result = f'{{{{< hoa-filetree/container driveURL="https://open.osa.moe/openauto/{self.repo}" repoURL="https://github.com/HITSZ-OpenAuto/{self.repo}" >}}}}\n'
        organized_paths = self.organize_paths(file_paths)

        if organized_paths:
            for directory, content in organized_paths.items():
                if isinstance(content, list) and is_human_readable_size(content[0]):
                    prefix = f'https://gh.hoa.moe/github.com/{self.owner}/{self.repo}/raw/main'
                    full_path = f'{prefix}/{directory}'

                    name, suffix = directory.rsplit('.', 1)
                    icon = match_suffix_icon(suffix)
                    result += f'  {{{{< hoa-filetree/file name="{name}" type="{suffix}" size="{content[0]}" date="{content[1]}" icon="{icon}" url="{full_path}" >}}}}\n'
                else:
                    folder_content = await self.generate_folder_content(directory, content)
                    result += folder_content

        result += "{{< /hoa-filetree/container >}}\n"
        return result

    @staticmethod
    def organize_paths(file_paths: List[Dict[str, str]]) -> Dict:
        organized_paths = {}
        for path_dict in file_paths:
            current_dict = organized_paths
            path = path_dict['path']
            for component in path.split('/')[:-1]:
                current_dict = current_dict.setdefault(component, {})
            current_dict[path.split('/')[-1]] = [path_dict['size'], path_dict['date']]
        return organized_paths

    async def generate_folder_content(self, directory: str, content: Dict) -> str:
        result = f'  {{{{< hoa-filetree/folder name="{os.path.basename(directory)}" date="" state="closed" >}}}}\n'

        for name, value in content.items():
            if isinstance(value, list) and is_human_readable_size(value[0]):
                file_path = f'{directory}/{name}'
                encoded_path = urllib.parse.quote(file_path, safe='/')
                prefix = f'https://gh.hoa.moe/github.com/{self.owner}/{self.repo}/raw/main'
                full_path = f'{prefix}/{encoded_path}'
                name, suffix = name.rsplit('.', 1)
                icon = match_suffix_icon(suffix)
                result += f'    {{{{< hoa-filetree/file name="{name}" type="{suffix}" size="{value[0]}" date="{value[1]}" icon="{icon}" url="{full_path}" >}}}}\n'
            elif isinstance(value, dict):
                result += await self.generate_folder_content(f'{directory}/{name}', value)
        result += '  {{< /hoa-filetree/folder >}}\n'
        return result


def is_human_readable_size(size_str: str) -> bool:
    pattern = r'''(?x)
        ^
        (\d{1,10}|\d{1,10}\.\d{1,2})
        \s*
        (byte|bytes|[KMGTPE]B|B)
        $
    '''
    if not size_str:
        return False

    match = re.match(pattern, size_str, re.IGNORECASE)
    if not match:
        return False

    try:
        value = float(match.group(1))
        return value >= 0
    except ValueError:
        return False


def match_suffix_icon(suffix: str) -> str:
    image = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'psd', 'tif', 'tiff']
    doc = ['doc', 'docx']
    icons = ['docx', 'pdf', 'image', 'ppt', 'txt', 'zip']

    if suffix in image:
        suffix = "image"
    if suffix in doc:
        suffix = "docx"
    if suffix not in icons:
        suffix = "file"

    return f"icons/{suffix}.png"


async def process_multiple_repos(owner: str, repos: List[str], token: str) -> None:
    # Create clients for all repos
    clients = [GitHubAPIClient(owner, repo, token) for repo in repos]

    # Run all clients concurrently
    await asyncio.gather(*(client.judge_filetree_cache() for client in clients))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate download links of files from a GitHub repository.")
    parser.add_argument("owner", help="GitHub repository owner", default="HITSZ-OpenAuto")
    # parser.add_argument("repo", help="GitHub repository name")
    parser.add_argument("token", help="GitHub token")
    
    args = parser.parse_args()

    # Get repos array from environment variable
    repos_json = os.environ.get('repos_array')
    repos = None
    
    if not repos_json:
        repos_json = os.environ.get('repo_name')
        repos = repos_json
    else:
        repos = json.loads(repos_json)
    
    if not repos_json:
        raise ValueError("Environment variable repo not found")
    

    # Run the async process for all repos
    start_time = time.perf_counter()
    asyncio.run(process_multiple_repos(args.owner, repos, args.token))

    end_time = time.perf_counter()
    file_tree_manager.save()
    file_tree_manager.export_card_files()
    execution_time = end_time - start_time
    print(f"Exec: {execution_time:.2f} s")
