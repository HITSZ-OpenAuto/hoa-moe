import asyncio
import json
import os
import re
import subprocess
import time
import logging
import traceback
import aiohttp

from argparse import ArgumentParser

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


# Constants def, the gap should be larger than the total of repos
WEIGHTS = {
    "counter_man": 1,  # The available weight of the template starts from 1
    "counter_dis": 200,
    "counter_graduate": 400,
    "counter_cross": 600,
    "counter_general": 800,
    "counter_legacy": 1000,
}

COUNTERS = {
    "mandatory": "counter_man",
    "distributional-selective": "counter_dis",
    "undergraduate-graduate-course": "counter_graduate",
    "selective": "counter_graduate",
    "cross-major-selective": "counter_cross",
    "general-knowledge": "counter_general",
    "legacy": "counter_legacy",
}

SEMESTER_MAPPING = {
    "第一学年秋季": "fresh-autumn",
    "第一学年春季": "fresh-spring",
    "第一学年夏季": "fresh-summer",
    "第二学年秋季": "sophomore-autumn",
    "第二学年春季": "sophomore-spring",
    "第二学年夏季": "sophomore-summer",
    "第三学年秋季": "junior-autumn",
    "第三学年春季": "junior-spring",
    "第三学年夏季": "junior-summer",
    "第四学年秋季": "senior-autumn",
    "第四学年春季": "senior-spring",
    "研究生秋季": "graduate-autumn",
    "研究生春季": "graduate-spring",
    # Special cases
    "跨专业选修": "cross-specialty",
    "文理通识": "general-knowledge",
}

CATEGORY_MAPPING: dict[str] = {
    "必修": ("mandatory", None),
    "限选": (
        "distributional-selective",
        "[限选课选课指南](https://hoa.moe/blog/distributive-guidance-for-23/)",
    ),
    "本研共通": (
        "undergraduate-graduate-course",
        "此类课程是本科生可跨选的研究生阶段课程。它们也属限选课，但是与专业限选课性质不同，故单独列出。具体请看[研究生阶段课程选课指南](https://hoa.moe/blog/master-phd-course-selection/)。",
    ),
    "选修": ("selective", None),
    "跨专业选修": ("cross-major-selective", None),
    "文理通识": ("general-knowledge", None),
    "归档": (
        "legacy",
        "此类课程在之前的培养方案中处于较重要的地位，但由于培养方案的调整，现在不再开设了。不过，原课程资料仍保留，感兴趣的同学可以自行查阅。",
    ),
}


EXCLUDE_REPOS = [
    ".github",
    "hoa-moe",
    "HITSZ-OpenAuto",
    "repos-management",
    "hoa-previewer",
    "hoa-fastdl",
    "aextra",
]


# Pre-compiled regex for better performance
PATTERN_CATEGORY = re.compile(r"category:\s*(.*)")
PATTERN_SEMESTER = re.compile(r"semester:\s*(.*)")
PATTERN_SEMESTERS = re.compile(r"\s*/\s*")
PATTERN_NAME = re.compile(r"name:\s*(.*)")


class GitHubAPIClient:
    """A GitHub API client."""

    def __init__(self, owner: str, repo: str, token: str, index: int):
        self.owner = owner
        self.repo = repo
        self.token = token
        self.index = index
        self.session = None
        # For update semester-category file
        self.semester_category_filenames: list[str] = []
        self.name: str | None = None

    async def init_session(self):
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json",
        }
        self.session = aiohttp.ClientSession(headers=headers)

    async def close_session(self):
        if self.session:
            await self.session.close()

    async def fetch_file_content(self, path: str) -> str:
        """Fetch the content of a file from the repository."""

        url = f"https://raw.githubusercontent.com/{self.owner}/{self.repo}/main/{path}"
        async with self.session.get(url) as response:
            if response.status != 200:
                raise Exception(
                    f"Failed to fetch file content from {url}, status code: {response.status}"
                )
            return await response.text()

    def update_semester_category_file(self):
        if not self.semester_category_filenames or not self.name:
            return
        for filename in self.semester_category_filenames:
            with open(filename, "a+", encoding="utf-8") as f:
                card_link = (
                    f'{{{{< card link="{self.repo.lower()}" title="{self.name}" >}}}}\n'
                )
                f.write(card_link)


