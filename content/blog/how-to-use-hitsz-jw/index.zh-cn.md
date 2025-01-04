---
title: 关于教务的两三事
description: 更适合自动化学子的教务使用教程
date: 2025-01-04
authors:
  - name: YinMo19
    link: https://github.com/YinMo19
    image: https://github.com/YinMo19.png
excludeSearch: false
math: true
tags:
  - 计算机
  - 信息查询
  - （简单的）逆向工程
---

本文是关于教务使用的一篇小教程，刚好笔者前阶段对教务也算深有感触，遂写此篇。

教务承担了课程选课、成绩查询等任务，自然在学期前与学期终迎来大量的流量。然而恕我直言，教务系统本身的编写并不优秀。如果你对 web 与逆向工程稍有了解，那么你肯定在教务卡死的时候尝试一些方法——最后你会发现，这一定是一个外包项目，因为源代码中甚至还有“购物车”这样的字眼。
![GouWuChe.doge](images/jw_GouWuChe.png)
然而差归差，我们必须捏着鼻子用它，因此更多技术相关内容下文表述，这里我先介绍一些实用的功能。

首先关于教务系统有一点不得不提的是，它甚至连返回都没做好，请你不要在页面左上角使用浏览器提供的返回上一级按钮，不然你会直接回到认证系统。关于认证系统的信息在文末提供。

## 查看课程信息

首页的
![score1](images/score_1.png)
有个主修计划查询，选择大类，点击查询
![dl](images/dl.png)
即可查询大类方案
![method](images/method.png)
可以看到课程是考试课还是考察课。另外还可以查看学分要求，确定要选的课程。
![scoreneed](images/scoreneed.png)

## 查看成绩信息

事实上很多人并不知道，教务有两个成绩信息的接口。
![score1](images/score_1.png)
![score2](images/score_2.png)
业务查询中的个人成绩查询和成绩类业务中的个人成绩查询在大部分内容中都是一致的，不过成绩类的信息更加齐全。进入后者，可以直接看到一些关于个人学分绩相关的 tag，一目了然。下面的表格内容则是课程的考试成绩信息。大概是这样的。关于详情内的信息大概如图。
![score_in](images/score_in.png)
![score_detail](images/score_detail.png)
可以发现，里面有关于排名的信息。然而如果没有进行评教的话大概是看不到相关信息的，因此还是尽早评教为好。评教相关这里按下不表，一学期花个 10 分钟就能解决。

虽然部分课程没有详细信息，但是其实只是没有在网站前端显示而已。打开浏览器 f12 控制台，刷新一次页面之后可以发现一个名为 `grcjcx` 的请求，并不显然地这个接口实际上是个人成绩查询的拼音缩写。查看返回的 json 数据
![person score](images/grcjcx.png)
可以发现，字段 `pm` （排名）直接可以看到，尽管并没有详情信息的按钮可以按。

还有一些关于查看未公布（但是已经录入）的成绩的奇技淫巧——也算是教务的 bug。
![score2](images/score_2.png)
在这里有一个成绩类申请的链接，点击进去之后可以发现
![score_resure](images/score_resure.png)
成绩复核的按钮。选择对应内容的可申请成绩，直接申请就能看到已经录入但是还没公布的成绩了。记得看完取消申请。
![resure](images/resure.png)

> 截止目前这个 bug 还在，不保证长期存在。

### 其余相关的可提前查看信息

相似操作可以查看*考试时间*，直接在成绩类申请的缓考页面中就能找到。（不过这个可能不是最终时间，有几率改动）

### 学习进度

进入主页面中 业务查询/个人成绩查询，可以选择学习进度查看目前的已修学分、排名。需要关注的是下一栏的学分类别要求。有一些课程需要修够特定数量的学分 (例如 23 届要求跨专业需要修满 10 学分)，就可以在这里查看目前已修的学分数量。
![need](images/need.png)
建议在选课前提前查看安排接下来的任务。更加详细的选课推荐请前往 hoa 正文查看对应内容。

## 关于选课

