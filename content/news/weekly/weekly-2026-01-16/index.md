---
authors:
  - image: https://github.com/openai.png
    link: https://github.com/openai
    name: ChatGPT
date: "2026-01-23"
draft: false
excludeSearch: false
title: AUTO 周报 2026-01-16 - 2026-01-23
---

## 本周更新摘要

- hoa-majors（专业/培养方案工具）
  - 大量重构与功能加强：项目重组为 src/、data/、tests/；扁平化并重命名 SCHOOL_MAJORS 为 plans；合并并统一 CLI 命令入口，新增 list course/plans/query、repo 等命令与版本信息；将打印替换为日志、改进核心逻辑并加入测试/CI（GitHub Action）。
  - 打包与兼容性：把 data 目录打包进包中，更新构建配置与依赖（pyproject.toml / uv.lock），Python 要求升级为 3.14。
  - 文档与开发环境：新增通过 uv tool 的安装说明并更新使用文档，添加 Makefile、pre-commit 配置与 LICENSE。
  - 其他：移除无用 lookup 工具并清理历史中的临时/私有文件，格式与 lint 修复。

- hoa-fastdl（静态资源加速）
  - 新增/完善：创建详细 README（含部署徽章）、加入 MIT 许可；增强请求处理逻辑以支持 robots.txt。
  - 部署与代码调整：重命名入口为 index.js，调整 wrangler 配置（兼容日期、smart placement 等），移除默认变量回退与部分部署引用。

- hoa-previewer（预览渲染器）
  - 架构与体验改进：迁移到 Cloudflare Workers，使用 streamdown 改进 Markdown 渲染，修复数学插件类型与运行时检测问题，提升文本换行样式。
  - 维护性提升：升级依赖、添加 prettier、移除未使用依赖并加入 knip 配置，若干格式与 lint 修复。

- CrossSpecialty（跨专业选修）
  - 新增课程：加入“走进量子世界”、“公司并购与估值”与“绿色金融与碳排放权交易”。

- 自动控制实践 B (AUTO3002B)
  - 教学资料与文档：添加本部“智能系统控制实践”课程资料并支持 README 双校区切换；重构 README 结构、移除 tabs 组件并修复页面构建问题。

- 凸优化与最优控制 (AUTO5023)
  - 上传了 25 秋学期回忆试题与大作业。

- hoa-fuma
  - 增加了 CourseInfo 组件以完善课程信息展示；同时清理了 .vscode/.claude 等不必要文件。

- 其他课程更新（简要）
  - ECON2005F：补充署名/贡献者信息。
  - MATH1004：补充教师信息与考试情况。
  - PHYS1001：补充大学物理部分课程信息。
  - COMP2051：修改并增添数字逻辑设计的课程内容。
  - GeneralKnowledge：补充文理通识课程信息。
  - EE2004：新增一份高等电路笔记。
  - AUTO2005：修正错误链接。

- 其它零碎维护（概括）
  - 多个仓库进行了格式化、lint 修复、依赖升级、文件重命名、忽略规则更新及删除无意义的 README/临时文件等常规维护。

## 更新内容

