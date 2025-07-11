---
title: （必修）自动控制实践 B
weight: 9
toc: true
editURL: "https://github.com/HITSZ-OpenAuto/AUTO3002B/edit/main/README.md"
math: true
---

{{< update-info update_time="2025 年 6 月 27 日" author="psp_dada" message="上传作业与实验相关内容 (#14)" >}}


<div class="img-div hx-mt-4 hx-flex-row hx-justify-start hx-items-center">

![Static Badge](https://img.shields.io/badge/%E8%80%83%E8%AF%95%E8%AF%BE-red)![Static Badge](https://img.shields.io/badge/%E5%AD%A6%E5%88%86（19~21%E7%BA%A7）-6-moccasin)![Static Badge](https://img.shields.io/badge/%E5%AD%A6%E5%88%86（22%E7%BA%A7）-4-moccasin)

![Static Badge](https://img.shields.io/badge/%E6%88%90%E7%BB%A9%E6%9E%84%E6%88%90（21%E7%BA%A7）-gold)
![Static Badge](https://img.shields.io/badge/%E4%BD%9C%E4%B8%9A-10%25-wheat)
![Static Badge](https://img.shields.io/badge/%E5%AE%9E%E9%AA%8C-40%25-wheat)
![Static Badge](https://img.shields.io/badge/%E6%9C%9F%E6%9C%AB%E8%80%83%E8%AF%95-50%25-wheat)

![Static Badge](https://img.shields.io/badge/%E5%AD%A6%E6%97%B6%E5%AE%89%E6%8E%92（22%E7%BA%A7）-gold)
![Static Badge](https://img.shields.io/badge/%E6%80%BB%E5%AD%A6%E6%97%B6-64-wheat)
![Static Badge](https://img.shields.io/badge/%E6%8E%88%E8%AF%BE-48-wheat)
![Static Badge](https://img.shields.io/badge/%E5%AE%9E%E9%AA%8C-16-wheat)

</div>

自 22 级开始，本课程原有的 STM32 理论部分和基础实验、调速实验部分均被纳入大三上的拓展选修课[《嵌入式系统》](https://hoa.moe/docs/junior-autumn/auto3024/)中。有关资料也已经转移，请移步查看。综合实验报告仍予保留。

注意，该课程为哈工大本部/深圳的考研复试课程。

## 教材及参考书

- 王广雄、何朕，控制系统设计，清华大学出版社。

## 授课教师

- 理论课：董广忠
  - 授课风格：通过加入密度极高的无意义衬词以及含糊其辞的表述，成功达到让人听不懂的效果。答疑态度十分一般。
  - 听课建议：不考勤。上课会提示重点，建议课后倍速听回放。课件在教师主页，不在 qq 群发放。

> 文/[Oliver Wu](https://github.com/oliverwu515)

- 实验课：王彬彬、刘瑞
  - 如遇到问题，建议自行 Google。

## 关于考试

> 文 / [xander-2077](https://github.com/xander-2077)

- 考试难度：较难
- 说明：注意老师给出的重点。同时对于理论部分的学习主要是一些固定的模型，注意公式推导和转换即可。实践部分听重点，过一遍 PPT 即可。

> 文 / [Oliver Wu](https://github.com/oliverwu515)

- 主要是大背诵。

> 文 / [psp_dada](https://github.com/pspdada), 2025.6

从回忆卷子就可以看出，25 年的考试如往常一样的大背诵，我考试时不到一个小时手就写酸了。不过虽然老师上课的时候讲了很多次题目会完全重新出，但是实际上（除了那一道 Anti Windup 简答题）大部分题目还都是原题，甚至最后一道设计大题完完全全没有变化，因此只要把往年题都做做好，考试的时候就不会有太大问题。

虽然听大家多会抱怨这门课，我个人觉得这门课在逻辑性和知识点密度上还是很不错的（相比自控实践 A 好了不是一点半点），大部分问题估计就是学生和老师之间沟通不够及时，很多问题没法有效解决，因此我写了往年题目的详解并放在 exams 文件夹下，供大家参考，大家做题时可以多和同学们交流，大部分情况都只能将大多数人认同的答案作为参考。

## 资料下载

如果你是校内学生，可点击如下「内网网盘」按钮查看本门课程的电子书、课件和实验软件等。

{{< hoa-filetree/container driveURL="https://open.osa.moe/openauto/AUTO3002B" repoURL="https://github.com/HITSZ-OpenAuto/AUTO3002B" >}}
{{< /hoa-filetree/container >}}

## 参与

HOA Core 成员有意重构 hoa 的网站，以接入更多的专业，实现更好的体验。如果你对资料分享或者网站搭建感兴趣，即使来自其他专业，非常欢迎你[联系](mailto:hi@hoa.moe)/加入我们 Core 团队。这里有我们[初步的重构计划](https://historical-mousepad-286.notion.site/HOA-1f71751ad5fe80978c70d9e32330d7e6)。

同时，HOA Core 初代成员已经毕业，如果你想加入 HOA Core，请阅读我们的博客了解更多：[《HOA 的未来，需要你一起来书写》](https://hoa.moe/news/future-of-hoa)。

{{< callout type="" >}}
  © 版权声明：[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-nc-sa/4.0/)
{{< /callout >}}