选课的入口在
![choose](images/choose.png)
进入之后可以直接选课。关于选什么课、什么课推荐请移步 hoa 正文部分，这里可能更偏重教务本身相关。一个比较有用的小 tip 是
![span](images/span.png)
右上角的小按钮展开之后可以选择忽略 0 余量课程与忽略冲突课程。否则你可能看到大量你选不了的课程（在跨专业中）。另外点入课程中可以看到一些课程相关的信息，这对于你是否选课很关键。有些课程有 70% 的考试，而有些课程只需要写论文。这些信息都可以在
![list](images/list.png)
点入的课程大纲中查看。

### 选课细节

> tips: 本节技术相关，对新手可能不友好。接下来的内容有关逆向工程（web 注入），请时刻谨记网络安全法。
>
> 本篇往下内容仅供学习参考，切勿用于非法用途。笔者不对仿造本文对任何尝试负责。

教务选课的 api 名称叫做 `addGouWuChe`，也就是 `添加购物车`。这点已经懒得喷了，不过更有意思的是，教务似乎并没有对选课进行鉴权，你可以直接直选上体育课、选上别专业的课程 etc.
![connot](images/choose_connot.png)
在不能选课的期间选课按钮是不能按的，但是右键点击检查
![disable](images/disable.png)
发现这个按钮实际上只是一个 `disable`，右键编辑为 html 删掉 `disable`属性
![able](images/able.png)
我们就可以按这个按钮了。当然了，教务还是对不在选课时间内做了检验的，你不需要担心选上不该选的课程。
![choosing](images/choosing.png)
但是刚才的请求也是切切实实的发出去了。因此在网络这一栏可以看到这个名为`addGouWuChe`的请求。整个请求体中有大量无效信息，这是因为教务的所有请求共用了一套表单，这也是教务奇卡无比的原因——做了大量无用的操作。我们看看其中有效的内容。一个必须的字段是`xktjz`，意思不明，该键值必须为`rwtjzyx`，意义不明。`xn/xq` 等等表示学年/学期比较好理解，而 `p_id`则是这个课程的唯一标识号。获取这个课程的标识号可以通过查看刚进入课程选课获取的表单
![id](images/id.png)
获取。而剩余最重要的是一个名为 `p_xkfsdm` 的键值对。经过猜测可以发现，原来意思是选课方式代码。经过长时间的测试发现

```
sx-b-b     -> 跨专业课程体系
xx-b-b     -> 限选
bx-b-b     -> 必修
fankzy-b-b -> 方案内跨专业
```

因此之前所说选别的学院的课程和直选体育课实际上就是这个字段。教务并没有对这个字段的严格检查，也就是你只需要找到特定体育课的 id，然后使用直选课程的请求体，更换为该体育课程的 id 就能直选上。当然我并不推荐你这么做——这可能有点危险，无论如何教务最后还是会做一些人工的检查。这里给一些我之前尝试的案例供参考（最后都退掉了
![pe](images/pe.png)
![by](images/by.png)

