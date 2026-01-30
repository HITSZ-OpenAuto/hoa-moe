---
authors:
  - image: https://github.com/openai.png
    link: https://github.com/openai
    name: ChatGPT
date: "2026-01-30"
draft: false
excludeSearch: false
title: AUTO 周报 2026-01-23 - 2026-01-30
---

## 本周更新摘要

- hoa-fuma（课程网站/内容平台）
  - 继续大规模迭代：新增并完善站点功能与内容管线，包括 CourseInfo 和 FileTree 组件、博客布局与文章迁移、Documentation/Blog/GitHub 链接、主题色（shadcn）与首页布局优化。
  - 构建与发布流程增强：增加 CI 工作流（包含 PR 预览）、构建/部署优化、将生成内容推送到 production 分支、下载 worktree.json、性能与脚本重构（模块化课程抓取、生成页面等）。
  - 代码质量与项目治理：添加 MIT 许可、README 与贡献指南、格式化/提交检查（prettier、eslint、husky 等）。
  - 小变更汇总：删除冗余文件（如 llms-full.txt）、依赖升级、若干布局/lint 修复与小逻辑调整。

- repos-management（仓库管理）
  - 上传了成绩构成信息；GitHub Actions 自动更新了仓库列表（CI 自动化更新）。

- 课程元数据 / 自动生成 TOML
  - 凸优化与最优控制 (AUTO5023)：新增结构化课程信息文件（AUTO5023.toml）。
  - 大学物理实验 (PHYS1002) 与 程序设计思维与实践 (COMP1011)：合并并应用了自动生成的 TOML（元数据自动化相关合并）。

- 课程模板 / 示例
  - （示例）大学物理实验（course-template）：合并了数据库课程信息功能（feature/database-course-info）。

- 学科课程内容更新
  - 文理通识课程体系（GeneralKnowledge）：增加并修改了对三门文理通识课程的描述。
  - 跨专业选修课程体系（CrossSpecialty）：新增两门课程描述，并加入行星科学课程说明。
  - 自动化专业导论（AUTO2001）：修正教师评价展示的多余横线。
  - 数字逻辑设计（COMP2051）：增加数字电路/实验描述。
  - 大学物理（PHYS1001）：补充了教师马永辉的评价。
  - hoa-majors：简化输出格式。

- 新建/初始化项目
  - hoa-make_toml：首次提交/初始化（first commit / first_pr）。

- 其他（琐碎操作一并说明）
  - 若干仓库进行了删改小文件、文件重命名、格式微调、移除开发配置（.vscode/.claude）、依赖提升与小范围逻辑修复等常规维护操作。

（摘要以本周仓库提交为准，重点突出新增文档、元数据、站点组件与 CI/发布改进）

## 更新内容

### 周五 (1.30)

- Jiao Ziang 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：上传成绩构成信息

- JLPL666 在 [hoa-make_toml](https://github.com/HITSZ-OpenAuto/hoa-make_toml) 中提交了信息：first_pr

- JLPL666 在 [hoa-make_toml](https://github.com/HITSZ-OpenAuto/hoa-make_toml) 中提交了信息：first commit

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：feat: home page layout (#28)

- Jiao Ziang 在 [凸优化与最优控制](https://github.com/HITSZ-OpenAuto/AUTO5023) 中提交了信息：docs: add structured course info (AUTO5023.toml) (#20)

- Jiao Ziang 在 [大学物理实验](https://github.com/HITSZ-OpenAuto/PHYS1002) 中提交了信息：Merge pull request #66 from HITSZ-OpenAuto/ci/auto-generate-toml-1768250009

- Jiao Ziang 在 [程序设计思维与实践](https://github.com/HITSZ-OpenAuto/COMP1011) 中提交了信息：Merge pull request #23 from HITSZ-OpenAuto/ci/auto-generate-toml-1768250740

### 周四 (1.29)

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：ci: add preview workflow for PRs (#29)

### 周三 (1.28)

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：feat: add Documentation, Blog, and GitHub links (#27)

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：ci: improve build and deployment pipeline

- kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：docs: migrate blog posts

### 周二 (1.27)

- kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：fix: blog page layout and banner improvements

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：feat: use shadcn theme color (#23)

### 周一 (1.26)

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：docs: update README and add contributing guide

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：chore: track blog content

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：refactor: update fumadocs collections and blog source configuration

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：chore: add MIT license

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：ci: push generated content to production branch

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：fix: deslop - reorganize components and fix lint issues (#22)

### 周日 (1.25)

- Mingjia Zhou 在 [文理通识课程体系](https://github.com/HITSZ-OpenAuto/GeneralKnowledge) 中提交了信息：增加了对三门文理通识课程的描述 且将表述进行了修改 (#22)

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：fix: remove llms-full.txt

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：feat: add FileTree component with JSON-to-tree transformation (#21)

- Kowyo 在 [自动化专业导论](https://github.com/HITSZ-OpenAuto/AUTO2001) 中提交了信息：移除教师评价中多余的横线

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：refactor(scripts): modularize and optimize course fetching logic

- Jiao Ziang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/course-template) 中提交了信息：Merge pull request #23 from HITSZ-OpenAuto/feature/database-course-info

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：feat: download worktree.json in fetch_repo_data and rename fetch_readme

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：refactor: extract generate_pages and hardcode directory paths

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：perf: optimize course build script (#18)

- cecilia 在 [数字逻辑设计](https://github.com/HITSZ-OpenAuto/COMP2051) 中提交了信息：增加对数逻实验的描述 (#17)

- cecilia 在 [大学物理](https://github.com/HITSZ-OpenAuto/PHYS1001) 中提交了信息：增加马永辉教师的评价 (#31)

### 周六 (1.24)

- Mingjia Zhou 在 [跨专业选修课程体系](https://github.com/HITSZ-OpenAuto/CrossSpecialty) 中提交了信息：增加了对两门跨专业课程的描述 (#19)

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：feat(ci): init building course pages workflow (#16)

- Kowyo 在 [hoa-majors](https://github.com/HITSZ-OpenAuto/hoa-majors) 中提交了信息：feat: simplify output

- Lurker 在 [跨专业选修课程体系](https://github.com/HITSZ-OpenAuto/CrossSpecialty) 中提交了信息：加入了行星科学课程说明 (#18)

- GitHub Actions 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：ci: update repositories list [automated]

### 周三 (1.21)

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：feat: implement CourseInfo component (#14)

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：chore: remove .vscode and .claude from git and ignore them

### 周三 (1.7)

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：chore: bump dependencies

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：feature: implement blog layout (#12)

### 周四 (1.1)

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：chore: setup husky, lint-staged and commitlint

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：feat: add prettier-plugin-tailwindcss

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：feat: add prettier and eslint-config-prettier for code formatting

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：chore: organize file structure

### 周一 (12.29)

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：fix logic

- Kowyo 在 [hoa-fuma](https://github.com/HITSZ-OpenAuto/hoa-fuma) 中提交了信息：add checkbox visibility
