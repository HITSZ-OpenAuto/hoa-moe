import os
import requests
import datetime
import certifi
import openai
import yaml
from datetime import timezone
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from tqdm import tqdm

TOKEN = os.environ.get('TOKEN')
ORG_NAME = os.environ.get('ORG_NAME')

openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.base_url = "https://aihubmix.com/v1/"
openai.default_headers = {"x-foo": "true"}

# Set the SSL certificates path
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

def chinese_weekday(date):
    weekdays = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    return weekdays[date.weekday()]

# Function to get an HTTP session with retry logic
def get_http_session():
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('https://', adapter)
    return session

# Use the session with retry logic for API requests
session = get_http_session()

# Headers for authentication
headers = {
    'Authorization': f'token {TOKEN}'
}

# Generate a funny summary using GPT-3.5-turbo
def generate_summary(report_text):
    prompt = f"Generate a funny summary for the weekly commit report in Chinese:\n\n{report_text}\n\n---\n\nSummary:"
    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": prompt,
                },
            ],
        )
        return completion.choices[0].message.content
    except:
        return None

# Function to get all public repos in the organization
def get_org_public_repos(url):
    repos = []
    while url:
        response = session.get(url, headers=headers)
        if response.status_code == 200:
            repos.extend([repo for repo in response.json() if not repo['private']])
            # Check if there's a next page of results
            if 'next' in response.links:
                url = response.links['next']['url']
            else:
                url = None
        else:
            print(f'Failed to fetch repositories: {response.status_code}')
            url = None
    return repos

# Function to get commits from the past week
def get_weekly_commits(owner, repo, since):
    commits_url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    params = {'since': since.isoformat()}
    response = session.get(commits_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to fetch commits for {repo}: {response.status_code}')
        return []

# Calculate the date one week ago
one_week_ago = datetime.datetime.now(timezone.utc) - datetime.timedelta(weeks=1)

# Get all public repositories in the organization
repos = get_org_public_repos(f'https://api.github.com/orgs/{ORG_NAME}/repos')

# Store weekly commits
weekly_commits = {}

# YAML front matter for the markdown file
yaml_front_matter = yaml.dump({
    "title": f"AUTO 周报 {one_week_ago.date()} - {datetime.datetime.now().date()}",
    "date": datetime.datetime.now().strftime("%Y-%m-%d"),
    "authors": [
        {
            "name": "ChatGPT",
            "link": "https://github.com/openai",
            "image": "https://github.com/openai.png"
        }
    ],
    "excludeSearch": False,
    "draft": False
}, default_flow_style=False, allow_unicode=True)

# Fetch and filter commits from the past week
for repo in repos:
    commits = get_weekly_commits(ORG_NAME, repo['name'], one_week_ago)
    if commits:
        weekly_commits[repo['name']] = []
        for commit in commits:
            weekly_commits[repo['name']].append({
                'author': commit['commit']['author']['name'],
                'date': commit['commit']['author']['date'],
                'message': commit['commit']['message']
            })

markdown_report = ""
if weekly_commits:
    for repo_name, commits in tqdm(weekly_commits.items()):

        # check if https://github.com/{ORG_NAME}/{repo_name}/blob/main/tag.txt exists, if exists, extract the tag start with "name:" as the repo name
        tag_url = f'https://raw.githubusercontent.com/{ORG_NAME}/{repo_name}/main/tag.txt'
        response = session.get(tag_url)
        if response.status_code == 200:
            tag = response.text.split("name:")[1].strip()
            title = tag
        else:
            title = repo_name

        markdown_report += f'## [{title}](https://github.com/{ORG_NAME}/{repo_name})\n\n'
        prev_author = None
        prev_date = None
        is_first_commit = True
        for commit in commits:
            if commit["author"] != "github-actions":  # Exclude commits authored by github-actions
                datetime_object = datetime.datetime.strptime(commit["date"], "%Y-%m-%dT%H:%M:%SZ")
                chinese_day = chinese_weekday(datetime_object)
                
                if prev_date != datetime_object.date():
                    markdown_report += f'### {chinese_day} \n'
                    prev_date = datetime_object.date()

                if commit["author"] != prev_author:
                    markdown_report += f'**{commit["author"]}**\n\n'
                    prev_author = commit["author"]
                    is_first_commit = True

                if is_first_commit:
                    markdown_report += "**更新内容：**\n"
                    is_first_commit = False
                
                message_lines = commit["message"].split('\n')
                heading = message_lines[0]
                markdown_report += f'- {heading}\n'
                markdown_report += '\n'

    final_markdown_report = f'---\n{yaml_front_matter}---\n\n'

    summary = generate_summary(markdown_report)

    if summary:
        final_markdown_report += f'## 本周概要\n\n{summary}\n\n'

    final_markdown_report += markdown_report

    with open(f'content/news/weekly-{one_week_ago.date()}.md', 'w') as file:
        file.write(final_markdown_report)

else:
    print('No commits found in the past week.')