> p1 是直选体育课，p2 是选上了建筑学院的毕业设计。建筑学院的毕业设计是我跨专业课程中对外人数为 0 的课程，替换为直选的键值对可以直接被判定为建筑学院的学生然后选上这门课。
>
> 另外学校选课的极限频率大概在 2s/次，超过这个频率会显示请求过于频繁，不过不会被封禁，无需担心。
>
> 最后，我写了一个选课加速器：[hit course](https://github.com/YinMo19/hit_course)。_用上了别忘了点个星星_。

## 更多技术相关

> tips: 接下来的内容有关逆向工程，请时刻谨记网络安全法。

教务的网站实际上有两个端点，分别是校内访问和校外访问。我们日常使用的 web 端是校内访问的，而手机 app 是校外访问的。他们的端点分别在

```
http://jw.hitsz.edu.cn/
https://mjw.hitsz.edu.cn/
```

可以查询 dns 发现，

```sh
> q mjw.hitsz.edu.cn
mjw.hitsz.edu.cn. 5m A 219.223.236.18
mjw.hitsz.edu.cn. 5m AAAA 2001:250:3c0f:4003:dbdf:ec12::
```

访问 mjw 会发现指向一个反向代理，该代理做了均衡负载，因此实际上在测试中手机端的性能反而比 web 要好一些。并且可以发现，实际上内网中走的是 http，而校外有 https 保护（并且内网的教务甚至明文传输密码），因此从性能和安全考虑我都更推荐使用手机端访问。

如果你想看看教务具体发了什么包，你可以直接在 web 看 f12，你会很惊喜的发现大量的包均为拼音命名、大量毫无意义的信息，get 方法和 post 方法共用同一套表单 etc. 经过测试，走 mjw 路线的 api 可能不是同一套，当然 mobile 版本的教务系统安全防护依然很低，你很轻松就能抓到包，除了 https 以外没有任何的网络防护（例如双端证书校验/ssl pinning etc.），参考各种 https 的 mitm 方法即可。
![mjw](images/mjw.png)

想要直接给教务发包，可以通过两种手段，一是复用浏览器获取的 cookie，二是通过账号密码登录。复用 cookie 又分两种方式，直接在浏览器重发请求/复制浏览器请求 cURL 在本地更改重发，以及复用 cookie 自行实现请求客户端。两种方法都比较简单，这里按下不表。

使用账号密码需要明确登陆流程。校内 web 端截止本文落笔使用一校三区的 sso 登陆。

> 什么是 sso？
> 单点登录（Single Sign-On, SSO）是一种身份验证机制，允许用户通过一次登录就可以访问多个相关但独立的系统，而不需要重复输入用户名和密码。SSO 的主要目的是简化用户体验并提高安全性。
> ![sso](images/sso.png)
> 简单来说，cookie 实际上是通过 sso 服务器获取的，之后与教务系统共享。因此在抢课高峰期被挤出事实上并非 sso 服务器失效，而是教务对 cookie 的验证超时导致的“session 已失效”假象。

对 sso 有了解之后我们就可以完成登陆。我们使用账号密码往 sso 站点请求登陆，持久化所获取的 cookie 再请求教务的 api 即可。笔者使用 `rust` 编写了简单的 demo 对操作进行展示。

```rs
use reqwest::redirect::Policy;
use reqwest::Client;
use scraper::{Html, Selector};
use serde_json::Value;
use std::collections::HashMap;
use std::error::Error;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // new client, with cookie store
    let client = Client::builder()
        .redirect(Policy::limited(5))
        .cookie_store(true)
        .build()
        .unwrap();

    let response = client
        .get("https://ids.hit.edu.cn/authserver/combinedLogin.do?type=IDSUnion&appId=ff2dfca3a2a2448e9026a8c6e38fa52b&success=http%3A%2F%2Fjw.hitsz.edu.cn%2FcasLogin")
        .send()
        .await?
        .text()
        .await?;

    let document = Html::parse_document(&response);
    let input_selector = Selector::parse("form#authZForm input[type=hidden]").unwrap();

    let mut form_data = HashMap::new();

    // username and password provide.
    form_data.insert("username", username); // username
    form_data.insert("password", password); // password

    for input in document.select(&input_selector) {
        if let Some(name) = input.value().attr("name") {
            if let Some(value) = input.value().attr("value") {
                form_data.insert(name, value.to_string());
            }
        }
    }

    let response = client
        .post("https://sso.hitsz.edu.cn:7002/cas/oauth2.0/authorize")
        .form(&form_data)
        .send()
        .await?;

    // 这一步结束之后拿到 cookie 就可以请求教务对应接口了
    // 接下来可以进行各种操作...
}
```

接下来的操作自然是根据需求完成，直接访问接口即可。使用者可能需要有扎实的拼音功底来辨认完全不是人看的 api。

最后，sso 对登陆次数进行限制。如果你频繁的登陆可能会被封禁。大概频率极限在 10 次/分钟。如果请求太多你可能会收到的短信/email：
![ban](images/ban.png)

> 文/ [YinMo19](https://github.com/YinMo19)，关于相关内容可以通过 `Me@YinMo19.top` 联系我。不过我看邮件有点佛系......
