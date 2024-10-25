---
title: （必修）自动控制实践B
weight: 39
toc: true
editURL: "https://github.com/HITSZ-OpenAuto/AUTO3002B/edit/main/README.md"
math: true
---
{{< update-info update_time="2024.7.21" author="吴俊达" message="更新README，更新实验报告版本，更新2024考试题 (#4)" >}}

<div class="img-div hx-mt-4 hx-flex-row hx-justify-start hx-items-center">

![Static Badge](https://img.shields.io/badge/%E8%80%83%E8%AF%95%E8%AF%BE-red)![Static Badge](https://img.shields.io/badge/%E5%AD%A6%E5%88%86（19~21级）-6-moccasin)![Static Badge](https://img.shields.io/badge/%E5%AD%A6%E5%88%86（22级）-4-moccasin)

![Static Badge](https://img.shields.io/badge/%E6%88%90%E7%BB%A9%E6%9E%84%E6%88%90（21级）-gold)
![Static Badge](https://img.shields.io/badge/作业-10%25-wheat)
![Static Badge](https://img.shields.io/badge/实验-40%25-wheat)
![Static Badge](https://img.shields.io/badge/%E6%9C%9F%E6%9C%AB%E8%80%83%E8%AF%95-50%25-wheat)

![Static Badge](https://img.shields.io/badge/学时安排（22级）-gold)
![Static Badge](https://img.shields.io/badge/总学时-64-wheat)
![Static Badge](https://img.shields.io/badge/授课-48-wheat)
![Static Badge](https://img.shields.io/badge/实验-16-wheat)


</div>

自22级开始，本课程原有的STM32理论部分和基础实验、调速实验部分均被纳入大三上的拓展选修课[《嵌入式系统》](https://hoa.moe/docs/junior-spring/auto3024/)中。有关资料也已经转移，请移步查看。综合实验报告仍予保留。

## 教材及参考书

- 王广雄、何朕，控制系统设计，清华大学出版社。

## 授课教师

- 理论课: 董广忠
  - 授课风格：通过加入密度极高的无意义衬词以及含糊其辞的表述，成功达到让人听不懂的效果。
  - 听课建议：不考勤。上课会提示重点，建议课后倍速听回放。课件在教师主页，不在qq群发放。
    
> 文/[Oliver Wu](https://github.com/oliverwu515)
  
- 实验课：王彬彬、刘瑞

## 关于考试

- 考试难度：较难
- 说明：注意老师给出的重点。同时对于理论部分的学习主要是一些固定的模型，注意公式推导和转换即可。实践部分听重点，过一遍PPT即可。

> 文/[xander-2077](https://github.com/xander-2077)

- 主要是大背诵。

> 文/[Oliver Wu](https://github.com/oliverwu515)

## 资料下载

{{< filetree/container >}}
  {{< filetree/folder name="assignments" state="closed" >}}
  {{< filetree/folder name="LL_Version" state="closed" >}}
    {{< filetree/file name="HW1.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/LL_Version/HW1.pdf" >}}
    {{< filetree/file name="HW2.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/LL_Version/HW2.pdf" >}}
    {{< filetree/file name="HW3.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/LL_Version/HW3.pdf" >}}
    {{< filetree/file name="HW4.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/LL_Version/HW4.pdf" >}}
    {{< filetree/file name="HW5.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/LL_Version/HW5.pdf" >}}
  {{< /filetree/folder >}}
  {{< /filetree/folder >}}
  {{< filetree/folder name="exams" state="closed" >}}
    {{< filetree/file name="2024 自动控制实践B试题回忆版(V1.0).pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/2024%20%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5B%E8%AF%95%E9%A2%98%E5%9B%9E%E5%BF%86%E7%89%88%28V1.0%29.pdf" >}}
    {{< filetree/file name="《黄瑞宁漏出》.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E3%80%8A%E9%BB%84%E7%91%9E%E5%AE%81%E6%BC%8F%E5%87%BA%E3%80%8B.pdf" >}}
    {{< filetree/file name="本部2020答案.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%9C%AC%E9%83%A82020%E7%AD%94%E6%A1%88.pdf" >}}
  {{< /filetree/folder >}}
  {{< filetree/folder name="labs" state="closed" >}}
    {{< filetree/file name="2024_wjd_综合-watermark.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/2024_wjd_%E7%BB%BC%E5%90%88-watermark.pdf" >}}
    {{< filetree/file name="2024_综合实验任务书.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/2024_%E7%BB%BC%E5%90%88%E5%AE%9E%E9%AA%8C%E4%BB%BB%E5%8A%A1%E4%B9%A6.pdf" >}}
  {{< filetree/folder name="ljh_version" state="closed" >}}
    {{< filetree/file name="综合实验报告模板_18号机.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/ljh_version/%E7%BB%BC%E5%90%88%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E6%A8%A1%E6%9D%BF_18%E5%8F%B7%E6%9C%BA.pdf" >}}
  {{< /filetree/folder >}}
    {{< filetree/file name="综合实验模板（修正）.docx" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E7%BB%BC%E5%90%88%E5%AE%9E%E9%AA%8C%E6%A8%A1%E6%9D%BF%EF%BC%88%E4%BF%AE%E6%AD%A3%EF%BC%89.docx" >}}
  {{< /filetree/folder >}}
  {{< filetree/folder name="notes" state="closed" >}}
    {{< filetree/file name="Revision of Auto-Practical.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/notes/Revision%20of%20Auto-Practical.pdf" >}}
    {{< filetree/file name="自控实践B复习_Tintin.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/notes/%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5B%E5%A4%8D%E4%B9%A0_Tintin.pdf" >}}
    {{< filetree/file name="自控实践复习整理byAb1g2he.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/notes/%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5%E5%A4%8D%E4%B9%A0%E6%95%B4%E7%90%86byAb1g2he.pdf" >}}
  {{< /filetree/folder >}}
{{< /filetree/container >}}

如果你是校内学生，可移步至 <a href='https://open.osa.moe/openauto/AUTO3002B'>open.osa.moe</a> 查看本门课程的电子书、课件和实验软件等。

## 参与

《HITSZ 自动化课程攻略共享计划》是所有同学都可以参与编写的，如果你有好的笔记或者资料，欢迎前往我们的 [GitHub](https://github.com/HITSZ-OpenAuto) 进行参与，也可以发邮件至 [📮hi@hoa.moe](mailto:hi@hoa.moe) 联系我们，我们会在收到的第一时间进行答复。

{{< callout type="" >}}
  © 版权声明：[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-nc-sa/4.0/)
{{< /callout >}}
