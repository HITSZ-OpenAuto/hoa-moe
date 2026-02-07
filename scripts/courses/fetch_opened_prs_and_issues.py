import subprocess
import json
import os
import re
from datetime import datetime, timedelta
import logging

TIME_ZONE = 8  # Beijing time zone


def run_gh_command(command):
    """
    Run a GitHub CLI command with optional Personal Access Token.

    :param command: List of command arguments
    :param pat: Personal Access Token (optional)
    :return: Parsed JSON output
    """
    token = os.environ.get("PERSONAL_ACCESS_TOKEN")
    try:
        if token:
            env = os.environ.copy()
            env["GH_TOKEN"] = token
        else:
            env = None

        result = subprocess.run(
            ["gh"] + command, capture_output=True, text=True, check=True, env=env
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running GitHub CLI command: {e}")
        print(f"Error output: {e.stderr}")
        return []


def get_org_issues(org_name):
    """
    Retrieve open issues for the specified organization.

    :param org_name: GitHub organization name
    :return: List of open issues
    """
    command = [
        "search",
        "issues",
        "--json",
        "title,url,repository,createdAt,author,labels",
        "--state",
        "open",
        "--owner",
        org_name,
    ]
    return run_gh_command(command)


def get_org_pull_requests(org_name):
    """
    Retrieve open pull requests for the specified organization.

    :param org_name: GitHub organization name
    :param pat: Personal Access Token (optional)
    :return: List of open pull requests
    """
    command = [
        "search",
        "prs",
        "--json",
        "title,url,repository,createdAt,author,labels",
        "--state",
        "open",
        "--owner",
        org_name,
    ]
    return run_gh_command(command)


def UTC2BJT(UTC_time_str):
    """
    Convert UTC time(in form of ISO 8601) to Beijing time.

    :param UTC_time_str: UTC time string, in form of ISO 8601
    :return: Beijing time string, in the form of 1970-01-01 00:00:00
    """
    UTC_time = datetime.strptime(UTC_time_str, "%Y-%m-%dT%H:%M:%SZ")
    Beijing_time = UTC_time + timedelta(hours=TIME_ZONE)
    Beijing_time_str = Beijing_time.strftime("%Y-%m-%d %H:%M:%S")
    return Beijing_time_str


def fetch_opened_prs_and_issues(org_name, public_repos):
    """
    Generate a markdown report of open issues and pull requests.

    :param org_name: GitHub organization name
    :param public_repos: public repositories of the org
    :param pat: Personal Access Token (optional)
    """
    # Get issues and PRs
    issues = get_org_issues(org_name)
    prs = get_org_pull_requests(org_name)

    # Generate markdown report
    with open("content/news/daily.md", "r+") as f:
        content = f.read()
        f.seek(0)
        # Keep content before "## 待解决的 Issues" and overwrite the rest
        if "## 待解决的 Issues" in content:
            f.write(content.split("## 待解决的 Issues")[0])
        else:
            f.write(content)
        f.write("## 待解决的 Issues\n\n")
        f.truncate()

        filtered_issues = [p for p in issues if p["repository"]["name"] in public_repos]

        if not filtered_issues:
            f.write("暂无待解决的 Issues\n\n")
        else:
            for issue in filtered_issues:
                f.write(f"### [{issue['title']}]({issue['url']})\n\n")
                f.write(f"- **仓库**: {issue['repository']['name']}\n")
                f.write(f"- **创建于**: {UTC2BJT(issue['createdAt'])}\n")
                f.write(f"- **作者**: {issue['author']['login']}\n")

                # Labels (if any)
                if issue["labels"]:
                    label_list = ", ".join([label["name"] for label in issue["labels"]])
                    f.write(f"- **标签**: {label_list}\n")

                f.write("\n")

        f.write("## 待合并的 Pull Requests\n\n")

        ci_pr_re = re.compile(r"(?i)\bci\s*[:：]")
        filtered_prs = [
            p
            for p in prs
            if p["repository"]["name"] in public_repos and not ci_pr_re.search(p["title"])
        ]

        if not filtered_prs:
            f.write("暂无待合并的 Pull Requests\n\n")
        else:
            for pr in filtered_prs:
                f.write(f"### [{pr['title']}]({pr['url']})\n\n")
                f.write(f"- **仓库**: {pr['repository']['name']}\n")
                f.write(f"- **创建于**: {UTC2BJT(pr['createdAt'])}\n")
                f.write(f"- **作者**: {pr['author']['login']}\n")

                if pr["labels"]:
                    label_list = ", ".join([label["name"] for label in pr["labels"]])
                    f.write(f"- **标签**: {label_list}\n")

                f.write("\n")

    logging.info("Report updated: content/news/daily.md")


def main():
    try:
        owner = os.environ["ORG_NAME"]
    except KeyError as e:
        raise ValueError(
            f"Environment variable {e} not found, please set it first."
        ) from e

    if not owner:
        raise ValueError(
            "Environment variable ORG_NAME not found, please set it first."
        )

    repos_json = os.environ.get("repos_array")
    public_repos = json.loads(repos_json) if repos_json else []

    fetch_opened_prs_and_issues(owner, public_repos)


if __name__ == "__main__":
    main()
