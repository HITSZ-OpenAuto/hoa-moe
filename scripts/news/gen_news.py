import logging
import os
import re
import requests
import datetime
import certifi
from pytz import timezone
import yaml
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# Chinese weekday names
WEEKDAYS = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]


def chinese_weekday(date):
    return WEEKDAYS[date.weekday()]


def get_http_session():
    """Create an HTTP session with retry logic."""
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session


DEFAULT_REPOS_LIST_URL = "https://raw.githubusercontent.com/HITSZ-OpenAuto/repos-management/main/repos_list.txt"


def get_repos_from_repos_list(session, headers, repos_list_url=DEFAULT_REPOS_LIST_URL):
    """Fetch repository names from repos-management repos_list.txt.

    Returns a list of dicts with at least {"name": <repo>} to stay compatible with
    downstream code.
    """
    response = session.get(repos_list_url, headers=headers)
    if response.status_code != 200:
        raise RuntimeError(
            f"Failed to fetch repos list from {repos_list_url}: {response.status_code}"
        )

    repo_names = []
    for raw in response.text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        # allow either `repo` or `org/repo`
        repo_names.append(line.split("/", 1)[-1])

    # Deduplicate while preserving order
    seen = set()
    repos = []
    for name in repo_names:
        if name in seen:
            continue
        seen.add(name)
        repos.append({"name": name})

    return repos


def get_filtered_commits(session, headers, owner, repo, since):
    """Get commits from a given repository since a specific date."""
    commits_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {"since": since.isoformat()}
    response = session.get(commits_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch commits for {repo}: {response.status_code}")
        return []


def calculate_start_time(news_type):
    """Calculate the start time based on the news type."""
    delta = (
        datetime.timedelta(weeks=1)
        if news_type == "weekly"
        else datetime.timedelta(days=1)
    )
    start_time = datetime.datetime.now(datetime.UTC) - delta
    return start_time.replace(hour=0, minute=0, second=0, microsecond=0), start_time


def generate_yaml_front_matter(news_type, display_start_time):
    """Generate YAML front matter for the markdown file."""
    if news_type == "weekly":
        return yaml.dump(
            {
                "title": f"AUTO 周报 {display_start_time.date()} - {datetime.datetime.now(timezone('Etc/GMT-8')).date()}",
                "date": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d"),
                "authors": [
                    {
                        "name": "ChatGPT",
                        "link": "https://github.com/openai",
                        "image": "https://github.com/openai.png",
                    }
                ],
                "excludeSearch": False,
                "draft": False,
            },
            allow_unicode=True,
        )
    elif news_type == "daily":
        return yaml.dump(
            {
                "title": "AUTO 更新速递",
                "date": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d"),
                "authors": [
                    {
                        "name": "github-actions[bot]",
                        "link": "https://github.com/features/actions",
                        "image": "https://avatars.githubusercontent.com/in/15368",
                    }
                ],
                "description": "每日更新",
                "excludeSearch": False,
                "draft": False,
            },
            allow_unicode=True,
        )


def fetch_commits_from_repos(session, headers, org_name, repos, start_time):
    """Fetch and filter commits from repositories."""
    filtered_commits = []
    org_course_name = {}

    for repo in repos:
        commits = get_filtered_commits(
            session, headers, org_name, repo["name"], start_time
        )
        contain_manual = any(
            commit["commit"]["author"]["name"] not in {"github-actions", "actions-user"}
            for commit in commits
        )

        if commits:
            for commit in commits:
                filtered_commits.append(
                    {
                        "author": commit["commit"]["author"]["name"],
                        "date": datetime.datetime.strptime(
                            commit["commit"]["author"]["date"], "%Y-%m-%dT%H:%M:%SZ"
                        )
                        + datetime.timedelta(hours=8),
                        "message": commit["commit"]["message"],
                        "repo_name": repo["name"],
                    }
                )
        # else:
        #     print(f"\nNo commits found in {repo['name']}")

        if contain_manual:
            tag_url = f"https://raw.githubusercontent.com/{org_name}/{repo['name']}/main/tag.txt"
            response = session.get(tag_url)
            if response.status_code == 200:
                org_course_name[repo["name"]] = response.text.split("name:")[1].strip()

    return filtered_commits, org_course_name


def create_markdown_report(filtered_commits, org_course_name, news_type, org_name):
    """Create the markdown report from filtered commits."""
    filtered_commits.sort(key=lambda a: a["date"], reverse=True)
    markdown_report = ""
    markdown_report += "## 更新内容\n\n"
    prev_date = None

    ci_re = re.compile(r"(?i)\bci\s*[:：]")
    merge_pr_re = re.compile(r"(?i)\bmerge\s+pull\s+request\b")
    structured_course_info_re = re.compile(
        r"(?i)\bdocs\s*:\s*add\s+structured\s+course\s+info\b"
    )
    readme_toml_re = re.compile(r"(?i)\breadme\.toml\b")
    update_readme_md_re = re.compile(r"(?i)^update\s+readme\.md\s+for\s+")

    for commit in filtered_commits:
        if commit["author"] == "github-actions" or commit["author"] == "actions-user":
            continue

        if ci_re.search(commit["message"]):
            continue

        if merge_pr_re.search(commit["message"]):
            continue

        if structured_course_info_re.search(commit["message"]):
            continue

        if readme_toml_re.search(commit["message"]):
            continue

        first_line = commit["message"].splitlines()[0]
        if update_readme_md_re.search(first_line):
            continue

        date = commit["date"]
        title = org_course_name.get(commit["repo_name"], commit["repo_name"])
        if prev_date != date.date():
            markdown_report += (
                f"### {chinese_weekday(date)} ({date.month}.{date.day})\n\n"
            )
            prev_date = date.date()

        markdown_report += f"- {commit['author']} 在 [{title}](https://github.com/{org_name}/{commit['repo_name']}) 中提交了信息：{commit['message'].splitlines()[0]}\n\n"

    return markdown_report


def save_report(report, news_type, display_start_time):
    """Save the generated report to a file."""
    # filename = f'content/news/{"weekly-" if news_type == "weekly" else ""}{display_start_time.date()}.md'
    if news_type == "daily":
        filename = "content/news/daily.md"
    else:
        filename = f"content/news/weekly/weekly-{display_start_time.date()}/index.md"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)