async def process_repo(client: GitHubAPIClient) -> None:
    """Process a single repository."""

    # due to async, can only concatenate log to ensure logs' coherency
    logs = []
    logs.append("-" * 50)
    logs.append(f"Processing {client.repo}")

    try:
        tag_content: str = await client.fetch_file_content("tag.txt")

        logs.append("---tag.txt---")
        logs.append(tag_content)
        logs.append("-------------")

        category_match = PATTERN_CATEGORY.search(tag_content)
        if category_match:
            category_raw = category_match.group(1)
            # For courses with the default tag, which does not exist in CATEGORY_MAPPING,
            # `get` returns None, causing error: cannot unpack non-iterable NoneType object.
            # So this should be judged specially
            if (
                category_raw.strip()
                == "必修/限选/跨专业选修/选修/本研共通/文理通识/归档"
            ):
                logger.warning(
                    "Default tag '必修/限选/跨专业选修/选修/本研共通/文理通识/归档' found, skipping process."
                )
                return  # don't raise error since this is reasonable, such as a draft repo

            category, extra_info = CATEGORY_MAPPING.get(category_raw.strip())
            logs.append(f"Matched category: {category}\n")
        else:
            raise ValueError(f"No match category {category_raw} for {client.repo}")

        if category_raw in ["跨专业选修", "文理通识"]:
            # special cases
            semesters = [category_raw]
            logs.append(f"Matched semester: {semesters}")
        else:
            semesters_match = PATTERN_SEMESTER.search(tag_content)
            if semesters_match:
                semesters_line = semesters_match.group(1)
                semesters: list[str] = PATTERN_SEMESTERS.split(
                    semesters_line
                )  # 以 / 分割多个学期
                logs.append(f"Matched semester: {semesters}")
            else:
                raise ValueError(f"No semester provided for {client.repo}")

        name_match = PATTERN_NAME.search(tag_content)
        if name_match:
            course_name = name_match.group(1)
            logs.append(f"Matched name: {course_name}")
        else:
            raise ValueError(f"No match name for course {client.repo}")

        for semester in semesters:
            semester_en = SEMESTER_MAPPING.get(semester.strip())
            if not semester_en:
                raise ValueError(
                    f"No match semester {semester} for course {course_name}"
                )

            logs.append(f"Matched semester: {semester_en}")

            semester_category_filename: str = f"{semester_en}-{category}.txt"
            if (
                not os.path.exists(semester_category_filename)
                or os.stat(semester_category_filename).st_size == 0
            ):
                c: str = f"## {category_raw.strip()}\n"
                if extra_info:
                    c += f"{extra_info}\n"
                c += "<!--more-->\n" + "{{< cards >}}\n"

                with open(semester_category_filename, "w", encoding="utf-8") as f:
                    f.write(c)
                del c

            # 保存更新学期类别文件所需的字段，以便在处理完所有 repo 后更新
            client.semester_category_filenames.append(semester_category_filename)
            client.name = course_name

            readme_content: str = await client.fetch_file_content("README.md")
            # 跳过第一行
            readme_lines = readme_content.split("\n")[1:]
            readme_content = "\n".join(readme_lines)

            # 为生成 md 文件准备的内容
            s: str = ""

            s += "---\n"
            if category != "cross-major-selective" and category != "general-knowledge":
                s += f"title: （{category_raw.strip()}）{course_name}\n"
            else:
                s += f"title: {course_name}\n"

            counter_key = COUNTERS.get(category)
            s += (
                f"weight: {WEIGHTS[counter_key] + client.index}\n"
                + "toc: true\n"
                + f'editURL: "https://github.com/{client.owner}/{client.repo}/edit/main/README.md"\n'
                + "math: true\n"
                + "---\n\n"
            )

            # python scripts/courses/gen_repo_update_time.py HITSZ-OpenAuto ${line} ${{ secrets.PERSONAL_ACCESS_TOKEN }}
            subprocess.run(
                [
                    "python",
                    "scripts/courses/gen_repo_update_time.py",
                    client.owner,
                    client.repo,
                    client.token,
                ],
                check=True,
            )
            with open(
                f"result_update_time_{client.repo}.txt", "r", encoding="utf-8"
            ) as result_file:
                s += result_file.read() + "\n"
            os.remove(f"result_update_time_{client.repo}.txt")

            s += readme_content + "\n" + "## 资料下载\n\n"
            with open(
                "scripts/infos/netdisk_notice.txt", "r", encoding="utf-8"
            ) as notice_file:
                s += notice_file.read() + "\n"
            with open(f"{client.repo}_cards.txt", "r", encoding="utf-8") as cards_file:
                s += cards_file.read() + "\n"
            with open(
                "scripts/infos/sponsor.txt", "r", encoding="utf-8"
            ) as sponsor_file:
                s += sponsor_file.read() + "\n"

            repo_md_filename = f"./content/docs/{semester_en}/{client.repo}.md"
            with open(repo_md_filename, "w", encoding="utf-8") as f:
                f.write(s)

    except Exception:
        logging.error(f"Error processing repo {client.repo}:")
        traceback.print_exc()
        logging.info("Logs before the error are:")
    finally:
        logs.append("-" * 50)
        logger.info("\n".join(logs))
    return


async def process_multiple_repos(owner: str, repos: list, token: str) -> None:
    repos = [repo for repo in repos if repo not in EXCLUDE_REPOS]
    sorted_repos = sorted(repos)  # 排序，用于在并行的情况下保证构建网页时的顺序

    clients = [
        GitHubAPIClient(owner, repo, token, index)
        for index, repo in enumerate(sorted_repos)
    ]
    tasks: list[asyncio.Task] = []

    for client in clients:
        await client.init_session()
        task = asyncio.create_task(process_repo(client))
        tasks.append(task)

    await asyncio.gather(*tasks)

    for client in clients:
        client.update_semester_category_file()  # 最后执行更新学期类别文件，以固定构建网页时的顺序
        await client.close_session()


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Generate course pages from GitHub repositories."
    )
    parser.add_argument(
        "owner", help="GitHub repository owner", default="HITSZ-OpenAuto"
    )
    parser.add_argument("token", help="GitHub token")

    args = parser.parse_args()

    repos_json = os.environ.get("repos_array")
    repos = json.loads(repos_json) if repos_json else []

    if not repos:
        raise ValueError("Environment variable REPOS_ARRAY not found")

    start_time = time.perf_counter()
    asyncio.run(process_multiple_repos(args.owner, repos, args.token))
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    logger.info(f"Exec: {execution_time:.2f} s")
