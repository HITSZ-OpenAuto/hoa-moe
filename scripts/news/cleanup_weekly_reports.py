import os
import re
from pathlib import Path

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


DEFAULT_ORG_NAME = "HITSZ-OpenAuto"
DEFAULT_REPOS_LIST_URL = (
    "https://raw.githubusercontent.com/HITSZ-OpenAuto/repos-management/main/repos_list.txt"
)


def get_http_session():
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session


def load_allowed_repos(session, repos_list_url: str) -> set[str]:
    resp = session.get(repos_list_url)
    if resp.status_code != 200:
        raise RuntimeError(
            f"Failed to fetch repos list from {repos_list_url}: {resp.status_code}"
        )

    allowed: set[str] = set()
    for raw in resp.text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        allowed.add(line.split("/", 1)[-1])
    return allowed


_SECTION_HEADER_RE = re.compile(r"^#{3,4}\s+")
_BULLET_RE = re.compile(r"^\s*-\s+")


def split_front_matter(text: str) -> tuple[str, str]:
    """Return (front_matter, body). front_matter includes the trailing '---\n'."""
    if not text.startswith("---\n"):
        return "", text

    # Find the second '---' line
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return "", text

    front = parts[0] + "\n---\n"
    body = parts[1]
    return front, body


def clean_markdown_body(body: str, org_name: str, allowed_repos: set[str]) -> str:
    link_re = re.compile(rf"https://github\.com/{re.escape(org_name)}/([^\s)]+)")

    lines = body.splitlines(keepends=True)
    out: list[str] = []

    i = 0
    while i < len(lines):
        line = lines[i]
        if _SECTION_HEADER_RE.match(line):
            section: list[str] = [line]
            i += 1
            while i < len(lines) and not _SECTION_HEADER_RE.match(lines[i]):
                section.append(lines[i])
                i += 1

            # If the header itself points to a repo not in the allowlist, drop the whole section.
            header_repo = None
            m_header = link_re.search(section[0])
            if m_header:
                header_repo = m_header.group(1)
            if header_repo and header_repo not in allowed_repos:
                if out and out[-1].strip() != "":
                    out.append("\n")
                continue

            cleaned = []
            cleaned.append(section[0])
            skip_next_blank = False

            for j in range(1, len(section)):
                l = section[j]
                if skip_next_blank and l.strip() == "":
                    skip_next_blank = False
                    continue
                skip_next_blank = False

                if _BULLET_RE.match(l):
                    m = link_re.search(l)
                    if m:
                        repo = m.group(1)
                        if repo not in allowed_repos:
                            skip_next_blank = True
                            continue

                cleaned.append(l)

            # If section has no bullet items left (and no non-empty content), drop it.
            has_content = any(
                (_BULLET_RE.match(l) or l.strip()) for l in cleaned[1:]
            )
            has_bullets = any(_BULLET_RE.match(l) for l in cleaned[1:])
            if has_content and has_bullets:
                out.extend(cleaned)
            else:
                # keep a single blank line to avoid gluing unrelated blocks
                if out and out[-1].strip() != "":
                    out.append("\n")
        else:
            out.append(line)
            i += 1

    # Normalize excessive blank lines
    text = "".join(out)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text


def main():
    org_name = os.getenv("ORG_NAME", DEFAULT_ORG_NAME)
    repos_list_url = os.getenv("REPOS_LIST_URL", DEFAULT_REPOS_LIST_URL)
    root = Path("content/news/weekly")

    session = get_http_session()
    allowed_repos = load_allowed_repos(session, repos_list_url)

    changed_files = 0

    for path in root.rglob("*.md"):
        if path.name.startswith("_index"):
            continue

        original = path.read_text(encoding="utf-8")
        front, body = split_front_matter(original)
        cleaned_body = clean_markdown_body(body, org_name, allowed_repos)
        cleaned = front + cleaned_body

        if cleaned != original:
            path.write_text(cleaned, encoding="utf-8")
            changed_files += 1

    print(f"Cleaned weekly reports. Changed files: {changed_files}")


if __name__ == "__main__":
    main()