### 周四 (1.22)

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：docs: add installation instructions via uv tool install

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：feat(cli): add repo command to lookup OpenAuto repository IDs (#3)

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：feat: add version information

- W. D. Gaster 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：上传只保留目前组织里仓库相关的特殊映射的 lookup table (#1)

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：style: fix format and lint issues

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：feat: add pre-commit hooks, Makefile, and LICENSE

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：feat: add pre-commit configuration and Makefile for development setup

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：refactor: implement JW_COOKIE warning logging in fetcher

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：chore: remove lookup table tooling

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：refactor: rename folder SCHOOL_MAJORS to plans

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：refactor: rename CLI files to match command names

- Kowyo 在 [hoa-fastdl](https://github.com/HITSZ-OpenAuto/hoa-fastdl) 中提交了信息：docs: update README with detailed usage and operational logic

- Lurker 在 [跨专业选修课程体系](https://github.com/HITSZ-OpenAuto/CrossSpecialty) 中提交了信息：增加了走进量子世界课程 (#16)

- Kowyo 在 [hoa-fastdl](https://github.com/HITSZ-OpenAuto/hoa-fastdl) 中提交了信息：chore: update compatibility date in wrangler.toml to 2026-01-20

- Kowyo 在 [hoa-fastdl](https://github.com/HITSZ-OpenAuto/hoa-fastdl) 中提交了信息：chore: rename entry to index.js

- Kowyo 在 [hoa-fastdl](https://github.com/HITSZ-OpenAuto/hoa-fastdl) 中提交了信息：feat: add support for robots.txt in request handling

- Kowyo 在 [hoa-fastdl](https://github.com/HITSZ-OpenAuto/hoa-fastdl) 中提交了信息：chore: enable smart placement and run_worker_first in wrangler.toml

- Kowyo 在 [hoa-fastdl](https://github.com/HITSZ-OpenAuto/hoa-fastdl) 中提交了信息：chore: add MIT license

- Kowyo 在 [hoa-fastdl](https://github.com/HITSZ-OpenAuto/hoa-fastdl) 中提交了信息：chore: remove deployment references

- Kowyo 在 [hoa-fastdl](https://github.com/HITSZ-OpenAuto/hoa-fastdl) 中提交了信息：feat: remove default variable fallbacks in worker.js

- Kowyo 在 [hoa-fastdl](https://github.com/HITSZ-OpenAuto/hoa-fastdl) 中提交了信息：docs: create README and add deployment badge

### 周三 (1.21)

- Hye 在 [自动控制实践 B](https://github.com/HITSZ-OpenAuto/AUTO3002B) 中提交了信息：调整 README 结构，删去了 tabs 组件，修复页面构建的问题。 (#28)

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：feat: implement CourseInfo component (#14)

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：chore: remove .vscode and .claude from git and ignore them

- Anastasia-Charies 在 [经济学原理](https://github.com/HITSZ-OpenAuto/ECON2005F) 中提交了信息：补充署名，以便后面贡献的同学编写 (#21)

- Costannt 在 [自动控制实践 B](https://github.com/HITSZ-OpenAuto/AUTO3002B) 中提交了信息：添加本部「智能系统控制实践」课程资料并支持 README 双校区切换 (#27)

- Pengjie Wang 在 [文理通识课程体系](https://github.com/HITSZ-OpenAuto/GeneralKnowledge) 中提交了信息：补充文理通识课程信息 (#20)

- Pengjie Wang 在 [概率论与数理统计](https://github.com/HITSZ-OpenAuto/MATH1004) 中提交了信息：增加了教师信息、考试情况补充 (#36)

- Pengjie Wang 在 [大学物理](https://github.com/HITSZ-OpenAuto/PHYS1001) 中提交了信息：增加了大学物理课程部分信息 (#30)

- Pengjie Wang 在 [数字逻辑设计](https://github.com/HITSZ-OpenAuto/COMP2051) 中提交了信息：修改、增添了数字逻辑设计课程一些内容 (#16)

### 周二 (1.20)

- Pengjie Wang 在 [跨专业选修课程体系](https://github.com/HITSZ-OpenAuto/CrossSpecialty) 中提交了信息：添加了两门跨专业课程：公司并购与估值、绿色金融与碳排放权交易 (#17)

- youyun0v0 在 [高等电路与电子分析](https://github.com/HITSZ-OpenAuto/EE2004) 中提交了信息：增加一份高电课程笔记 (#17)

- Jiao Ziang 在 [信号分析与处理](https://github.com/HITSZ-OpenAuto/AUTO2005) 中提交了信息：修改错误链接 (#38)

- Kowyo 在 [hoa-previewer](https://github.com/HITSZ-OpenAuto/hoa-previewer) 中提交了信息：chore: update compatibility date

- Kowyo 在 [hoa-previewer](https://github.com/HITSZ-OpenAuto/hoa-previewer) 中提交了信息：style: format code

- Kowyo 在 [hoa-previewer](https://github.com/HITSZ-OpenAuto/hoa-previewer) 中提交了信息：style: enhance MarkdownComponent styling for better text wrapping

- Kowyo 在 [hoa-previewer](https://github.com/HITSZ-OpenAuto/hoa-previewer) 中提交了信息：fix: update math plugin type definition

- Kowyo 在 [hoa-previewer](https://github.com/HITSZ-OpenAuto/hoa-previewer) 中提交了信息：fix: replace any types with unknown to resolve lint errors

- Kowyo 在 [hoa-previewer](https://github.com/HITSZ-OpenAuto/hoa-previewer) 中提交了信息：chore: add prettier and format codebase

- Kowyo 在 [hoa-previewer](https://github.com/HITSZ-OpenAuto/hoa-previewer) 中提交了信息：fix: remove unused dependencies identified by knip

- Kowyo 在 [hoa-previewer](https://github.com/HITSZ-OpenAuto/hoa-previewer) 中提交了信息：chore: add knip configuration

- Kowyo 在 [hoa-previewer](https://github.com/HITSZ-OpenAuto/hoa-previewer) 中提交了信息：refactor: use streamdown to render markdown component

- Kowyo 在 [hoa-previewer](https://github.com/HITSZ-OpenAuto/hoa-previewer) 中提交了信息：fix: solve build error by checking for katexInstance

- Kowyo 在 [hoa-previewer](https://github.com/HITSZ-OpenAuto/hoa-previewer) 中提交了信息：style: fix lint issues in App and components

- Kowyo 在 [hoa-previewer](https://github.com/HITSZ-OpenAuto/hoa-previewer) 中提交了信息：chore: bump dependencies to latest

- Kowyo 在 [hoa-previewer](https://github.com/HITSZ-OpenAuto/hoa-previewer) 中提交了信息：chore: migrate from Cloudflare Pages to Workers

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：refactor: replace print statements with logging in CLI tools

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：fix: update smoke tests

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：chore: update build system and dependencies in pyproject.toml

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：chore: reorder build-system section in pyproject.toml

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：refactor: consolidate CLI commands under a single entry point

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：refactor: bundle data directory into package and update CLI tools

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：feat(ci): add GitHub Action for HOA Majors CLI setup

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：chore: update Python version requirement in uv.lock to 3.14

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：refactor: improve project structure, core logic, and CLI consistency

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：feat: add list course/plans/query commands

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：chore: update Python version requirements to 3.14

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：fix: format code and resolve lint issues with ruff

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：refactor: flatten and rename SCHOOL_MAJORS data structure

- 345ljh 在 [凸优化与最优控制](https://github.com/HITSZ-OpenAuto/AUTO5023) 中提交了信息：上传 25 秋回忆试题与大作业 (#17)

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：chore: ignore .claude and .cursor and remove them from git history

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：docs: update usage using uv

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：Update .gitignore with standard Python ignore patterns

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：Add uv.lock

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：Refactor project structure: reorganize into src/, data/, and tests/
