---
title: 新版校园网登录界面如何登录到服务器
description: instructed by 圈圈四 from HITSZ 开源技术协会
date: 2025-5-31
authors:
  - name: XII
    link: https://github.com/IAMXII
    image: https://github.com/IAMXII.png
excludeSearch: false
---

## ssh 连接到服务器

```shell
ssh -D 端口号（随便） username@ip
eg: ssh -D 1337 aha@10.249.250.240
```

## 找一个可以自己配置代理的浏览器

打开浏览器设置的 Proxy 面板（这里以 Firefox 为例）：

<img src="./assets/image-20250530195546174.png" alt="image-20250530195546174" style="zoom:30%;" />

将端口号改成和刚才连接的端口号一样，保存设置重启浏览器，输入10.248.98.2，进行登录就可以了。

{{% steps %}}

### ssh 连接到服务器

```shell
ssh -D 端口号（随便） username@ip
eg: ssh -D 1337 aha@10.249.250.240
```

### 找一个可以自己配置代理的浏览器

打开浏览器设置的 Proxy 面板（这里以 Firefox 为例）：

<img src="./assets/image-20250530195546174.png" alt="image-20250530195546174" style="zoom:30%;" />

将端口号改成和刚才连接的端口号一样，保存设置重启浏览器，输入10.248.98.2，进行登录就可以了。

{{% /steps %}}