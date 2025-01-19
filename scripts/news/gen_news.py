import os
import requests
import datetime
import certifi
import openai
from pytz import timezone
import yaml
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from tqdm import tqdm
from gen_image import generate_image
import shutil

# Load environment variables
TOKEN = os.environ.get("TOKEN")
ORG_NAME = os.environ.get("ORG_NAME")
NEWS_TYPE = os.environ.get("NEWS_TYPE")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

for key in [TOKEN, ORG_NAME, NEWS_TYPE]:
    if not key:
        raise ValueError("Please set the environment variables: TOKEN, ORG_NAME, NEWS_TYPE")

if NEWS_TYPE == "weekly" and not OPENAI_API_KEY:  # OpenAI API key is not necessary for daily report
    raise ValueError("Please set the environment variable: OPENAI_API_KEY")

# Set SSL certificates path
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

# Chinese weekday names
WEEKDAYS = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']

def chinese_weekday(date):
    return WEEKDAYS[date.weekday()]

def get_http_session():
    """Create an HTTP session with retry logic."""
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    return session

session = get_http_session()
headers = {'Authorization': f'token {TOKEN}'}

def generate_summary(report_text):
    """Generate a summary using OpenAI's API."""
    print("Generating AI summary...")
    openai.api_key = OPENAI_API_KEY
    openai.base_url = "https://aihubmix.com/v1/"
    prompt = f"Generate a summary for the weekly commit report in Chinese:\n\n{report_text}\n\n---\n\nSummary:"
    try:
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": prompt}],
        )
        return completion.choices[0].message.content
    except Exception:
        return None

def get_org_public_repos(url):
    """Fetch all public repositories in the organization."""
    repos = []
    while url:
        response = session.get(url, headers=headers)
        if response.status_code == 200:
            repos.extend(repo for repo in response.json() if not repo['private'])
            url = response.links.get('next', {}).get('url')
        else:
            print(f'Failed to fetch repositories: {response.status_code}')
            break
    return repos

