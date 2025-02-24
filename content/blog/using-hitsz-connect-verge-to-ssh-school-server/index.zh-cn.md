---
title: 如何通过 HITSZ Connect Verge 在校外优雅地访问校园服务器
description: 笔者探索这套方案的过程并不优雅
date: 2025-02-23T19:12:00+08:00
authors: 
    - name: Kowyo
      link: https://github.com/kowyo
      image: https://github.com/kowyo.png
draft: false
---

作为大四要参加毕业设计的学生，必不可少会接触到使用校内服务器进行深度学习训练的场景，本篇文章讲介绍如何在校外访问校园服务器。

## 注册账号

集群的网址是 http://hpc.hitsz.edu.cn/

需要校园网环境才可以访问，如果你位于校外，可以使用笔者开发的工具 [HITSZ Connect Verge](https://github.com/kowyo/hitsz-connect-verge) （EasyConnect 的优雅替代方案[^1]）连接到校园网。

初次登陆，你需要先加入到项目当中，你需要访问[哈工大大型仪器开放共享系统](https://17.hit.edu.cn/)，在`仪器查询` -> `GPU集群(注意是郑海刚老师)`选择`自主上机`和预约。如果你有其他疑问，加入 [QQ 群聊（936399193）](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=4DV_-meRzJ-PbIFMOJ0lcsDN_M8bYr-c&authKey=yuaZaGedkrFGH0G8ZTLlFCYckFpu509iSGD5aQU6PZ%2BXVBsRLCXpQ2G5TzhjHZXa&noverify=0&group_code=936399193) 问问老师和其他同学吧。一般要等待至周五老师才会审核。

## 申请资源

这部分属于基本操作，请参考[平台文档](http://hpc.hitsz.edu.cn/docs/zh/home)。

需要注意的是，免费额度只有 20000 点，不使用的时候请释放资源以防止造成点数浪费，如果点数不足可以充值，具体方法请在 QQ 群咨询老师（因为笔者也不会）。

## 通过 SSH 连接服务器

服务器提供远程桌面和 SSH 两种访问方式。

笔者选择通过 SSH 连接服务器，好处是可以使用自己电脑上的 VS Code 或者其他编辑器，并且配合 AI 写代码也方便很多。下面面向不同平台的用户介绍如何使用 HITSZ Connect Verge[^2] 进行服务器访问，如果你是校内学生（已经连接至校园网），可以不使用 HITSZ Connect Verge 代理和 ProxyCommand 参数，直接使用 SSH 连接。

我们的核心思路是：让电脑通过 HITSZ Connect Verge 的 SOCKS5 代理访问服务器。HITSZ Connect Verge 连接后，配置终端或者 VS Code Remote Server 访问连接服务器。[^3]

### Windows

最开始使用的是老牌软件 PuTTY，但是终端界面十分古老，因此很快就放弃。

首先，需要开启 OpenSSH，可以参考[这篇文章](https://blog.csdn.net/2301_77554343/article/details/134328867)。

为了使用代理需要下载 [Nmap](https://nmap.org/download.html)。

之后，在资源管理器 -> `%userprofile%` 路径下，创建 `.ssh` 文件夹，创建 `config`文件，添加如下信息：

```config
Host <ip 地址>
    HostName <ip 地址>
    ProxyCommand ncat --proxy 127.0.0.1:1080 --proxy-type socks5 %h %p
    User <u+学号，如 u2103xxxxx>
    Port <端口>
```

其中的 `ncat` 命令使用了我们下载的 Nmap 中的 ncat.exe，1080 是 HITSZ Connect Verge 中设置的 SOCKS 5 端口，如果产生冲突，可以自定义为其他端口。

完成之后，打开 VS Code，点击左下角的图标即可通过 SSH 连接至服务器。

## macOS/Linux

macOS 和 Linux 就轻松不少了。

可以直接在终端使用

```bash
ssh -o ProxyCommand="nc -X 5 -x 127.0.0.1:1080 %h %p" <用户名>@<服务器地址> -p <端口>
```

或者在 .ssh/config 中，加入类似 Windows 的配置

```config
Host <ip 地址>
  HostName <ip 地址>
  ProxyCommand nc -X 5 -x 127.0.0.1:1080 %h %p
  User <u+学号，如 u2103xxxxx>
  Port <端口>
```

完成之后即可通过 VS Code Remote Server 访问。

## 一些注意事项

- 服务器密码需要在 hpc.hitsz.edu.cn 点击个人头像 -> 重置密码进行修改。
- 如果所有配置完成后登录时出现报错 “Permission denied, please try again.”，可能不是你的问题，申请其他类型的实例或者到群里问问老师。

## 写在最后

读到这里的你学会了吗？有什么不懂或者需要补充的地方欢迎在评论区下方留言。希望通过这篇博客能让更多同学学会如何优雅地访问校园服务器。

[^1]: 关于笔者为什么不使用 EasyConnect，推荐观看视频：[转发给你的同学看看 如何应对与卸载删除它？有什么替代方案？](https://www.bilibili.com/video/BV163411Z7BD)。
[^2]: 同校另一位同学开发的软件 [EZ4Connect](https://github.com/PageChen04/EZ4Connect) 也支持类似功能，但是笔者尚未亲自测试。
