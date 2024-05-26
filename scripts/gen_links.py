import requests
import argparse
import urllib.parse
import os

def create_hugo_shortcode(file_paths, owner, repo):
    result = "{{< filetree/container >}}\n"
    organized_paths = organize_paths(file_paths)

    # Generate shortcode for each directory
    for directory, content in organized_paths.items():
        result += generate_folder_shortcode(directory, content, owner, repo)
    
    result += "{{< /filetree/container >}}\n"
    return result

def organize_paths(file_paths):
    organized_paths = {}
    for path in file_paths:
        components = path.split(os.path.sep)
        current_dict = organized_paths
        for component in components[:-1]:
            current_dict = current_dict.setdefault(component, {})
        current_dict[components[-1]] = None
    return organized_paths

def generate_folder_shortcode(directory, content, owner, repo):
    result = f'  {{{{< filetree/folder name="{os.path.basename(directory)}" state="closed" >}}}}\n'
    for name, value in content.items():
        if value is None:
            # It's a file
            file_path = os.path.join(directory, name)
            encoded_path = urllib.parse.quote(file_path)
            
            prefix = f'https://gh.hoa.moe/github.com/{owner}/{repo}/raw/main'
            
            full_path = f'{prefix}/{encoded_path}'
            result += f'    {{{{< filetree/file name="{name}" url="{full_path}" >}}}}\n'
        else:
            # It's a subfolder
            result += generate_folder_shortcode(os.path.join(directory, name), value, owner, repo)
    result += '  {{< /filetree/folder >}}\n'
    return result

def list_files_in_repo(owner, repo, token, path=''):
    paths = []
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    # response = requests.get(url, auth=(token))
    headers = {
        'Authorization': f'token {token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        contents = response.json()
        for content in contents:
            if content['type'] == 'file':
                paths.append(content['path'])
            elif content['type'] == 'dir':
                paths.extend(list_files_in_repo(owner, repo, token, content['path']))
    else:
        print(f"Failed to retrieve files. Status code: {response.status_code}")
        print(response.text)
    return paths

def save_files_list(owner, repo, token):
    paths = list_files_in_repo(owner, repo, token)
    filtered_paths = [path for path in paths if path.endswith(('.pdf', '.zip', '.rar', '.7z', '.docx', '.doc', '.ipynb', '.pptx', '.apkg', '.mp4', '.csv', 'xlsx'))]
    result_content = ""
    if filtered_paths:
        result_content = create_hugo_shortcode(filtered_paths, owner, repo)
    with open('result.txt', 'w') as file:
        file.write(result_content)     

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate download links of files from a GitHub repository.")
    parser.add_argument("owner", help="GitHub repository owner")
    parser.add_argument("repo", help="GitHub repository name")
    parser.add_argument("token", help="GitHub token")

    args = parser.parse_args()
    owner = args.owner
    repo = args.repo
    token = args.token
    
    save_files_list(owner, repo, token)
