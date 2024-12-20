import asyncio
import aiohttp
import argparse
import urllib.parse
import os
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
    headers = {'Authorization': f'token {token}'}
    
    try:
        contents = await fetch_content(session, url, headers)
        tasks = []
        
        for content in contents:
            if content['type'] == 'file':
                cached_path = cache_path(content['path'])
                if any(cached_path.endswith(ext) for ext in ('.pdf', '.zip', '.rar', '.7z', '.docx', '.doc', 
                                                           '.ipynb', '.pptx', '.apkg', '.mp4', '.csv', '.xlsx', '.md')):
                    paths.append(cached_path)
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
            result_content = create_hugo_shortcode(paths, owner, repo)
            with open('result.txt', 'w', encoding="utf-8") as file:
                file.write(result_content)

def create_hugo_shortcode(file_paths: List[str], owner: str, repo: str) -> str:
    result = "{{< filetree/container >}}\n"
    organized_paths = organize_paths(file_paths)

    for directory, content in organized_paths.items():
        if content is None:
            prefix = f'https://gh.hoa.moe/github.com/{owner}/{repo}/raw/main'
            full_path = f'{prefix}/{directory}'
            result += f'  {{{{< filetree/file name="{directory}" url="{full_path}" >}}}}\n'
        else:
            result += generate_folder_shortcode(directory, content, owner, repo)
    
    result += "{{< /filetree/container >}}\n"
    return result

def organize_paths(file_paths: List[str]) -> Dict:
    organized_paths = {}
    for path in file_paths:
        current_dict = organized_paths
        for component in path.split('/')[:-1]:
            current_dict = current_dict.setdefault(component, {})
        current_dict[path.split('/')[-1]] = None
    return organized_paths

def generate_folder_shortcode(directory: str, content: Dict, owner: str, repo: str) -> str:
    result = f'  {{{{< filetree/folder name="{os.path.basename(directory)}" state="closed" >}}}}\n'
    for name, value in content.items():
        if value is None:
            file_path = f'{directory}/{name}'
            encoded_path = urllib.parse.quote(file_path, safe='/')
            prefix = f'https://gh.hoa.moe/github.com/{owner}/{repo}/raw/main'
            full_path = f'{prefix}/{encoded_path}'
            result += f'    {{{{< filetree/file name="{name}" url="{full_path}" >}}}}\n'
        else:
            result += generate_folder_shortcode(f'{directory}/{name}', value, owner, repo)
    result += '  {{< /filetree/folder >}}\n'
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate download links of files from a GitHub repository.")
    parser.add_argument("owner", help="GitHub repository owner", default="HITSZ-OpenAuto")
    parser.add_argument("repo", help="GitHub repository name")
    parser.add_argument("token", help="GitHub token")

    args = parser.parse_args()
    
    asyncio.run(save_files_list_async(args.owner, args.repo, args.token))
