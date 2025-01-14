---
title: （必修）微积分 B
weight: 22
toc: true
editURL: "https://github.com/HITSZ-OpenAuto/MATH1015B/edit/main/README.md"
math: true
---

{{< update-info update_time="2025 年 1 月 4 日" author="W·D·Gaster" message="补充严志彬老师的内容" >}}

<!--
1. 通过 [Shields.io](https://shields.io/) 生成如下的徽章，标注课程的基本信息。
2. 请根据课程的具体内容增删仓库的子文件夹。子文件夹建议使用小写英文，并且添加 README.md。
3. 关于课程的描述可以不止以下几个方面，酌情增删。
4. hoa.moe 生成本课程对应页面后，请将页面链接复制到 GitHub 仓库的 About/Website 中。
5. 可以在 GitHub 页面的 About/Topics 中为课程添加话题名称。
-->

<div class="img-div hx-mt-4 hx-flex-row hx-justify-start hx-items-center">

![%E8%80%83%E8%AF%95%E8%AF%BE](https://img.shields.io/badge/%E8%80%83%E8%AF%95%E8%AF%BE-red)
![%E5%AD%A6%E5%88%86](https://img.shields.io/badge/%E5%AD%A6%E5%88%86-5-moccasin)

![%E6%88%90%E7%BB%A9%E6%9E%84%E6%88%90](https://img.shields.io/badge/%E6%88%90%E7%BB%A9%E6%9E%84%E6%88%90-gold)
![%E4%BD%9C%E4%B8%9A20%](https://img.shields.io/badge/%E4%BD%9C%E4%B8%9A-20%25-wheat)
![%E6%9C%9F%E4%B8%AD%E8%80%83%E8%AF%9530%](https://img.shields.io/badge/%E6%9C%9F%E6%9C%AB%E8%80%83%E8%AF%95-30%25-wheat)
![%E6%9C%9F%E6%9C%AB%E8%80%83%E8%AF%9550%](https://img.shields.io/badge/%E6%9C%9F%E6%9C%AB%E8%80%83%E8%AF%95-50%25-wheat)

</div>

## 授课教师
- 包革军
  - 授课风格：完全不用幻灯片，纯板书，而且板书非常有条理，把他的板书全部抄下来就是一份可读性很好的笔记了（这一点比 yjw 好）。偶尔会点名。
  有学生觉得他讲得太慢，但事实上这位老先生总能在最后一刻讲完所有要讲的东西。
  唯二的问题是板书时常出现笔误、总是拖堂。
    > “当他在期末最后一节课上向到场的所有学生鞠躬致谢时，我便知道他是我在大一遇到的最有哈工大人气质的教授。” -[@Maxwell Jay](https://github.com/MaxwellJay256)
    >
    > 这两个问题出在这个老师身上我觉得都不是问题了，这并不影响他讲课的连贯性和逻辑性。如果出现笔误可以在课堂上尽早指出来，就不会耗费太多时间。-[@psp_dada](https://github.com/pspdada) 2024.7.18
  - 是否需要认真听讲做笔记：如果你愿意听他的课，最好就完全跟着他的思路来。老师会在课上讲很多的例题，如果能把它们都记下来并且课后稍微复习一下，基本上就足够掌握这一部分的内容了（都把例题喂到你嘴里了这还不冲？）。
  - 听课建议：如果你是挑剔的学生，大多数课都不愿意听老师讲，那么他的课应该是你最后一个选择 skip 的。

- 余君武
  - 授课风格：
    - 板书为主，幻灯片为辅（更像他的讲义），首先板书细致讲本节课内容和重点，再~~照本宣科~~念一遍 ppt，还会逐题板书讲幻灯片例题
    - 偶尔吹水，但内容也与课程有关，基本是以生动的例子来类比定理，给你直觉上的理解
    - 每章讲完后会上一节习题课，其中有相当一部分就是黄本原题
    - 讲课非常有活力，有时讲兴奋了还会「指指点点」，气氛拉满
    - 可能因为例题还没讲完而拖堂
  - 听课建议：
     - 老师上课时会补充不少 经典例题、方法、技巧 等，非常值得记下来；此外，他还会解释常见的 错误理解、难点 等，帮助你理解概念——这正是自学容易忽略的地方
     - （于 2024.4.15 更新）~~老师不考勤~~ 学到二重积分时，老师会开始考勤。当然这不是一件坏事——后面的东西，正如余老师、OpenAuto 的学长所言，难度很大，自学更是不一定学得懂
     - 可以参考本部的《工科数学分析学习指导与习题解答》，他的讲解和这本书有一些重合部分
  - 课后：
    - 所有上课的课件都会发群里（甚至可以直接提醒他发），也会时不时分享一些技巧、黄本题目答案之类
    - 不懂可以直接问，非常负责任

  > 文/[IcyDesert](https://github.com/IcyDesert), 2024.3

- 严志彬
  - 授课风格：纯板书，板书风格比较潦草，随心而动。板书和课本并不完全一致（主要是顺序上的）。
  - 听课建议：
    - 建议听课，老师上课很有活力，而且逻辑特别清晰。
    - 由于严老师常年教学数学系，思维和工科数学的思维有很多的不同，偏重数学定理的证明。但是你认真听他的课一定会受益良多，在数学思维上有很大的提升。
    - 严老师的习题课并不局限于习题本身，而是跳出习题从更高的思维角度解读题目，对微积分的理解能让你超越课本的。
  > 文/[Gaster](https://github.com/WDGaster), 2025.1
  
## 关于考试
- 考试难度：半期考试比较容易，25+ 对于大多数同学是能实现的；期末考试由于曲线曲面积分以及级数的加入，计算量陡增，难度也随之增加，想上 40 分会比较有挑战性，挂科率也是相当高。
- 但 2024 春的期末考试并没有特别难，曲面积分和级数的计算量相对于作业题都不大；可能是三个校区第一年统一考试，不想太为难学生？还是不要掉以轻心为好。
> 文/[IcyDesert](https://github.com/IcyDesert), 2024.7


## 学习建议
看了上面关于两位老师的评价我觉得特别合适，他们都是非常认真负责的老师，都是可以信赖可以跟着走完一整门课的老师。

由于 微积分 B 和 微积分 A 的学习是一脉贯通的，因此可以移步 [微积分 A](https://hoa.moe/docs/fresh-autumn/math1015a/) 仓库观看详细的学习指导

> 文/[psp_dada](https://github.com/pspdada) 2024.7.18

## 资料下载

如果你是校内学生，可点击如下「内网网盘」按钮查看本门课程的电子书、课件和实验软件等。

{{< callout type="info" >}}
  注意，内网网盘（[open.osa.moe](https://open.osa.moe/openauto)）由于机房停电不可用，预计 2025 年 1 月 13 日 起可正常使用。
{{< /callout >}}

{{< hoa-filetree/container driveURL="https://open.osa.moe/openauto/MATH1015B" repoURL="https://github.com/HITSZ-OpenAuto/MATH1015B" >}}
{{< /hoa-filetree/container >}}

## 参与

《HITSZ 自动化课程攻略共享计划》是所有同学都可以参与编写的，如果你有好的笔记或者资料，欢迎前往我们的 [GitHub](https://github.com/HITSZ-OpenAuto) 进行参与，也可以发邮件至 [📮hi@hoa.moe](mailto:hi@hoa.moe) 联系我们，我们会在收到的第一时间进行答复。

{{< callout type="" >}}
  © 版权声明：[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-nc-sa/4.0/)
{{< /callout >}}
