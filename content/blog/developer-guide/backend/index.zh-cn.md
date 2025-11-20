---
title: 后端架构概览
description: OpenAuto 开发者指南（贰）
date: 2025-01-27
authors:
  - name: longlin li
    link: https://github.com/longlin10086
    image: https://github.com/longlin10086.png
excludeSearch: false
math: true
weight: 3
next: /blog/developer-guide/frontend/
prev: /blog/developer-guide/maintenance
---

> [!WARNING]
> 本文将主要涉及 Python 脚本的编写，可能需要一定的 Python 基础知识。

我们的网站后端主要是围绕与 GitHub API 的交互，涉及很多网络请求，为减少运行时间开销，脚本内使用了很多异步编程。

> 异步编程是一种编程模式，用于处理可能会花费较长时间的操作，而不会阻塞其他代码的执行。

我们会以当前最重要的 `scripts/build_course_pages.py` 为例，逐步理清整个脚本到底做了些什么工作。

## 🏠基本介绍

在确定前端框架后，我们需要着手解决内容迁移的问题。如果采用手动方式将各个文档逐一复制，不仅工作量巨大，也不便于后期扩展。因此，我们计划开发自动化脚本，用于获取当前所有公开课程仓库的内容，包括分散在各仓库中的 README 文档以及已上传的资料元信息。同时，我们将借助 GitHub Action 实现定期检测：按照设定的时间间隔自动查询各课程仓库的更新状态，并据此判断是否需要重新构建内容。

在项目初期，由于课程仓库和网站功能相对简单，我们采用了直接在 workflow yaml 文件中编写 shell 脚本的方式。随着项目规模的扩大，脚本的复杂度也随之提升。这促使我们进行了一系列优化：

1. 将部分难以用 shell 实现的功能提取出来，**改用更易维护的 Python 脚本**
2. 为了解决因网络请求增多导致的执行时间过长问题，在一次大规模更新中将同步处理改为了**异步处理**
3. 为提升代码的可维护性，把原本集成在 yaml 文件中的所有 shell 脚本都独立出来，统一存放在 scripts 文件夹下。

```sh
.
├── about
│   ├── __init__.py
│   └── update_about.py
├── courses
│   ├── __init__.py
│   ├── build_course_pages.py
│   ├── fetch_opened_prs_and_issues.py
│   ├── gen_links.py
│   └── wrap_badges.py
├── filetrees
│   ├── __init__.py
│   ├── filetree_manager.py
│   └── filetrees.json
├── infos
│   ├── netdisk_notice.txt
│   └── sponsor.txt
├── news
│   ├── __init__.py
│   ├── gen_news.py
│   └── generate.py
├── workflows
│   ├── build_directory_pages.sh
│   └── build_semester_pages.sh
├── __init__.py
├── pyproject.toml
└── uv.lock
```

## 📄生成课程文档

`build_course_pages.py` 整个脚本的主要目的便是从 GitHub 课程仓库获取课程信息，并生成课程页面。在 `course.yaml` 中，我们可以看到脚本是通过如下方式被调用的：

```yaml
jobs:
  build-documentation:
    runs-on: ubuntu-22.04
    permissions:
      contents: write
      id-token: write
    env:
      PYTHONPATH: /home/runner/work/hoa-moe/hoa-moe
    steps:
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r scripts/requirements.txt

      # 获取 OpenAuto 组织下仓库名等步骤已省去，具体内容可自行查看 .github/workflow/course.yaml

      - name: Build course pages
        run: python scripts/courses/build_course_pages.py
```

> [!WARNING]
> 注意，此处出现代码为方便理解在部分地方做了修改。

既已知道脚本的调用方式，我们便可以先从脚本的 main 函数入手：

```py
if __name__ == "__main__":
    # 1. 设置命令行参数
    #    命令行内使用 python scripts/courses/build_course_pages.py HITSZ-OpenAuto token 调用
    parser = ArgumentParser(description="Generate course pages from GitHub repositories.")
    parser.add_argument("owner", help="GitHub repository owner", default="HITSZ-OpenAuto")
    parser.add_argument("token", help="GitHub token")

    # 2. 从环境变量获取仓库列表
    #    查看 course.yaml 可以发现，在之前步骤中已经把可用仓库名设置成了 repos_array 的环境变量
    repos_json = os.environ.get("repos_array")
    repos = json.loads(repos_json) if repos_json else []

    # 3. 记录执行时间并运行主要处理函数
    #    进入下一个函数 -> process_multiple_repos
    start_time = time.perf_counter()
    asyncio.run(process_multiple_repos(args.owner, repos, args.token))
    end_time = time.perf_counter()
    execution_time = end_time - start_time
```

