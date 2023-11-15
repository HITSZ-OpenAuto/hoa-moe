import requests
import argparse

def list_files_in_repo(owner, repo, path=''):
    paths = []
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    response = requests.get(url)
    if response.status_code == 200:
        contents = response.json()
        for content in contents:
            if content['type'] == 'file':
                print(content['path'])
                paths.append(content['path'])
            elif content['type'] == 'dir':
                paths.extend(list_files_in_repo(owner, repo, content['path']))
        print(f"Successfully retrieved {len(paths)} files.")
    else:
        print(f"Failed to retrieve files. Status code: {response.status_code}")
        print(response.text)

    return paths

def save_files_list(owner, repo):
     paths = list_files_in_repo(owner, repo)
     prefix = f'https://github.com/HITSZ-OpenAuto/{repo}/raw/main/'
     filtered_paths = [path for path in paths if path.endswith(('.pdf', '.zip'))]
     with open('result.txt', 'w') as file:
        for path in filtered_paths:
            full_path = prefix + path
            file.write(full_path + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate download links of files from a GitHub repository.")
    parser.add_argument("owner", help="GitHub repository owner")
    parser.add_argument("repo", help="GitHub repository name")

    args = parser.parse_args()
    owner = args.owner
    repo = args.repo
    
    save_files_list(owner, repo)