def main():
    # Load environment variables
    try:
        token = os.environ["PERSONAL_ACCESS_TOKEN"]
        org_name = os.environ["ORG_NAME"]
        news_type = os.environ["NEWS_TYPE"]
    except KeyError as e:
        raise KeyError(f"Missing required environment variable: {e}") from e

    if news_type == "weekly":
        from generate import generate_summary

    # Set SSL certificates path
    os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

    session = get_http_session()
    headers = {"Authorization": f"token {token}"}

    start_time, display_start_time = calculate_start_time(news_type)
    repos_list_url = os.getenv("REPOS_LIST_URL", DEFAULT_REPOS_LIST_URL)
    repos = get_repos_from_repos_list(session, headers, repos_list_url)
    yaml_front_matter = generate_yaml_front_matter(news_type, display_start_time)
    filtered_commits, org_course_name = fetch_commits_from_repos(
        session, headers, org_name, repos, start_time
    )

    if not os.path.exists(f"content/news/weekly/weekly-{display_start_time.date()}"):
        os.makedirs(f"content/news/weekly/weekly-{display_start_time.date()}")

    if filtered_commits:
        markdown_report = create_markdown_report(
            filtered_commits, org_course_name, news_type, org_name
        )

        final_report = f"---\n{yaml_front_matter}---\n\n"

        if news_type == "weekly":
            # try:
            #     generate_image(markdown_report)
            #     shutil.move(
            #         "generated_image.png",
            #         f"content/news/weekly/weekly-{display_start_time.date()}/generated_image.png",
            #     )
            #     final_report += "![AI Image of the Week](generated_image.png)\n\n"
            #     logging.info("AI image generated successfully.")
            # except Exception as e:
            #     logging.warning(f"Image generation failed: {e}")

            try:
                summary = generate_summary(markdown_report)
                if summary == "__NO_SUMMARY__":
                    logging.info("No summary generated, using full report instead.")
                else:
                    logging.info("AI summary generated successfully.")
                    final_report += f"{summary}\n\n"
                final_report += f"{markdown_report}"

            except Exception as e:
                logging.warning(
                    f"Summary generation failed: {e}, using full report instead."
                )
                final_report += f"{markdown_report}"

            # update content/news/weekly/_index.zh-cn.md description
            with open(
                "content/news/weekly/_index.zh-cn.md", "w", encoding="utf-8"
            ) as file:
                yaml_front_matter = yaml.dump(
                    {
                        "title": "AUTO 周报",
                        "date": datetime.datetime.now(datetime.UTC).strftime(
                            "%Y-%m-%d"
                        ),
                        "description": f"AUTO 周报是由 ChatGPT 每周五发布的一份简报，最近更新于 {datetime.datetime.now(timezone('Etc/GMT-8')).date()}。",
                    },
                    allow_unicode=True,
                )
                file.write(f"---\n{yaml_front_matter}---\n")

        else:
            final_report += f"{markdown_report}"

        save_report(final_report, news_type, display_start_time)

    else:
        print("No commits found in the given period of time")


if __name__ == "__main__":
    main()
