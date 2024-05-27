import requests
import os

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ORG_NAME = 'HITSZ-OpenAuto'

def get_repos(org_name, access_token):
    url = f'https://api.github.com/orgs/{org_name}/repos'
    headers = {'Authorization': f'token {access_token}'}
    repos = []
    
    while url:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        repos.extend(repo['name'] for repo in data if repo['name'] != '.github' and repo['name'] != 'hoa.moe' and not repo['private'])   
        url = response.links.get('next', {}).get('url')
    
    return repos

def generate_contributors_url(file_path):
    base_url = "https://contrib.nn.ci/api?repo="
    with open(file_path, 'r') as file:
        repos = file.read().splitlines()
    repos_param = '&repo='.join(repos)
    return base_url + repos_param

def update_readme(readme_path, new_url):
    with open(readme_path, 'r') as file:
        lines = file.readlines()

    with open(readme_path, 'w') as file:
        for line in lines:
            if line.strip().startswith("![Contributors]"):
                file.write(f"![Contributors]({new_url})\n")
            else:
                file.write(line)

if __name__ == "__main__":

    repos = get_repos(ORG_NAME, ACCESS_TOKEN)
    with open('repos_list.txt', 'w') as f:
        for repo in repos:
            f.write(f'HITSZ-OpenAuto/{repo}\n')

        f.write('noname7321/HITSZ-OpenAuto\n')

    repo_file_path = 'repos_list.txt'
    readme_file_path = 'content/about/index.zh-cn.md'
    new_contributors_url = generate_contributors_url(repo_file_path)
    update_readme(readme_file_path, new_contributors_url)