大部分代码还是很好理解的，下面让我们进入 `process_multiple_repos` 函数看看吧。

### `process_multiple_repos`

```py
async def process_multiple_repos(owner: str, repos: list, token: str) -> None:
    # 1.排序，用于在并行的情况下保证构建网页时的顺序
    sorted_repos = sorted(repos)

    # 2. 为每个仓库创建一个 GitHubAPIClient 实例
    #    只需要知道这个类主要是用来和 GitHub 网络通信拿取有关信息就行
    clients = [GitHubAPIClient(owner, repo, token, index) for index, repo in enumerate(sorted_repos)]
    tasks: list[asyncio.Task] = []

    # 3. 使用异步方式并行处理所有仓库
    #    为每个仓库都单独创建一个执行 process_repo 函数的 task，每个 task 可以同时执行（只消耗一份时间）
    for client in clients:
        await client.init_session()
        task = asyncio.create_task(process_repo(client))
        tasks.append(task)

    await asyncio.gather(*tasks) # 等待所有 task 执行完毕

    # 4. 最后更新学期类别文件并关闭所有会话
    for client in clients:
        client.update_semester_category_file()  # 最后执行更新学期类别文件，以固定构建网页时的顺序
        await client.close_session()
```

本函数的作用便是把各个仓库的主要执行函数分成能异步执行的一个个 task，节约时间开销。现在让我们看看整个脚本的最重要任务 `process_repo` 在干嘛吧。

### `process_repo`

```py
async def process_repo(client: GitHubAPIClient) -> None:
    # 1. 读取仓库中的 tag.txt 文件获取课程信息（类别、学期、课程名等）
    tag_content: str = await client.fetch_file_content("tag.txt")

    # 2. 根据学期和类别信息创建或更新相应的分类文件
    # 课程类别，如必修
    category_match = PATTERN_CATEGORY.search(tag_content)
        if category_match:
            category_raw = category_match.group(1)
            category, extra_info = CATEGORY_MAPPING.get(category_raw.strip())

        # 开课学期
        if category_raw in ["跨专业选修", "文理通识"]:
            # special cases
            semesters = [category_raw]
        else:
            semesters_match = PATTERN_SEMESTER.search(tag_content)
            # ...

        # 课程名称
        name_match = PATTERN_NAME.search(tag_content)
        #...

    # 一个课程可能会有多个学期
    for semester in semesters:

        # 3. 获取 README.md 的内容
        readme_content: str = await client.fetch_file_content("README.md")

        # 4. 生成包含课程信息、更新时间、README 内容等的完整课程页面
        s: str = ""
        s += "---\n"
        s += f"title: {course_name}\n"
        s += (
            "toc: true\n"
            + f'editURL: "https://github.com/{client.owner}/{client.repo}/edit/main/README.md"\n'
            + "math: true\n"
            + "---\n\n"
        )

        s += readme_content + "\n"

        # 5. 添加资料下载、网盘提示和赞助信息
        s += "## 资料下载\n\n"
        with open("scripts/infos/netdisk_notice.txt", "r", encoding="utf-8") as notice_file:
            s += notice_file.read() + "\n"
        with open(f"{client.repo}_cards.txt", "r", encoding="utf-8") as cards_file:
            s += cards_file.read() + "\n"
        with open("scripts/infos/sponsor.txt", "r", encoding="utf-8") as sponsor_file:
            s += sponsor_file.read() + "\n"

        # 6. 将生成的界面内容写入对应路径下的 Markdown 文档
        repo_md_filename = f"./content/docs/{semester_en}/{client.repo}.md"
        with open(repo_md_filename, "w", encoding="utf-8") as f:
            f.write(s)
```

你可以打开一个我们课程的 Markdown 文档的源码比对着看，相信你很快就能知道文档的各部分是怎么来的了。
