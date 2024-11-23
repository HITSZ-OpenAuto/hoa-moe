import subprocess
import json
import os
# from dotenv import load_dotenv

# load_dotenv()

def run_gh_command(command, pat=None):
    """
    Run a GitHub CLI command with optional Personal Access Token.
    
    :param command: List of command arguments
    :param pat: Personal Access Token (optional)
    :return: Parsed JSON output
    """
    try:
        # If PAT is provided, set it as an environment variable
        if pat:
            env = os.environ.copy()
            env['GH_TOKEN'] = pat
        else:
            env = None
        
        result = subprocess.run(['gh'] + command, 
                                capture_output=True, 
                                text=True, 
                                check=True,
                                env=env)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running GitHub CLI command: {e}")
        print(f"Error output: {e.stderr}")
        return []

def get_org_issues(org_name, pat=None):
    """
    Retrieve open issues for the specified organization.
    
    :param org_name: GitHub organization name
    :param pat: Personal Access Token (optional)
    :return: List of open issues
    """
    command = [
        'search', 'issues',
        '--json', 'title,url,repository,createdAt,author,labels',
        '--state', 'open',
        '--owner', org_name,
    ]
    return run_gh_command(command, pat)

def get_org_pull_requests(org_name, pat=None):
    """
    Retrieve open pull requests for the specified organization.
    
    :param org_name: GitHub organization name
    :param pat: Personal Access Token (optional)
    :return: List of open pull requests
    """
    command = [
        'search', 'prs',
        '--json', 'title,url,repository,createdAt,author,labels',
        '--state', 'open',
        '--owner', org_name,
    ]
    return run_gh_command(command, pat)

def fetch_opened_prs_and_issues(org_name, pat=None):
    """
    Generate a markdown report of open issues and pull requests.
    
    :param org_name: GitHub organization name
    :param pat: Personal Access Token (optional)
    """
    # Get issues and PRs
    issues = get_org_issues(org_name, pat)
    prs = get_org_pull_requests(org_name, pat)
    
    # Generate markdown report
    with open(f'content/news/daily.md', 'r+') as f:
        content = f.read()
        f.seek(0)
        # Keep content before "## 议题" and overwrite the rest
        if "## 待解决的 Issues" in content:
            f.write(content.split("## 待解决的 Issues")[0])
        else:
            f.write(content)
        f.write("## 待解决的 Issues\n")
        f.truncate()
        if not issues:
            f.write("暂无待解决的 Issues\n\n")
        else:
            for issue in issues:
                if issue['repository']['name'] != 'hoa-moe':
                    f.write(f"### [{issue['title']}]({issue['url']})\n")
                    f.write(f"- **仓库**: {issue['repository']['name']}\n")
                    f.write(f"- **创建于**: {issue['createdAt']}\n")
                    f.write(f"- **作者**: {issue['author']['login']}\n")
                    
                # Labels (if any)
                if issue['labels']:
                    label_list = ', '.join([label['name'] for label in issue['labels']])
                    f.write(f"- **标签**: {label_list}\n")
                
                f.write("\n")
        
        # Pull Requests section
        f.write("## 待合并的 Pull Requests\n")
        if not prs:
            f.write("暂无打开的 Pull Requests\n\n")
        else:
            for pr in prs:
                if pr['repository']['name'] != 'hoa-moe':
                    f.write(f"### [{pr['title']}]({pr['url']})\n")
                    f.write(f"- **仓库**: {pr['repository']['name']}\n")
                    f.write(f"- **创建于**: {pr['createdAt']}\n")
                    f.write(f"- **作者**: {pr['author']['login']}\n")
                    
                # Labels (if any)
                if pr['labels']:
                    label_list = ', '.join([label['name'] for label in pr['labels']])
                    f.write(f"- **标签**: {label_list}\n")
                
                f.write("\n")
    
    print(f"Report updated: content/news/daily.md")

def main():
    org_name = 'HITSZ-OpenAuto'
    pat = os.getenv('TOKEN')
    
    fetch_opened_prs_and_issues(org_name, pat)

if __name__ == '__main__':
    main()