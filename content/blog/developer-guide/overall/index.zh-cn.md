---
title: 整体架构概览
description: OpenAuto 开发者指南（零）
date: 2025-01-24
authors:
  - name: longlin li
    link: https://github.com/longlin10086
    image: https://github.com/longlin10086.png
excludeSearch: false
math: true
weight: 1
next: false
prev: /blog/developer-guide/frontend/
---

如何用一句话介绍完 OpenAuto 项目的主要内容及技术栈？~~（感谢 Claude-3.5 Sonnet）~~

> 我们构建了一个基于 Hugo 静态站点生成器和 GitHub Action 持续集成与部署工作流的开放式资源共享平台，致力于知识传播和技术交流。

与大多数托管在 GitHub 的资源共享项目不同，我们有着对用户更加友好的前端页面展示；也因此，我们的项目是一个集成前端、后端和运维的全栈型项目，无论是相关功能添加还是日常维护都需要一定的学习成本与技术积累，部分新人开发者可能会望而却步。本指南旨在改变这一状况，用简单明了的语言介绍清楚网站的整体架构，方便新人开发者快速上手开发。

具体架构指南将分为三部分：

- [前端架构详解 - 如何修改网站样式](/blog/developer-guide/frontend/)
- [后端架构详解 - 网站脚本的工作原理](/blog/developer-guide/backend/)
- [运维架构详解 - 我们的网站工作流](/blog/developer-guide/maintenance/)

而在本篇，我们会着眼于三者之间的联系而忽略大部分技术细节，简要剖析 OpenAuto 的网站是如何搭建起来的。

```sh
tree -L 1 .
# hoa-moe 文件树
.
├── archetypes
├── assets          # 包含自定义的 CSS 样式、JS 脚本
├── content         # 存放 md 文件，Hugo 能自动将其中的 markdown 文件转化成相应 HTML 网页
├── i18n            # 语言相关配置
├── layouts         # 包含自定义的 HTML 框架
├── public          # Hugo 最终构建出的产物（即网站本体），一般不需要做任何改动，也不会被同步到 GitHub 远端仓库中
├── scripts         # 存放 HOA 后端脚本文件
├── static          # 存放网站相关静态文件，如 Logo、缩略图等
├── themes          # Hugo 主题模块文件夹
└── hugo.yaml       # 网站基础配置文件
```

## 🦴骨架 —— Hugo

先借用 WikiPedia 里对 Hugo 的介绍：

> Hugo 是一个用 Go 编写的静态网站生成器。Hugo 把用户提供的数据文件、i18n 包、配置、布局模板、静态文件，以及用 Markdown 编写的内容，处理并生成一个完整的静态网站。较出色的功能包括多语言支持、图像处理、定制输出格式、短代码等等。

由于 Hugo 的可拓展性，我们可以在网上找到很多基于 Hugo 的博客主题，用户可以很简单的对主题进行定制化从而构建出属于自己的博客站点：更改对应配置文件并在 markdown 文件内写好内容后执行 Hugo 命令便能得到网页。我们网站的前端便是在博客主题 [Hextra](https://imfing.github.io/hextra/) 基础上魔改来的。如此一来，我们就能更专注于内容的编写，不需要过多考虑前端样式问题。 ~~（是这样……吗？）~~

生成 `public` 文件夹中的 Hugo 构建产物后，我们便可以将其部署在 CloudFlare Page 上，绑定域名后通过 `hoa.moe` 访问网页了。

## 💪主体 —— GitHub Action

有了 Hugo 作为框架，我们便可以开始填充内容了。为了方便用户，同时避免一个仓库体积过大，我们按课程编号将最早的大仓库拆成了一个个小仓库。因此，我们需要在网页对应的仓库里用一种方式将各个课程仓库中的 `README.md` 内容拿到，移动到网页仓库的 `content` 文件夹下，再生成静态站点，我们所采用的方式便是 GitHub Action。

> GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.
>
> GitHub Actions goes beyond just DevOps and lets you run workflows when other events happen in your repository. For example, you can run a workflow to automatically add the appropriate labels whenever someone creates a new issue in your repository.
>
> GitHub provides Linux, Windows, and macOS virtual machines to run your workflows, or you can host your own self-hosted runners in your own data center or cloud infrastructure.

GitHub Action 会为我们的仓库「分配」一台包含仓库内文件的虚拟机，我们可以在这台虚拟机上运行我们的脚本，执行复杂的任务。正是凭借这一特性，我们做到了诸如：抓取 `README` 文件、获取仓库内文件相关信息、为课程文档进行分类等一系列操作，最终构建出前端网页。

## 👉结尾与下一章

在正式开始进入下一章前，可以先阅读一下这篇文章：[Hugo + GitHub Action，搭建你的博客自动发布系统](https://sspai.com/post/73512)，这篇文章几乎囊括了我们网站搭建过程中的所有步骤，所给出的例子也是网站的最小化实现。

确保你对网站整体有个大概印象，下面让我们具体聊聊网站的前端样式吧：

- [前端架构详解 - 如何修改网站样式](/blog/developer-guide/frontend/)
