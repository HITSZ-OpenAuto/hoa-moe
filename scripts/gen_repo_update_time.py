import requests
import datetime
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import argparse


# Function to get an HTTP session with retry logic
def get_http_session():
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('https://', adapter)
    return session


# Function to get the latest commit
def get_latest_commit(owner, repo):
    commits_url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    params = {'since': '2000-01-01T00:00:01Z',
              'per_page': 1}
    response = session.get(commits_url, headers=headers, params=params)
    commit_info = dict()
    if response.status_code == 200:
        commit = response.json()
        commit_info['author'] = commit[0]['commit']['author']['name']
        commit_info['date'] = datetime.datetime.strptime(commit[0]['commit']['author']['date'],
                                                         "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(hours=8)  # UTC-8
        commit_info['message'] = commit[0]['commit']['message']
    else:
        print(f'Failed to fetch commits for {repo}: {response.status_code}')
    return commit_info


def save_latest_update(commit_info):
    datetime_object = commit_info['date']
    yymmdd = f'{datetime_object.year}.{datetime_object.month}.{datetime_object.day}'
    result_content = "最近由 " + commit_info['author'] + " 更新于 " + yymmdd + "，更新内容：" + commit_info['message'] + "\n"
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

    # Use the session with retry logic for API requests
    session = get_http_session()

    # Headers for authentication
    headers = {
        'Authorization': f'token {token}'
    }

    # Fetch and parse the latest commit
    latest_commit_info = get_latest_commit(owner, repo)
    if latest_commit_info:
        save_latest_update(latest_commit_info)
