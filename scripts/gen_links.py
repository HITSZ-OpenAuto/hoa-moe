import asyncio
import aiohttp
import argparse
import urllib.parse
import os
import re
from datetime import datetime
from fs import filesize
from functools import lru_cache
from typing import List, Dict
import time
from aiohttp import ClientTimeout
from tenacity import retry, stop_after_attempt, wait_exponential

# Cache for API responses
@lru_cache(maxsize=1000)
def cache_path(path: str) -> str:
    return path

async def fetch_content(session: aiohttp.ClientSession, url: str, headers: Dict) -> Dict:
    timeout = ClientTimeout(total=30)
    async with session.get(url, headers=headers, timeout=timeout) as response:
        if response.status == 200:
            return await response.json()
        raise Exception(f"Failed to fetch {url}: {response.status}")

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
async def list_files_in_repo_async(session: aiohttp.ClientSession, owner: str, repo: str, token: str, path='') -> List[str]:
    paths = []
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    headers = {
        'Authorization': f'token {token}',
    }

    try:
        contents = await fetch_content(session, url, headers)
        tasks = []

        for content in contents:
            if content['type'] == 'file':
                cached_path = cache_path(content['path'])
                last_modified_date = await get_file_last_modified_date(owner, repo, content['path'], token)
                if any(cached_path.endswith(ext) for ext in ('.pdf', '.zip', '.rar', '.7z', '.docx', '.doc',
                                                             '.ipynb', '.pptx', '.apkg', '.mp4', '.csv', '.xlsx',
                                                             '.md')):
                    paths.append({
                        'path': cached_path,
                        'size': filesize.traditional(int(content['size'])),
                        'date': last_modified_date
                    })
                    # print(f"{filesize.traditional(int(content['size']))}", content)
            elif content['type'] == 'dir':
                task = list_files_in_repo_async(session, owner, repo, token, content['path'])
                tasks.append(task)

        if tasks:
            results = await asyncio.gather(*tasks)
            for result in results:
                paths.extend(result)

    except Exception as e:
        print(f"Error processing {url}: {str(e)}")

    return paths

async def save_files_list_async(owner: str, repo: str, token: str):
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        paths = await list_files_in_repo_async(session, owner, repo, token)
        end_time = time.time()

        print(f"Retrieved {len(paths)} files in {end_time - start_time:.2f} seconds")

        if paths:
            result_content = await create_hugo_shortcode(paths, owner, repo, token)
            with open('result.txt', 'w', encoding="utf-8") as file:
                file.write(result_content)

async def create_hugo_shortcode(file_paths: List[Dict[str, str]], owner: str, repo: str, token: str) -> str:
    result = f'{{{{< hoa-filetree/container driveURL="https://open.osa.moe/openauto/{repo}" >}}}}\n'
    organized_paths = organize_paths(file_paths)

    for directory, content in organized_paths.items():
        if isinstance(content, list) and is_human_readable_size(content[0]):
            prefix = f'https://gh.hoa.moe/github.com/{owner}/{repo}/raw/main'
            full_path = f'{prefix}/{directory}'

            name, suffix = directory.rsplit('.', 1)
            icon = match_suffix_icon(suffix)
            result += f'  {{{{< hoa-filetree/file name="{name}" type="{suffix}" size="{content[0]}" date="{content[1]}" icon="{icon}" url="{full_path}" >}}}}\n'
        else:
            # 使用 await 等待异步函数完成
            folder_content = await generate_folder_shortcode(directory, content, owner, repo, token)
            result += folder_content

    result += "{{< /hoa-filetree/container >}}\n"
    return result

def organize_paths(file_paths: List[Dict[str, str]]) -> Dict:
    organized_paths = {}
    # pathDict: { path, size }
    for pathDict in file_paths:
        current_dict = organized_paths
        path = pathDict['path']
        for component in path.split('/')[:-1]:
            current_dict = current_dict.setdefault(component, {})
        current_dict[path.split('/')[-1]] = [pathDict['size'], pathDict['date']]
    return organized_paths

