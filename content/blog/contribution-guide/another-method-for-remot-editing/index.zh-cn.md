---
title: 远程编辑 hoa.moe 的方法补充
date: 2025-03-03
description: 更加简单的远程操作
authors:
  - name: 潜伏
    link: https://github.com/capoo-fan
    image: https://github.com/capoo-fan.png
excludeSearch: false
---



#  前言
对于 Github 的其他仓库,本身体积不大,可以直接 clone 到本地进行编辑并且推送上去,但是 hoa.moe 的仓库体积比较大,如果直接 clone 到本地,不仅需要花费大量的时间,而且还需要大量的磁盘空间,所以我们需要一种更加简单的方法来编辑 hoa.moe 的仓库

前面已经介绍了一种 codespaces 的方法,这里有一种依赖一个插件,直接在 VSCode 上编辑的方法,此方法打开 hoa.moe 的速度大概在三四秒左右(魔法状态下), 然后可以直接编辑,编辑完成后直接 push 到远程仓库,不需要任何其他操作,非常方便

# 操作流程

1. 将仓库 fork 到自己的 Github 账号下

2. 下载 GitHub Repositories 插件

![](./img/github-Repositories.png)

3. 打开 GitHub Repositories 插件,并登录自己的帐号,打开对应的仓库
   
![](./img/teach.png)  

虽然 Markdown-Preview-Enhanced 插件在远程仓库中无法使用,但是此时只需要 CTRL+SHIFT+V 打开 VSCode 内置的 Markdown 预览即可,所以不需要担心预览的问题

4. 编辑完成后,就可以在 VSCode 上进行 push ,然后就可以回到 Github 帐号下进行 pr 了
   

# 总结

这个方法是笔者在读 [VSCode官方文档](https://code.visualstudio.com/docs) 时发现出来的方法,很简便且易于操作,在这里分享给大家.同时也推荐大家多读官方文档或者Github 原作者的 REAMED.md ,往往会有意想不到的收获!