---
title: LaTeX 环境配置
date: 2024-02-01
authors:
  - name: 吴俊达
    link: https://github.com/oliverwu515
    image: https://github.com/oliverwu515.png
description: 面向每一位想入门 LaTeX 的新人
excludeSearch: false
math: true
---

**[返回 Markdown 文章主页](../basic-of-latex-with-markdown)**

分两部分：编译器和编辑器。

### 编译器配置

需要安装 TeXLive 或 MiKTeX。不要再用 CTeX 套装了。

- TeXLive 的安装稍麻烦些，可看[文章 1](https://www.cnblogs.com/eslzzyl/p/17358405.html)+ [文章 2](https://blog.csdn.net/weixin_44375591/article/details/103953590)（Linux、WSL、Windows 均适用）；或[文章 3](https://zhuanlan.zhihu.com/p/166523064)的前半部分（Windows）。
- MiKTeX 的安装非常简单，可参考[这篇文章](https://blog.csdn.net/DrGuCoding/article/details/123523407)的第 1、2 点。但据说在 Linux 下经常报错（待补充）。
- TeX Live 和 MiKTeX 的区别，详见[一份不太简短的 LaTeX2e 介绍](https://ctan.org/tex-archive/info/lshort/chinese)附录 A 及[LaTeX 配置安装大对比](https://zhuanlan.zhihu.com/p/374491983)。个人建议，Linux 用户使用 TeX Live，Windows 用户使用 MiKTeX。
- Windows 下，安装其中之一后，就会有个纯文本式的编辑器 Texworks，很简洁，但是没有自动补全。

### 编辑器配置

- 使用 TexStudio：
  - Windows：[TeX Live 和 TeXstudio 的下载、安装配置及使用](https://zhuanlan.zhihu.com/p/138586028)，该教程也适用于 MiKTeX 用户。
  - Linux：（待补充）
- 使用 Visual Studio Code：
  - Windows：[Visual Studio Code & TeX Live 配置 LaTeX](https://zhuanlan.zhihu.com/p/166523064)。
  - Linux：[文章 1](https://www.cnblogs.com/eslzzyl/p/17358405.html) （LaTeX Workshop 的 settings.json 文件配置，可结合上一行这篇文章）
  - LaTeX Workshop 扩展的安装文档可参看：[Install · LaTeX-Workshop Wiki](https://github.com/James-Yu/LaTeX-Workshop/wiki/Install)。文档中明确提及''We **strongly recommend** TeX Live''. 上述教程即为基于 TeX Live 的教程。
  - 若利用 MiKTeX，同样可参考上述教程，区别仅在于：在 Windows 系统中，如果编译时用到 latexmk，则需额外安装[Strawberry Perl for Windows](https://strawberryperl.com/)（若不用，则无需理会）。要检验 Perl 是否安装正确，可参考[这篇文章](https://blog.csdn.net/DrGuCoding/article/details/123523407)的第 3 点。Ubuntu 发行版自带 Perl，故无需担心。
- 在 Windows 系统中，使用 WSL 可以加速编译，环境配置可参考：[文章 1](https://www.cnblogs.com/eslzzyl/p/17358405.html)与[在 WSL 中安装 LaTeX](https://zhuanlan.zhihu.com/p/202865739)。关于速度对比的更多信息，可参看：[LaTeX 配置安装大对比](https://zhuanlan.zhihu.com/p/374491983)。