async def generate_folder_shortcode(directory: str, content: Dict, owner: str, repo: str, token: str) -> str:
    print("directory: ", directory)
    result = f'  {{{{< hoa-filetree/folder name="{os.path.basename(directory)}" date="{await get_file_last_modified_date(owner, repo, directory, token)}" state="closed" >}}}}\n'
    # print("content: ", content)
    for name, value in content.items():
        if isinstance(value, list) and is_human_readable_size(value[0]):
            file_path = f'{directory}/{name}'
            encoded_path = urllib.parse.quote(file_path, safe='/')
            prefix = f'https://gh.hoa.moe/github.com/{owner}/{repo}/raw/main'
            full_path = f'{prefix}/{encoded_path}'
            name, suffix = name.rsplit('.', 1)
            icon = match_suffix_icon(suffix)
            result += f'    {{{{< hoa-filetree/file name="{name}" type="{suffix}" size="{value[0]}" date="{value[1]}" icon="{icon}" url="{full_path}" >}}}}\n'
        elif isinstance(value, dict):
            result += await generate_folder_shortcode(f'{directory}/{name}', value, owner, repo, token)
    result += '  {{< /hoa-filetree/folder >}}\n'
    return result

def is_human_readable_size(size_str: str) -> bool:
    pattern = r'''(?x)                   # 开启详细模式，允许注释
        ^                                # 字符串开始
        (\d{1,10}                       # 1-10位整数
        |\d{1,10}\.\d{1,2})            # 或者带1-2位小数的数字
        \s*                             # 可选的空白字符
        (byte|bytes|[KMGTPE]B|B)        # 单位
        $                               # 字符串结束
    '''

    if not size_str:
        return False

    match = re.match(pattern, size_str, re.IGNORECASE)
    if not match:
        return False

    # 提取数值部分
    try:
        value = float(match.group(1))
        # 确保数值为正数
        if value < 0:
            return False
        return True
    except ValueError:
        return False

async def get_file_last_modified_date(owner, repo, path, token):
    """
    获取 GitHub 仓库中指定文件的最后修改日期

    参数:
        owner (str): 仓库所有者
        repo (str): 仓库名称
        path (str): 文件路径
        token (str): GitHub Personal Access Token

    返回:
        str: 最后修改日期（ISO 8601格式）
        None: 如果发生错误
    """

    # 设置请求头
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    try:
        # 构建提交查询 URL
        commits_url = f'https://api.github.com/repos/{owner}/{repo}/commits'
        params = {
            'path': path,
            'per_page': 1  # 只获取最新的提交
        }
        connector = aiohttp.TCPConnector(ssl=False)
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(
                    commits_url,
                    headers=headers,
                    params=params,
                    timeout=ClientTimeout(total=30)
            ) as response:
                if response.status == 200:
                    commits_data = await response.json()
                    last_commit = commits_data[0]  # 返回最新的提交
                else:
                    raise Exception(f"GitHub API request failed with status: {response.status}")

        commit_date = last_commit['commit']['committer']['date']

        # 可选：将 ISO 8601 格式转换为更友好的格式
        dt = datetime.fromisoformat(commit_date.replace('Z', '+00:00'))
        formatted_date = dt.strftime('%Y/%m/%d')

        return formatted_date

    except (KeyError, IndexError) as e:
        print(f"解析响应时发生错误: {e}")
        return None
    

def match_suffix_icon(suffix: str) -> str:
    # 匹配前端 icon 名称
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate download links of files from a GitHub repository.")
    parser.add_argument("owner", help="GitHub repository owner", default="HITSZ-OpenAuto")
    parser.add_argument("repo", help="GitHub repository name")
    parser.add_argument("token", help="GitHub token")

    args = parser.parse_args()
    
    asyncio.run(save_files_list_async(args.owner, args.repo, args.token))
