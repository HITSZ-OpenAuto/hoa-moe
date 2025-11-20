---
title: 你的学生邮箱能薅到哪些羊毛？
description: 自动化本科期间可以用到的免费正版软件清单
date: 2024-01-29T20:15:00+08:00
authors:
  - name: Maxwell Jay
    link: https://github.com/MaxwellJay256
    image: https://github.com/MaxwellJay256.png
  - name: kowyo
    link: https://github.com/kowyo
    image: https://github.com/kowyo.png
draft: false
---

许多工程、科研用的商业软件，尤其是国外的软件，如果购买商用的正版，往往价格不菲。
但是好在许多软件厂商都会提供其产品的免费学生版或教育版，通过学校邮箱即可申请使用。

笔者整理了一些自动化专业学生常用到的、可用学生邮箱申请教育版的免费软件清单（我们亲自测试申请了以下所有许可证）。
也欢迎大家在评论区补充，我会及时更新到正文中。

## 1. 编程相关

### GitHub

**申请链接**：[**以学生身份申请 GitHub Global Campus - GitHub 文档**](https://docs.github.com/zh/education/explore-the-benefits-of-teaching-and-learning-with-github-education/github-global-campus-for-students/apply-to-github-global-campus-as-a-student)

申请 GitHub Global Campus，相当于：

- 将 GitHub 个人账户升级为 PRO
- 获得 [**GitHub Copilot**](https://github.com/features/copilot)
- 获得包含 JetBrains 在内的 [Student Developer Pack](https://education.github.com/pack/offers) 中的权益

> GitHub Copilot 并非唯一的 AI 代码助手，它也有其他免费的替代品，例如 [TabNine](https://www.tabnine.com/)，[Codeium](https://www.codeium.com/) 等。

### JetBrains

**申请链接**：[**免费教育许可证 - JetBrains**](https://www.jetbrains.com/zh-cn/community/education/#students)

JetBrains 是来自捷克的软件开发公司，针对许多编程语言提供了一系列的 IDE，例如面向 `Java` 的 [IntelliJ IDEA](https://www.jetbrains.com/idea/)、面向 `Python` 的 [PyCharm](https://www.jetbrains.com/pycharm/)、面向 `C++` 的 [CLion](https://www.jetbrains.com/clion/) 等。

不巧的是，HIT 位于 JetBrains 的 [stoplist](https://github.com/JetBrains/swot/blob/master/lib/domains/stoplist.txt) 中。
因此在上述申请链接直接使用学生邮箱会申请失败；即使使用 GitHub Student Developer Pack 登录也可能遭到拒绝。

- 解决办法：

1. 使用 GitHub Student Developer Pack 登录遭到拒绝的原因是 JetBrains 发现你的 GitHub 用户中含有「<xxx@stu.hit.edu.cn>」的邮箱。
   因此，你可以临时将学生邮箱从你的 GitHub 账户中移除，再使用 GitHub 申请 JetBrains 教育许可证；等到需要更新你的 GitHub 学生认证时再将学生邮箱添加回去。
2. 使用学信网的学籍证明申请 JetBrains 教育许可证。
   参考[「Jetbrains 学生授权获取指南 - 知乎」](https://zhuanlan.zhihu.com/p/378185042)中的流程。

### Qt

**申请链接**：[**Qt Educational Licenses for Students and Teachers - Qt**](https://www.qt.io/qt-educational-license)

Qt 是一个跨平台的 `C++` GUI 库，可以用于开发桌面应用、嵌入式应用、移动应用等。
Qt 教育许可证可以免费为用户提供 Qt 的商业专业级功能。

## 2. 硬件相关

### Altium Designer

**申请链接**：[**Altium Student Lab - Altium**](https://www.altium.com/education/students)

Altium Designer 是一款电子设计自动化软件，用于电路原理图、PCB、FPGA 设计，由 Altium Ltd. 开发。

### Autodesk

**申请链接**：[**Autodesk 教育和学生访问权限 - Autodesk**](https://www.autodesk.com.cn/education/edu-software)

Autodesk 是一家专业的 CAD 软件公司，旗下的软件包括
[AutoCAD](https://www.autodesk.com.cn/products/autocad),
[3ds Max](https://www.autodesk.com.cn/products/3ds-max),
[Maya](https://www.autodesk.com.cn/products/maya) 等。

Autodesk 的教育访问权限允许用户免费获得其绝大多数软件产品，包括以上 3 项。

## 3. 数据分析

### MATLAB?

2020 年，HIT 被美国禁止使用 [MATLAB](https://www.mathworks.cn/products/matlab.html)。

考虑使用 [GNU Octave](https://www.gnu.org/software/octave/) 作为在公开研究中的替代。
`Python` 也可以胜任 MATLAB 除去 Simulink 之外的大部分工作。

> 也可以前往淘宝购买正版成品账号，价格在 20 元左右，关键词 `MATLAB 正版`。

### Origin

**申请链接**：[**Origin Student Version - OriginLab**](https://www.originlab.com/index.aspx?go=PRODUCTS/OriginStudentVersion)

[Origin](https://www.originlab.com/index.aspx?go=PRODUCTS/Origin) 是来自 [OriginLab](https://www.originlab.com/) 的数据分析和绘图软件，并且拥有 `C++` 和 `Python` API。

### HALCON

MVTec HALCON 是一款综合性的机器视觉标准软件，拥有全球通用的集成开发环境 (HDevelop)。它不仅能够节约成本而且缩短您产品进入市场的时间。HALCON 的灵活架构有利于快速开发任何类型的机器视觉应用。

HALCON 虽然也有针对教育用户推出的免费版本，并不可以用 HIT 的学生邮箱申请，拒绝理由显示所在地区没有该计划。所幸 HALCON 对免费试用的申请并不严格，申请 HALCON 正版试用的方法有：

- 联系中国代理商申请，这也是官方的唯一正规渠道（笔者 Kowyo 亲自尝试，回复很迅速）。
- 这个 [GitHub 仓库](https://github.com/lovelyyoshino/Halcon_licenses) 有每个月更新的 HALCON 试用许可证。
- 淘宝有一家店也售卖相关的许可证，软件从官网下载即可。
