---
title: （必修）自动控制实践 B
weight: 36
toc: true
editURL: "https://github.com/HITSZ-OpenAuto/AUTO3002B/edit/main/README.md"
math: true
---

{{< update-info update_time="2024 年 12 月 20 日" author="psp_dada" message="修改试题命名 (#8)" >}}

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

- 考试难度：较难
- 说明：注意老师给出的重点。同时对于理论部分的学习主要是一些固定的模型，注意公式推导和转换即可。实践部分听重点，过一遍 PPT 即可。

> 文/[xander-2077](https://github.com/xander-2077)

- 主要是大背诵。

> 文/[Oliver Wu](https://github.com/oliverwu515)

## 资料下载

如果你是校内学生，可点击如下「内网网盘」按钮查看本门课程的电子书、课件和实验软件等。

{{< callout type="info" >}}
  注意，内网网盘（[open.osa.moe](https://open.osa.moe/openauto)）由于机房停电不可用，预计 2025 年 1 月 13 日 起可正常使用。
{{< /callout >}}

{{< hoa-filetree/container driveURL="https://open.osa.moe/openauto/AUTO3002B" repoURL="https://github.com/HITSZ-OpenAuto/AUTO3002B" >}}
  {{< hoa-filetree/folder name="assignments" date="" state="closed" >}}
  {{< hoa-filetree/folder name="LL_Version" date="" state="closed" >}}
    {{< hoa-filetree/file name="HW1" type="pdf" size="63.1 KB" date="2024/05/09" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/LL_Version/HW1.pdf" >}}
    {{< hoa-filetree/file name="HW2" type="pdf" size="632.6 KB" date="2024/05/09" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/LL_Version/HW2.pdf" >}}
    {{< hoa-filetree/file name="HW3" type="pdf" size="84.1 KB" date="2024/05/09" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/LL_Version/HW3.pdf" >}}
    {{< hoa-filetree/file name="HW4" type="pdf" size="118.8 KB" date="2024/05/09" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/LL_Version/HW4.pdf" >}}
    {{< hoa-filetree/file name="HW5" type="pdf" size="221.2 KB" date="2024/05/09" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/LL_Version/HW5.pdf" >}}
  {{< /hoa-filetree/folder >}}
  {{< /hoa-filetree/folder >}}
  {{< hoa-filetree/folder name="exams" date="" state="closed" >}}
    {{< hoa-filetree/file name="2021 自控实践 B 试题与答案" type="pdf" size="689.7 KB" date="2024/05/09" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/2021%20%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5B%E8%AF%95%E9%A2%98%E4%B8%8E%E7%AD%94%E6%A1%88.pdf" >}}
    {{< hoa-filetree/file name="2024 自控实践 B 试题回忆版 (V1.0)" type="pdf" size="652.8 KB" date="2024/07/21" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/2024%20%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5B%E8%AF%95%E9%A2%98%E5%9B%9E%E5%BF%86%E7%89%88%28V1.0%29.pdf" >}}
  {{< hoa-filetree/folder name="本部 - 往年题" date="" state="closed" >}}
    {{< hoa-filetree/file name="哈尔滨工业大学 2020 试题" type="jpg" size="5.1 MB" date="2024/05/09" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%9C%AC%E9%83%A8-%E5%BE%80%E5%B9%B4%E9%A2%98/%E5%93%88%E5%B0%94%E6%BB%A8%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A62020%E8%AF%95%E9%A2%98.jpg" >}}
    {{< hoa-filetree/file name="哈尔滨工业大学 2020 试题答案" type="pdf" size="7.7 MB" date="2024/05/09" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%9C%AC%E9%83%A8-%E5%BE%80%E5%B9%B4%E9%A2%98/%E5%93%88%E5%B0%94%E6%BB%A8%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A62020%E8%AF%95%E9%A2%98%E7%AD%94%E6%A1%88.pdf" >}}
  {{< /hoa-filetree/folder >}}
  {{< /hoa-filetree/folder >}}
  {{< hoa-filetree/folder name="labs" date="" state="closed" >}}
    {{< hoa-filetree/file name="2024_wjd_综合-watermark" type="pdf" size="2.4 MB" date="2024/07/21" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/2024_wjd_%E7%BB%BC%E5%90%88-watermark.pdf" >}}
    {{< hoa-filetree/file name="2024_综合实验任务书" type="pdf" size="5.5 MB" date="2024/07/21" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/2024_%E7%BB%BC%E5%90%88%E5%AE%9E%E9%AA%8C%E4%BB%BB%E5%8A%A1%E4%B9%A6.pdf" >}}
    {{< hoa-filetree/file name="综合实验模板（修正）" type="docx" size="1.1 MB" date="2024/07/21" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E7%BB%BC%E5%90%88%E5%AE%9E%E9%AA%8C%E6%A8%A1%E6%9D%BF%EF%BC%88%E4%BF%AE%E6%AD%A3%EF%BC%89.docx" >}}
  {{< hoa-filetree/folder name="ljh_version" date="" state="closed" >}}
    {{< hoa-filetree/file name="综合实验报告模板_18 号机" type="pdf" size="1.7 MB" date="2024/07/04" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/ljh_version/%E7%BB%BC%E5%90%88%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E6%A8%A1%E6%9D%BF_18%E5%8F%B7%E6%9C%BA.pdf" >}}
  {{< /hoa-filetree/folder >}}
  {{< /hoa-filetree/folder >}}
{{< /hoa-filetree/container >}}

## 参与

《HITSZ 自动化课程攻略共享计划》是所有同学都可以参与编写的，如果你有好的笔记或者资料，欢迎前往我们的 [GitHub](https://github.com/HITSZ-OpenAuto) 进行参与，也可以发邮件至 [📮hi@hoa.moe](mailto:hi@hoa.moe) 联系我们，我们会在收到的第一时间进行答复。

{{< callout type="" >}}
  © 版权声明：[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-nc-sa/4.0/)
{{< /callout >}}
