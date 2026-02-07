import os
import re
from pathlib import Path


DEFAULT_ORG_NAME = "HITSZ-OpenAuto"

# Only clean meta/tooling repos (keep historical course repos even if renamed)
DEFAULT_CLEAN_PREFIXES = ("hoa-", "fuma", "aextra", "repos")


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


def clean_markdown_body(body: str, org_name: str, clean_prefixes: tuple[str, ...]) -> str:
    link_re = re.compile(rf"https://github\.com/{re.escape(org_name)}/([^\s)]+)")

    def should_clean(repo: str) -> bool:
        return repo.startswith(clean_prefixes)

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

            # If the header itself points to a repo we want to clean, drop the whole section.
            header_repo = None
            m_header = link_re.search(section[0])
            if m_header:
                header_repo = m_header.group(1)
            if header_repo and should_clean(header_repo):
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
                        if should_clean(repo):
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
    root = Path("content/news/weekly")

    prefixes_env = os.getenv("CLEAN_PREFIXES")
    clean_prefixes = (
        tuple(p.strip() for p in prefixes_env.split(",") if p.strip())
        if prefixes_env
        else DEFAULT_CLEAN_PREFIXES
    )

    changed_files = 0

    for path in root.rglob("*.md"):
        if path.name.startswith("_index"):
            continue

        original = path.read_text(encoding="utf-8")
        front, body = split_front_matter(original)
        cleaned_body = clean_markdown_body(body, org_name, clean_prefixes)
        cleaned = front + cleaned_body

        if cleaned != original:
            path.write_text(cleaned, encoding="utf-8")
            changed_files += 1

    print(f"Cleaned weekly reports. Changed files: {changed_files}")


if __name__ == "__main__":
    main()
