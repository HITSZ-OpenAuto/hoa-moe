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
{{< hoa-filetree/file name="" type="gitignore" size="15 bytes" date="2024/05/09" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/.gitignore" >}}
{{< hoa-filetree/folder name="assignments" date="" state="closed" >}}
{{< hoa-filetree/folder name="LL" date="" state="closed" >}}
{{< hoa-filetree/file name="HW1" type="pdf" size="63.1 KB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/LL/assignments/LL/HW1.pdf" >}}
{{< hoa-filetree/file name="HW2" type="pdf" size="617.6 KB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/LL/assignments/LL/HW2.pdf" >}}
{{< hoa-filetree/file name="HW3" type="pdf" size="84.1 KB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/LL/assignments/LL/HW3.pdf" >}}
{{< hoa-filetree/file name="HW4" type="pdf" size="118.8 KB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/LL/assignments/LL/HW4.pdf" >}}
{{< hoa-filetree/file name="HW5" type="pdf" size="221.2 KB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/LL/assignments/LL/HW5.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="psp" date="" state="closed" >}}
{{< hoa-filetree/folder name="hw1" date="" state="closed" >}}
{{< hoa-filetree/folder name="code" date="" state="closed" >}}
{{< hoa-filetree/file name="hw1_a" type="m" size="1.7 KB" date="2025/06/27" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/psp/hw1/code/assignments/psp/hw1/code/hw1_a.m" >}}
{{< hoa-filetree/file name="hw1_b" type="m" size="1.1 KB" date="2025/06/27" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/psp/hw1/code/assignments/psp/hw1/code/hw1_b.m" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/file name="hw1-psp" type="docx" size="687.1 KB" date="2025/06/27" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/psp/hw1/assignments/psp/hw1/hw1-psp.docx" >}}
{{< hoa-filetree/file name="hw1" type="pdf" size="109.5 KB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/psp/hw1/assignments/psp/hw1/hw1.pdf" >}}
{{< hoa-filetree/folder name="simu" date="" state="closed" >}}
{{< hoa-filetree/file name="simu_22a" type="slx" size="42.3 KB" date="2025/06/27" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/psp/hw1/simu/assignments/psp/hw1/simu/simu_22a.slx" >}}
{{< hoa-filetree/file name="simu_25a" type="slx" size="40.7 KB" date="2025/06/27" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/psp/hw1/simu/assignments/psp/hw1/simu/simu_25a.slx" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="hw2" date="" state="closed" >}}
{{< hoa-filetree/file name="hw2-psp" type="docx" size="589.9 KB" date="2025/06/27" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/psp/hw2/assignments/psp/hw2/hw2-psp.docx" >}}
{{< hoa-filetree/file name="hw2" type="pdf" size="62.3 KB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/psp/hw2/assignments/psp/hw2/hw2.pdf" >}}
{{< hoa-filetree/folder name="simu" date="" state="closed" >}}
{{< hoa-filetree/file name="simu_22a" type="slx" size="43.8 KB" date="2025/06/27" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/psp/hw2/simu/assignments/psp/hw2/simu/simu_22a.slx" >}}
{{< hoa-filetree/file name="simu_25a" type="slx" size="46.4 KB" date="2025/06/27" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/psp/hw2/simu/assignments/psp/hw2/simu/simu_25a.slx" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="exams" date="" state="closed" >}}
{{< hoa-filetree/folder name="本部" date="" state="closed" >}}
{{< hoa-filetree/folder name="答案" date="" state="closed" >}}
{{< hoa-filetree/file name="2020 控制系统实践 II 试题-psp 详解" type="pdf" size="5.5 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%9C%AC%E9%83%A8/%E7%AD%94%E6%A1%88/exams/%E6%9C%AC%E9%83%A8/%E7%AD%94%E6%A1%88/2020%20%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E5%AE%9E%E8%B7%B5II%E8%AF%95%E9%A2%98-psp%E8%AF%A6%E8%A7%A3.pdf" >}}
{{< hoa-filetree/file name="2020 控制系统实践 II 试题答案" type="pdf" size="5.6 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%9C%AC%E9%83%A8/%E7%AD%94%E6%A1%88/exams/%E6%9C%AC%E9%83%A8/%E7%AD%94%E6%A1%88/2020%20%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E5%AE%9E%E8%B7%B5II%E8%AF%95%E9%A2%98%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="控制系统实践 II 复习题-psp 详解" type="pdf" size="15.8 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%9C%AC%E9%83%A8/%E7%AD%94%E6%A1%88/exams/%E6%9C%AC%E9%83%A8/%E7%AD%94%E6%A1%88/%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E5%AE%9E%E8%B7%B5II%E5%A4%8D%E4%B9%A0%E9%A2%98-psp%E8%AF%A6%E8%A7%A3.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="题目" date="" state="closed" >}}
{{< hoa-filetree/file name="2020 控制系统实践 II 试题" type="pdf" size="1.7 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%9C%AC%E9%83%A8/%E9%A2%98%E7%9B%AE/exams/%E6%9C%AC%E9%83%A8/%E9%A2%98%E7%9B%AE/2020%20%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E5%AE%9E%E8%B7%B5II%E8%AF%95%E9%A2%98.pdf" >}}
{{< hoa-filetree/file name="控制系统实践 II 复习题" type="pdf" size="15.6 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%9C%AC%E9%83%A8/%E9%A2%98%E7%9B%AE/exams/%E6%9C%AC%E9%83%A8/%E9%A2%98%E7%9B%AE/%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E5%AE%9E%E8%B7%B5II%E5%A4%8D%E4%B9%A0%E9%A2%98.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="深圳" date="" state="closed" >}}
{{< hoa-filetree/file name="2021 自动控制实践 B 试题与答案-psp 详解" type="pdf" size="2.3 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%B7%B1%E5%9C%B3/exams/%E6%B7%B1%E5%9C%B3/2021%20%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5B%E8%AF%95%E9%A2%98%E4%B8%8E%E7%AD%94%E6%A1%88-psp%E8%AF%A6%E8%A7%A3.pdf" >}}
{{< hoa-filetree/file name="2021 自动控制实践 B 试题与答案" type="pdf" size="652.3 KB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%B7%B1%E5%9C%B3/exams/%E6%B7%B1%E5%9C%B3/2021%20%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5B%E8%AF%95%E9%A2%98%E4%B8%8E%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="2024 自动控制实践 B 试题回忆版-psp 详解" type="pdf" size="9.2 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%B7%B1%E5%9C%B3/exams/%E6%B7%B1%E5%9C%B3/2024%20%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5B%E8%AF%95%E9%A2%98%E5%9B%9E%E5%BF%86%E7%89%88-psp%E8%AF%A6%E8%A7%A3.pdf" >}}
{{< hoa-filetree/file name="2024 自动控制实践 B 试题回忆版" type="pdf" size="652.8 KB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%B7%B1%E5%9C%B3/exams/%E6%B7%B1%E5%9C%B3/2024%20%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5B%E8%AF%95%E9%A2%98%E5%9B%9E%E5%BF%86%E7%89%88.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="labs" date="" state="closed" >}}
{{< hoa-filetree/folder name="2024" date="" state="closed" >}}
{{< hoa-filetree/folder name="LJH" date="" state="closed" >}}
{{< hoa-filetree/file name="ljh_综合实验报告_18 号机" type="pdf" size="1.7 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/2024/LJH/labs/2024/LJH/ljh_%E7%BB%BC%E5%90%88%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A_18%E5%8F%B7%E6%9C%BA.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="WJD" date="" state="closed" >}}
{{< hoa-filetree/file name="wjd_综合" type="pdf" size="2.4 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/2024/WJD/labs/2024/WJD/wjd_%E7%BB%BC%E5%90%88.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2025" date="" state="closed" >}}
{{< hoa-filetree/folder name="psp" date="" state="closed" >}}
{{< hoa-filetree/file name="2025-psp" type="docx" size="2.3 MB" date="2025/06/27" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/2025/psp/labs/2025/psp/2025-psp.docx" >}}
{{< hoa-filetree/folder name="simu" date="" state="closed" >}}
{{< hoa-filetree/file name="simu_22a" type="slx" size="36.9 KB" date="2025/06/27" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/2025/psp/simu/labs/2025/psp/simu/simu_22a.slx" >}}
{{< hoa-filetree/file name="simu_25a" type="slx" size="102.4 KB" date="2025/06/27" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/2025/psp/simu/labs/2025/psp/simu/simu_25a.slx" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/file name="实验任务书" type="pdf" size="5.6 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/2025/labs/2025/%E5%AE%9E%E9%AA%8C%E4%BB%BB%E5%8A%A1%E4%B9%A6.pdf" >}}
{{< hoa-filetree/file name="实验报告模板" type="docx" size="976.9 KB" date="2025/06/27" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/2025/labs/2025/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E6%A8%A1%E6%9D%BF.docx" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="notes" date="" state="closed" >}}
{{< hoa-filetree/file name="November_in_North_自控实践 B 笔记" type="pdf" size="97.5 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/notes/notes/November_in_North_%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5B%E7%AC%94%E8%AE%B0.pdf" >}}
{{< hoa-filetree/file name="Revision of Auto-Practical" type="pdf" size="9.4 MB" date="2024/05/09" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/notes/notes/Revision%20of%20Auto-Practical.pdf" >}}
{{< hoa-filetree/file name="【2025 春季学期】自动控制实践 B 课程总结笔记 -22 级自动化 - 刘劭航-v1.2" type="pdf" size="2.6 MB" date="2025/06/03" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/notes/notes/%E3%80%902025%E6%98%A5%E5%AD%A3%E5%AD%A6%E6%9C%9F%E3%80%91%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5B%E8%AF%BE%E7%A8%8B%E6%80%BB%E7%BB%93%E7%AC%94%E8%AE%B0-22%E7%BA%A7%E8%87%AA%E5%8A%A8%E5%8C%96-%E5%88%98%E5%8A%AD%E8%88%AA-v1.2.pdf" >}}
{{< hoa-filetree/file name="自控实践 B 复习_Tintin" type="pdf" size="6.4 MB" date="2024/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/notes/notes/%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5B%E5%A4%8D%E4%B9%A0_Tintin.pdf" >}}
{{< hoa-filetree/file name="自控实践复习整理 byAb1g2he" type="pdf" size="3.4 MB" date="2024/07/16" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/notes/notes/%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5%E5%A4%8D%E4%B9%A0%E6%95%B4%E7%90%86byAb1g2he.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="slides" date="" state="closed" >}}
{{< hoa-filetree/folder name="课件 - 带笔记-psp" date="" state="closed" >}}
{{< hoa-filetree/file name="1 绪论" type="pdf" size="716.7 KB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/1%20%E7%BB%AA%E8%AE%BA.pdf" >}}
{{< hoa-filetree/file name="10 课程习题讲解" type="pdf" size="3.2 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/10%20%E8%AF%BE%E7%A8%8B%E4%B9%A0%E9%A2%98%E8%AE%B2%E8%A7%A3.pdf" >}}
{{< hoa-filetree/file name="2 控制系统的设计流程" type="pdf" size="2.3 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/2%20%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E7%9A%84%E8%AE%BE%E8%AE%A1%E6%B5%81%E7%A8%8B.pdf" >}}
{{< hoa-filetree/file name="3.1 控制系统的输入条件分析 - 输入" type="pdf" size="13.3 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/3.1%20%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E7%9A%84%E8%BE%93%E5%85%A5%E6%9D%A1%E4%BB%B6%E5%88%86%E6%9E%90-%E8%BE%93%E5%85%A5.pdf" >}}
{{< hoa-filetree/file name="3.2 控制系统输入条件分析 - 干扰" type="pdf" size="6.8 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/3.2%20%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E8%BE%93%E5%85%A5%E6%9D%A1%E4%BB%B6%E5%88%86%E6%9E%90-%E5%B9%B2%E6%89%B0.pdf" >}}
{{< hoa-filetree/file name="3.3 控制系统输入条件分析 - 噪声" type="pdf" size="9.1 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/3.3%20%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E8%BE%93%E5%85%A5%E6%9D%A1%E4%BB%B6%E5%88%86%E6%9E%90-%E5%99%AA%E5%A3%B0.pdf" >}}
{{< hoa-filetree/file name="4 控制系统的设计约束" type="pdf" size="12.0 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/4%20%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E7%9A%84%E8%AE%BE%E8%AE%A1%E7%BA%A6%E6%9D%9F.pdf" >}}
{{< hoa-filetree/file name="5 Anti-Windup 设计" type="pdf" size="6.4 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/5%20Anti-Windup%E8%AE%BE%E8%AE%A1.pdf" >}}
{{< hoa-filetree/file name="6 伺服系统" type="pdf" size="6.3 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/6%20%E4%BC%BA%E6%9C%8D%E7%B3%BB%E7%BB%9F.pdf" >}}
{{< hoa-filetree/file name="7 调节系统的设计" type="pdf" size="7.1 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/7%20%E8%B0%83%E8%8A%82%E7%B3%BB%E7%BB%9F%E7%9A%84%E8%AE%BE%E8%AE%A1.pdf" >}}
{{< hoa-filetree/file name="8 多回路系统的设计" type="pdf" size="5.1 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/8%20%E5%A4%9A%E5%9B%9E%E8%B7%AF%E7%B3%BB%E7%BB%9F%E7%9A%84%E8%AE%BE%E8%AE%A1.pdf" >}}
{{< hoa-filetree/file name="9 课程总结" type="pdf" size="1.3 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/9%20%E8%AF%BE%E7%A8%8B%E6%80%BB%E7%BB%93.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/container >}}

## 参与

HOA Core 成员有意重构 hoa 的网站，以接入更多的专业，实现更好的体验。如果你对资料分享或者网站搭建感兴趣，即使来自其他专业，非常欢迎你[联系](mailto:hi@hoa.moe)/加入我们 Core 团队。这里有我们[初步的重构计划](https://historical-mousepad-286.notion.site/HOA-1f71751ad5fe80978c70d9e32330d7e6)。

同时，HOA Core 初代成员已经毕业，如果你想加入 HOA Core，请阅读我们的博客了解更多：[《HOA 的未来，需要你一起来书写》](https://hoa.moe/news/future-of-hoa)。

{{< callout type="" >}}
  © 版权声明：[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-nc-sa/4.0/)
{{< /callout >}}