def get_filtered_commits(owner, repo, since):
    """Get commits from a given repository since a specific date."""
    commits_url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    params = {'since': since.isoformat()}
    response = session.get(commits_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to fetch commits for {repo}: {response.status_code}')
        return []

def calculate_start_time(news_type):
    """Calculate the start time based on the news type."""
    delta = datetime.timedelta(weeks=1) if news_type == "weekly" else datetime.timedelta(days=1)
    start_time = datetime.datetime.now(datetime.UTC) - delta
    return start_time.replace(hour=0, minute=0, second=0, microsecond=0), start_time

def generate_yaml_front_matter(news_type, display_start_time):
    """Generate YAML front matter for the markdown file."""
    if news_type == "weekly":
        return yaml.dump({
            "title": f"AUTO 周报 {display_start_time.date()} - {datetime.datetime.now(timezone('Etc/GMT-8')).date()}",
            "date": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d"),
            "authors": [{"name": "ChatGPT", "link": "https://github.com/openai", "image": "https://github.com/openai.png"}],
            "excludeSearch": False,
            "draft": False
        }, allow_unicode=True)
    elif news_type == "daily":
        return yaml.dump({
            "title": "AUTO 更新速递",
            "date": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d"),
            "authors": [{"name": "github-actions[bot]", "link": "https://github.com/features/actions", "image": "https://avatars.githubusercontent.com/in/15368"}],
            "description": f"北京时间 {display_start_time.date()} {display_start_time.hour:02}时至今",
            "excludeSearch": False,
            "draft": False
        }, allow_unicode=True)

def fetch_commits_from_repos(repos, start_time):
    """Fetch and filter commits from repositories."""
    filtered_commits = []
    org_course_name = {}

    for repo in tqdm(repos):
        commits = get_filtered_commits(ORG_NAME, repo['name'], start_time)
        contain_manual = any(commit['commit']['author']['name'] != "github-actions" for commit in commits)

        if commits and repo['name'] != "hoa-moe" and repo['name'] != ".github":
            for commit in commits:
                filtered_commits.append({
                    'author': commit['commit']['author']['name'],
                    'date': datetime.datetime.strptime(commit['commit']['author']['date'], "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(hours=8),
                    'message': commit['commit']['message'],
                    'repo_name': repo['name']
                })
        # else:
        #     print(f"\nNo commits found in {repo['name']}")

        if contain_manual:
            tag_url = f'https://raw.githubusercontent.com/{ORG_NAME}/{repo["name"]}/main/tag.txt'
            response = session.get(tag_url)
            if response.status_code == 200:
                org_course_name[repo['name']] = response.text.split("name:")[1].strip()

    return filtered_commits, org_course_name

def create_markdown_report(filtered_commits, org_course_name, news_type):
    """Create the markdown report from filtered commits."""
    filtered_commits.sort(key=lambda a: a['date'], reverse=True)
    markdown_report = ""
    markdown_report += f'## 更新内容\n\n'
    prev_date = None

    for commit in filtered_commits:
        if commit["author"] == "github-actions" or commit["author"] == "actions-user":
            continue

        date = commit['date']
        title = org_course_name.get(commit['repo_name'], commit['repo_name'])
        if prev_date != date.date():
            markdown_report += f'### {chinese_weekday(date)} ({date.month}.{date.day})\n\n'
            prev_date = date.date()

        markdown_report += f'- {commit["author"]} 在 [{title}](https://github.com/{ORG_NAME}/{commit["repo_name"]}) 中提交了信息： {commit["message"].splitlines()[0]}\n\n'

    return markdown_report

def save_report(report, news_type, display_start_time):
    """Save the generated report to a file."""
    # filename = f'content/news/{"weekly-" if news_type == "weekly" else ""}{display_start_time.date()}.md'
    if news_type == "daily":
        filename = f'content/news/daily.md'
    else:
        filename = f'content/news/weekly/weekly-{display_start_time.date()}/index.md'
        
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(report)

def main():
    start_time, display_start_time = calculate_start_time(NEWS_TYPE)
    repos = get_org_public_repos(f'https://api.github.com/orgs/{ORG_NAME}/repos')
    yaml_front_matter = generate_yaml_front_matter(NEWS_TYPE, display_start_time)
    filtered_commits, org_course_name = fetch_commits_from_repos(repos, start_time)
    
    if not os.path.exists(f'content/news/weekly/weekly-{display_start_time.date()}'):
        os.makedirs(f'content/news/weekly/weekly-{display_start_time.date()}')
    
    if filtered_commits:
        markdown_report = create_markdown_report(filtered_commits, org_course_name, NEWS_TYPE)
        final_report = f'---\n{yaml_front_matter}---\n\n'
        if NEWS_TYPE == "weekly":
            generate_image(OPENAI_API_KEY)
            shutil.move("generated_image.png", f'content/news/weekly/weekly-{display_start_time.date()}/generated_image.png')
            shutil.move("generated_image_cropped.png", f'content/news/weekly/weekly-{display_start_time.date()}/generated_image_cropped.png')
            final_report += f'![AI Image of the Week](generated_image_cropped.png)\n\n'
            # summary = generate_summary(markdown_report)
            # if summary:
            #     final_report += f'## ✨AI 摘要\n\n{summary}\n\n'
            # else:
            final_report += f'{markdown_report}'

            # update content/news/weekly/_index.zh-cn.md description
            with open('content/news/weekly/_index.zh-cn.md', 'w', encoding="utf-8") as file:
                yaml_front_matter = yaml.dump({
                    "title": "AUTO 周报",
                    "date": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d"),
                    "description": f"AUTO 周报是由 ChatGPT 每周五发布的一份简报，最近更新于 {datetime.datetime.now(timezone('Etc/GMT-8')).date()}。"
                }, allow_unicode=True)
                file.write(f'---\n{yaml_front_matter}---\n')

        else: 
            final_report += f'{markdown_report}'
        
        save_report(final_report, NEWS_TYPE, display_start_time)
        
    else:
        print('No commits found in the given period of time')

if __name__ == "__main__":
    main()
