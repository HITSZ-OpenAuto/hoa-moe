---
title: (必修)创新训练课B
weight: 27
toc: true
editURL: "https://github.com/HITSZ-OpenAuto/AUTO2003B"
---

<!--
1. 通过 [Shields.io](https://shields.io/) 生成如下的徽章，标注课程的基本信息。
2. 请根据课程的具体内容增删仓库的子文件夹。子文件夹建议使用小写英文，并且添加 README.md。
3. 关于课程的描述可以不止以下几个方面，酌情增删。
4. hoa.moe 生成本课程对应页面后，请将页面链接复制到 GitHub 仓库的 About/Website 中。
5. 可以在 GitHub 页面的 About/Topics 中为课程添加话题名称。
-->

![考查课](https://img.shields.io/badge/%E8%80%83%E6%9F%A5%E8%AF%BE-green)
![学分1](https://img.shields.io/badge/%E5%AD%A6%E5%88%86-1-moccasin)

![成绩构成](https://img.shields.io/badge/%E6%88%90%E7%BB%A9%E6%9E%84%E6%88%90-gold)
![大作业100%](https://img.shields.io/badge/大作业-100%25-wheat)

## 课程介绍（摘自教学大纲）
本课程设计是在学生完成[高级语言程序设计](https://hoa.moe/docs/fresh-autumn/comp2021/)课程学习后进行的。
学生通过本课程的实践，能进一步掌握高级语言程序设计基本概念，掌握基本的程序设计方法；
通过设计一个完整的小型程序，给学生提供独立实践的机会，将课本上的理论知识和实际有机的结合起来，锻炼学生的分析解决实际问题的能力。
提高学生适应实际，实践编程的能力。
初步掌握开发软件所需的需求定义能力、功能分解能力和程序设计能力、代码调试技能；为未来的软件编程及其他课程的学习打下良好的基础。

翻译：
**自己动手制作一个程序**。

选题从课程给出的几个中选择一个，或者提交你自己的选题。

夏季学期结束时需提交开题报告；成果最后在大一立项结题的同时验收，需提交结题报告。

2022 级给出的选题有：
- 学院职工管理信息管理系统
- 学院学生信息管理系统
- 模拟地铁自动售票系统
- 贪吃蛇小游戏
- 跳棋游戏
- 简易三国杀游戏

## 授课教师

- Wu Xiaojun
  - 本课程与教师基本无关。

## 攻略

> by [@Maxwell Jay](https://github.com/MaxwellJay256), 2023.12

这应该是自动化学生为数不多的软件开发的机会。

### 挑选一个开发框架

**课程要求项目必须使用 `C/C++`**。
然而 `C/C++` 本身是没有办法制作 GUI 的，因此我们需要使用第三方库。

现代的桌面应用程序已经几乎不使用 `C/C++` 开发，但是为了降低学习成本，`C/C++` 仍是多数学生的唯一选择。

好在目前有不少基于 `C/C++` 的 GUI 开发框架可供选择，学习起来也不困难。
以下是教学大纲中提到的 4 个。
1. [EasyX](https://docs.easyx.cn/)：一个基于 `GDI+` 的图形库，比较古老了，使用简单，但是功能有限。
2. [Qt](https://www.qt.io/)：跨平台的 GUI 开发框架，功能强大，几乎可以做任何事情。并且你校学生证可以申请到 Qt 的教育许可证，解锁完整特性。
3. [MFC(Microsoft Foundation Classes)](https://learn.microsoft.com/zh-cn/cpp/mfc/mfc-desktop-applications)：一组封装了 C++ 类库的 Windows 编程框架，优点是兼容从 Win95 至今的所有 Windows 操作系统，且运行效率非常高；缺点是开发效率低，并且只能在 Windows 上运行。
4. [C#](https://learn.microsoft.com/dotnet/csharp/)：微软推出的一种面向对象的编程语言，语法类似于 `C/C++`，但是更加简洁，配合 UWP 或 WPF 可以开发出非常现代化的桌面应用程序。

个人推荐前 2 个。

### IDE

由于整个项目将会是一个大型工程，因此可以使用 [Visual Studio](https://visualstudio.microsoft.com) 作为你的 IDE 。
Visual Studio 也是 MFC 或 C# 的最佳选择。

Qt 有自己的 IDE [Qt Creator](https://www.qt.io/product/development-tools)，适合学习和实操 Qt 时使用。

### 选题

图省事的话推荐贪吃蛇，借助 AI 不到 1 天就能速通。

如果想多积累一点敲代码经验，可以选择客户端类型的软件（信息管理系统、售票系统），体验一下前、后端的开发思想，尤其是 GUI 该怎么设计才能中看又中用。
<br>
<br>
<br>


## 资料下载

<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/%E5%88%9B%E6%96%B0%E8%AE%AD%E7%BB%83%E8%AF%BEB%E6%8A%A5%E5%91%8A.docx">course_design/创新训练课B报告.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/%E5%9C%B0%E9%93%81%E7%AB%99%E7%A4%BA%E4%BE%8B/Qt-%E5%88%9B%E6%96%B0%E8%AE%AD%E7%BB%83%E9%A2%98%E7%9B%AE3.zip">course_design/地铁站示例/Qt-创新训练题目3.zip</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/%E5%9C%B0%E9%93%81%E7%AB%99%E7%A4%BA%E4%BE%8B/%E9%A1%B9%E7%9B%AE%E5%B1%95%E7%A4%BA%E7%AD%94%E8%BE%A9.zip">course_design/地铁站示例/项目展示答辩.zip</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/%E5%9C%B0%E9%93%81%E7%AB%99%E7%A4%BA%E4%BE%8B/%E9%BB%84%E7%BB%A7%E5%87%A1-%E5%88%9B%E6%96%B0%E8%AE%AD%E7%BB%83%E8%AF%BEB%E6%8A%A5%E5%91%8A.docx">course_design/地铁站示例/黄继凡-创新训练课B报告.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/slides/%E7%AC%AC1%E7%AB%A0%20%E9%AB%98%E7%BA%A7%E8%AF%AD%E8%A8%80%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1.pdf">slides/第1章 高级语言程序设计.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/slides/%E7%AC%AC2%E7%AB%A0%20%E5%8F%AF%E8%A1%8C%E6%80%A7%E7%A0%94%E7%A9%B6.pdf">slides/第2章 可行性研究.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/slides/%E7%AC%AC3%E7%AB%A0%20%E9%9C%80%E6%B1%82%E5%88%86%E6%9E%90.pdf">slides/第3章 需求分析.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/slides/%E7%AC%AC4%E7%AB%A0%20%E6%80%BB%E4%BD%93%E8%AE%BE%E8%AE%A1.pdf">slides/第4章 总体设计.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/slides/%E7%AC%AC5%E7%AB%A0%20%E8%AF%A6%E7%BB%86%E8%AE%BE%E8%AE%A11.pdf">slides/第5章 详细设计1.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/slides/%E7%AC%AC6%E7%AB%A0%20%E5%AE%9E%E7%8E%B0.pdf">slides/第6章 实现.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/slides/%E7%AC%AC7%E7%AB%A0%20%E7%BB%B4%E6%8A%A4.pdf">slides/第7章 维护.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/slides/%E8%AF%BE%E7%A8%8B%E8%AE%BE%E8%AE%A1%E9%A2%98%E7%9B%AE.pdf">slides/课程设计题目.pdf</a>
<br>
<br>


## 支持我们

如果你喜欢 HITSZ 自动化课程攻略共享计划，想支持我们，以下是几种支持我们的方式:

- HITSZ 自动化课程攻略共享计划 是所有同学都可以参与编写贡献的，如果你有好的笔记或者资料，欢迎前往我们的[GitHub](https://github.com/HITSZ-OpenAuto)进行贡献，也可以发邮件至[📮hi@hoa.moe](mailto:hi@hoa.moe)联系我们，我们会在收到的第一时间进行答复。

- 将本网站分享给你的同学也是支持我们的重要方式。

- 如果您认为本页面提供的信息对您有帮助，请考虑捐赠 ¥2 给我们。每一份慷慨支持都将大幅减轻我们承担的域名及对象存储服务的费用负担。我们鼓励选择“向对方展示我的名字”，你的ID和留言将会显示在我们的[Sponsor](https://hoa.moe/sponsor/)页面中。

<br>
<img src="https://mitcher-1316637614.cos.ap-nanjing.myqcloud.com/hoa/20231112170457.png?imageSlim" alt="Reward_Code" style="zoom:25%; display: block; margin: 0 auto;" />