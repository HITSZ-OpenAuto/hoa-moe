import asyncio
import aiohttp
import urllib.parse
import os
import json
from datetime import datetime
from fs import filesize
from typing import List, Dict
import time
from aiohttp import ClientTimeout


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
        self.batch_size = 100  # GitHub API allows up to 100 items per page

    async def task(self):
        """Main task: fetch worktree information online, generate shortcodes, and persist them."""
        async with aiohttp.ClientSession() as session:
            worktree = await self.get_worktree_json(session)
            if not worktree:
                print(f"Worktree for {self.repo} is empty or could not be fetched.")
                return
            print(f"Worktree for {self.repo} generated successfully.")

        shortcode = self.create_hugo_shortcode(worktree)

        file_name = f"{self.repo}_cards.txt"  # File storing the shortcode
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(shortcode)
        print(f"Shortcode saved to {file_name}.")
        print("-" * 50)

    async def fetch_content(self, session: aiohttp.ClientSession, url: str) -> Dict:
        timeout = ClientTimeout(total=30)
        async with session.get(url, headers=self.headers, timeout=timeout) as response:
            if response.status == 200:
                print(f"Fetched {url} successfully.\nNow parsing JSON content.")
                return await response.json(content_type=None)
            else:
                raise Exception(f"Failed to fetch {url}: {response.status}")

    async def get_worktree_json(self, session: aiohttp.ClientSession) -> Dict:
        url = f"https://raw.githubusercontent.com/HITSZ-OpenAuto/{self.repo}/refs/heads/worktree/worktree.json"
        try:
            return await self.fetch_content(session, url)
        except Exception as e:
            print(f"Error fetching worktree.json: {e}")
            return {}

    @staticmethod
    def organize_paths(worktree_info: Dict[str, Dict[str, int | str]]) -> Dict:
        """Pass in worktree information, return a Dict containing structured information of folders and files.\n
        Example of incoming worktree information (i.e., worktree.json, one level deep):\n
        {"materials/考研近代史考点.pdf": {
            "size": 42834145,
            "time": 1701264546,
            "hash": "b31cf9d66b9ec1547b8984df95368ff314612263"
        }}\n
        Example of the returned dictionary (uncertain depth):
        {
            "materials": {
                "materials/考研近代史考点.pdf": [
                "考研近代史考点",
                "pdf",
                "40.8 MB",
                "2023/11/29",
                "icons/pdf.png"],
            }
        }"""

        # Exclude rules: files containing these patterns; files without an extension;
        # files with excluded extensions.
        exclude_patterns = [
            "README.md",
            ".gitkeep",
            ".github/",
            ".hoa/",
            "LICENSE",
            "tag.txt",
            ".tmp",
            ".gitignore",
            ".gitattributes",
        ]
        exclude_extensions = {
            "toml",
        }

        organized_paths = {}
        for original_path, info in worktree_info.items():
            # TODO: more specific filtering
            if any(pattern in original_path for pattern in exclude_patterns):
                continue  # Skip unnecessary files or directories
            # Generate information needed to build the shortcode
            size_bytes = info.get("size")
            timestamp = info.get("time")
            if size_bytes is None or timestamp is None:
                print(f"Skipping {original_path} due to missing size or time.")
                continue
            size = filesize.traditional(size_bytes)
            date = datetime.fromtimestamp(timestamp).strftime("%Y/%m/%d")
            path_components = original_path.split("/")
            full_name = path_components[-1]
            if "." not in full_name:
                continue  # Skip files without an extension
            current_dict = organized_paths

            for component in path_components[:-1]:
                current_dict = current_dict.setdefault(component, {})
            name, suffix = full_name.rsplit(".", 1)
            if suffix.lower() in exclude_extensions:
                continue  # Skip excluded file extensions (e.g. *.toml)

            icon = match_suffix_icon(suffix)

            current_dict[original_path] = [name, suffix, size, date, icon]
        return organized_paths

    def create_hugo_shortcode(self, worktree_info: List[Dict[str, int | str]]) -> str:
        result = f'{{{{< hoa-filetree/container driveURL="https://open.osa.moe/openauto/{self.repo}" repoURL="https://github.com/HITSZ-OpenAuto/{self.repo}" >}}}}\n'
        organized_paths = self.organize_paths(worktree_info)

        if organized_paths:
            result += self.generate_shortcodes_recursive(organized_paths, "")

        result += "{{< /hoa-filetree/container >}}\n"
        return result

    def generate_shortcodes_recursive(
        self, worktree_info: Dict, current_path: str
    ) -> str:
        """Recursively generate Hugo shortcodes for folders and files."""
        result = ""

        for name, value in worktree_info.items():
            if isinstance(value, dict):  # Folder
                new_path = f"{current_path}/{name}" if current_path else name
                result += f'{{{{< hoa-filetree/folder name="{name}" date="" state="closed" >}}}}\n'
                result += self.generate_shortcodes_recursive(
                    value,
                    new_path,  # Recurse
                )
                result += "{{< /hoa-filetree/folder >}}\n"
            elif isinstance(value, list):  # File
                filename, suffix, size, date, icon = value
                encoded_path = urllib.parse.quote(name, safe="/")
                prefix = (
                    f"https://gh.hoa.moe/github.com/{self.owner}/{self.repo}/raw/main"
                )
                full_url = f"{prefix}/{encoded_path}"
                result += f'{{{{< hoa-filetree/file name="{filename}" type="{suffix}" size="{size}" date="{date}" icon="{icon}" url="{full_url}" >}}}}\n'

        return result


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
    """Process multiple course repositories, a collection of main tasks."""
    clients = [GitHubAPIClient(owner, repo, token) for repo in repos]

    await asyncio.gather(*(client.task() for client in clients))


if __name__ == "__main__":
    try:
        owner = os.environ["ORG_NAME"]
        token = os.environ["PERSONAL_ACCESS_TOKEN"]
    except KeyError as e:
        raise ValueError(
            f"Environment variable {e} not found, please set it first."
        ) from e

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
    asyncio.run(process_multiple_repos(owner, repos, token))
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Exec: {execution_time:.2f} s")
