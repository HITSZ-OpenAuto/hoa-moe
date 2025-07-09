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
from scripts.filetrees import FileTreeManager, CourseData, create_course_data

file_tree_manager = FileTreeManager()


class GitHubAPIClient:
    """Client for only one GitHub repository."""

    def __init__(self, owner: str, repo: str, token: str):
        self.owner = owner
        self.repo = repo
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
        }
        self.commit_cache = {}
        self.batch_size = 100  # GitHub API allows up to 100 items per page
        self.has_commit_error = False
    
    async def task(self):
        with aiohttp.ClientSession() as session:
            worktree = await self.get_worktree_json(self, session)
            if not worktree:
                print(f"Worktree for {self.repo} is empty or could not be fetched.")
                return
        return self.create_hugo_shortcode(worktree)

    async def fetch_content(self, session: aiohttp.ClientSession, url: str) -> Dict:
        timeout = ClientTimeout(total=30)
        async with session.get(url, headers=self.headers, timeout=timeout) as response:
            if response.status == 200:
                return await response.json()
            raise Exception(f"Failed to fetch {url}: {response.status}")

    async def get_worktree_json(self, session: aiohttp.ClientSession) -> Dict:
        url = f'https://raw.githubusercontent.com/HITSZ-OpenAuto/{self.repo}/refs/heads/worktree/worktree.json'
        async with aiohttp.ClientSession() as session:
            try:
                return await self.fetch_content(session, url)
            except Exception as e:
                print(f"Error fetching worktree.json: {e}")
                return {}

    @staticmethod
    def organize_paths(worktree_info: Dict[str, Dict[str, int | str]]) -> Dict:
        """传入工作树信息，返回一个字典，包含文件夹和文件的结构化信息。\n
        传入工作树信息示例（即 worktree.json，一层深度）：\n
        {"materials/考研近代史考点.pdf": {
            "size": 42834145,
            "time": 1701264546,
            "hash": "b31cf9d66b9ec1547b8984df95368ff314612263"
        }}\n
        返回的字典示例（其深度不确定）：
        {
            "materials": {
                "考研近代史考点.pdf": [
                "考研近代史考点", 
                "file", 
                "icons/file.png", 
                "40.8 MB", 
                "2023/11/29"],
            }
        }"""
        exclude_patterns = ['README.md', '.gitkeep', '.github/', '.hoa/', 'LICENSE', 'tag.txt'] # TODO：筛选比较粗糙

        organized_paths = {}
        for original_path, info in worktree_info.items():
            if any(pattern in original_path for pattern in exclude_patterns):
                continue # 跳过不需要的文件或目录
            size = filesize.format_size(info["size"])
            date = datetime.fromtimestamp(info["time"]).strftime("%Y/%m/%d")
            path_components = original_path.split("/")
            full_name = path_components[-1]
            current_dict = organized_paths

            for component in path_components[:-1]:
                current_dict = current_dict.setdefault(component, {})

            name, suffix = full_name.rsplit(".", 1)
            icon = match_suffix_icon(suffix)

            current_dict[name] = [name, suffix, size, date, icon]
        return organized_paths

    def create_hugo_shortcode(self, worktree_info: List[Dict[str, str]]) -> str:
        result = f'{{{{< hoa-filetree/container driveURL="https://open.osa.moe/openauto/{self.repo}" repoURL="https://github.com/HITSZ-OpenAuto/{self.repo}" >}}}}\n'
        organized_paths = self.organize_paths(worktree_info)

        if organized_paths:
            result += self._generate_shortcodes_recursive(organized_paths, "")

        result += "{{< /hoa-filetree/container >}}\n"
        return result

    def _generate_shortcodes_recursive(self, worktree_info: Dict, current_path: str) -> str:
        """递归地生成文件夹和文件的 Hugo 短代码"""
        result = ""

        for name, value in worktree_info.items():
            new_path = f"{current_path}/{name}" if current_path else name
            if isinstance(value, dict):  # 文件夹
                result += f'{{{{< hoa-filetree/folder name="{name}" date="" state="closed" >}}}}\n'
                result += self._generate_shortcodes_recursive(
                    value, new_path  # 递归
                )
                result += f'{{{{< /hoa-filetree/folder >}}}}\n'
            elif isinstance(value, list):  # 文件
                filename, suffix, size, date, icon = value
                encoded_path = urllib.parse.quote(new_path, safe="/")
                prefix = f"https://gh.hoa.moe/github.com/{self.owner}/{self.repo}/raw/main"
                full_url = f"{prefix}/{encoded_path}"
                result += f'{{{{< hoa-filetree/file name="{filename}" type="{suffix}" size="{size}" date="{date}" icon="{icon}" url="{full_url}" >}}}}\n'
        return result


def is_human_readable_size(size_str: str) -> bool:
    pattern = r"""(?x)
        ^
        (\d{1,10}|\d{1,10}\.\d{1,2})
        \s*
        (byte|bytes|[KMGTPE]B|B)
        $
    """
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
    image = ["png", "jpg", "jpeg", "gif", "bmp", "psd", "tif", "tiff"]
    doc = ["doc", "docx"]
    icons = ["docx", "pdf", "image", "ppt", "txt", "zip"]

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
    parser = argparse.ArgumentParser(
        description="Generate download links of files from a GitHub repository."
    )
    parser.add_argument(
        "owner", help="GitHub repository owner", default="HITSZ-OpenAuto"
    )
    # parser.add_argument("repo", help="GitHub repository name")
    parser.add_argument("token", help="GitHub token")

    args = parser.parse_args()

    # Get repos array from environment variable
    repos_json = os.environ.get("repos_array")
    repos = None

    if not repos_json:
        repos_json = os.environ.get("repo_name")
        repos = ["".join(str(c) for c in repos_json)]
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
