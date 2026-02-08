---
title: （必修）自动控制实践 A
weight: 9
toc: true
editURL: "https://github.com/HITSZ-OpenAuto/AUTO3002A/edit/main/README.md"
math: true
---

{{< update-info update_time="2025 年 10 月 25 日" author="Maxwell Jay" message="添加关于习题答案的提醒 (#38)" >}}

<div class="hoa-badge">

![Static Badge](https://img.shields.io/badge/%E8%80%83%E8%AF%95%E8%AF%BE-red)
![Static Badge](https://img.shields.io/badge/%E5%AD%A6%E5%88%86-3-moccasin)

![Static Badge](https://img.shields.io/badge/%E6%88%90%E7%BB%A9%E6%9E%84%E6%88%90（21,22%E7%BA%A7）-gold)
![Static Badge](https://img.shields.io/badge/%E4%BD%9C%E4%B8%9A-10%25-wheat)
![Static Badge](https://img.shields.io/badge/%E5%AE%9E%E9%AA%8C-25%25-wheat)
![Static Badge](https://img.shields.io/badge/%E6%9C%9F%E6%9C%AB%E8%80%83%E8%AF%95-65%25-wheat)

![Static Badge](https://img.shields.io/badge/%E6%80%BB%E5%AD%A6%E6%97%B6-48-wheat) ![Static Badge](https://img.shields.io/badge/%E8%AE%B2%E8%AF%BE-40-wheat) ![Static Badge](https://img.shields.io/badge/%E5%AE%9E%E9%AA%8C-2%E5%AD%A6%E6%97%B6*4-wheat)

</div>

该课程有配套的课程设计（2024 年秋季学期起改名为“实验”）：[自动控制实践 A 实验](https://hoa.moe/docs/junior-autumn/auto3016/)，独立设课，1.5 学分，40 学时。



## 教材

梅晓榕主编，自动控制元件及线路（第五版），科学出版社。

### 习题答案

- [《自动控制元件》复习笔记及习题答案 - Bilibili 专栏](https://www.bilibili.com/read/cv19892484/)
- [《自动控制元件》期末总结及课后习题答案 - Bilibili 专栏](https://www.bilibili.com/read/cv22652100)

> [!NOTE]
> 1. 以上两篇专栏为民间整理，不能保证完全正确，阅读时自行辨别正误。
> 2. 本仓库 materials 文件夹下的《自动控制元件及线路课后题答案（百度文库）》与《自动控制元件习题资料》系从网上下载，部分习题与老师布置的课后作业相同，可作补充，但是答案不一定正确，仅供参考。

## 课程介绍

本课程涵盖三部分内容，以第一块内容为最重：

1. 电机驱动与拖动
2. 简单的电力电子技术（PWM）
3. 传感与测量元件

### 电机学

传统电机学教材，可以看里面的直流电机、变压器、异步电机和同步电机：

- （哈尔滨理工大学）戈宝军，梁艳萍，温嘉斌，电机学（第三版），中国电力出版社。

  配套网课：[电机学（哈尔滨理工大学）- Bilibili](https://www.bilibili.com/video/BV1cx411Z76w)

- （哈尔滨理工大学）汤蕴璆编著，电机学（第 5 版），机械工业出版社。
- （大连理工大学）孙建忠、刘凤春等编，电机与拖动（第 4 版），机械工业出版社。

关于伺服电机和步进电机，可以参考以下书目：

- [日]坂本正文著，王自强译，步进电机应用技术，科学出版社 2010 年版。（翻译有些错误，凑合着看）
  - 此书已放到校内网盘。
- （一些奇怪的论坛里的 pdf，找到后放上来）

### 电力电子技术

本门课对电力电子技术要求很低。如果大家想拓展 ~~(学电气的专业课)~~ ，可以参考：

- （西安交通大学）王兆安等，电力电子技术（第 5 版），机械工业出版社。
- Erickson，Fundamental of power electronics（3rd ed.)，Springer。
- [傅旻帆个人主页 - Bilibili](https://space.bilibili.com/519909115)
- [西瓜粥西瓜粥个人主页 - Bilibili](https://space.bilibili.com/287344644)

（请大家量力而行，学有余力再去看拓展提高的内容！）

<!-- ### 传感与测量元件 待补充-->

## 学时安排

<h4>学时安排表（21 级）</h4>

> 文/ [Oliver Wu](https://github.com/OliverWu515)，2024.2

<table border="1">
  <thead>
    <tr>
      <th>授课教师</th>
      <th>授课内容</th>
      <th>学时安排</th>
      <th>建议</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="10">隆志力</td>
      <td>绪论</td>
      <td>2</td>
      <td>了解即可。</td>
    </tr>
    <tr>
      <td>磁路基础</td>
      <td>2</td>
      <td>重要！磁量的关系、磁路定律要很清楚，变压器和交流电机中经常用到。</td>
    </tr>
    <tr>
      <td>直流电机的结构和工作原理</td>
      <td>2</td>
      <td>结构要认识（不用细到绕法这些，只要知道每个部件名称和属于定子还是转子）、工作原理比较好理解，重点是换向器和电刷，简单描述即可。</td>
    </tr>
    <tr>
      <td>直流电机的磁场、电枢反应与换向</td>
      <td>2</td>
      <td>理解，重在知道结果，不是重点。</td>
    </tr>
    <tr>
      <td>直流电机基本方程、机械特性、调节特性</td>
      <td>2</td>
      <td>很重要，需要记忆几乎每个公式！数形结合是很重要的方法！结合图形分析事半功倍！</td>
    </tr>
    <tr>
      <td>直流电机的调速运行</td>
      <td>2</td>
      <td>很重要，需要结合图形记忆调速方式的特点！</td>
    </tr>
    <tr>
      <td>直流电机的四象限运行（工作状态）</td>
      <td>2</td>
      <td>很重要，需要结合图形记忆每个象限、曲线的不同阶段对应的工作状态！</td>
    </tr>
    <tr>
      <td>电力电子技术概述</td>
      <td>2</td>
      <td>理解，主要关注器件分类、工作原理、适用范围。</td>
    </tr>
    <tr>
      <td>PWM</td>
      <td>2</td>
      <td>很重要，需要理解一个周期 PWM 元件上的电流流向、导通关断与否以及元件的作用。</td>
    </tr>
    <tr>
      <td>变压器</td>
      <td>2</td>
      <td>很重要，学时很少，要记忆的东西却很多。重点在负载运行和空载运行的基本方程和 T 形等效电路。笔记文件夹里的笔记整理得很清楚。</td>
    </tr>
    <tr>
      <td rowspan="10">李建刚</td>
      <td>课程概述</td>
      <td>1</td>
      <td>了解即可。</td>
    </tr>
    <tr>
      <td>步进电机的结构与工作原理</td>
      <td>1</td>
      <td>重要。理解“错齿是使步进电机运动的根本原因”。关于齿数的计算，反应式和混合式其实是有不同的。但是一般按照反应式的公式计算。</td>
    </tr>
    <tr>
      <td>步进电机的静态特性、动态特性与驱动</td>
      <td>3</td>
      <td>重要。静态特性主要是矩角特性，动态特性主要是从矩角特性出发用合成法来分析启动特性（图解特别重要），以及矩频特性。驱动以细分驱动为主。</td>
    </tr>
    <tr>
      <td>交流电机概述</td>
      <td>2</td>
      <td>这节课让大家对异步电机和同步电机的结构和工作原理有基本的认识。但是详细的分析还需后面仔细学习。</td>
    </tr>
    <tr>
      <td>无刷直流电机与交流伺服电机</td>
      <td>5</td>
      <td>讲得最细致的部分，但其实原理相对比较简单，重点理解六步换向和 Clark-Park/d-q 变换，理解如何将伺服电机的驱动变得像有刷直流那样简单。</td>
    </tr>
    <tr>
      <td>测量元件、旋转变压器、感应同步器、编码器、光栅</td>
      <td>3</td>
      <td>由于学时剩余很少，讲课速度开始进入倍速模式。大家从这里开始只要尽量听明白就行，笔记课后再做。</td>
    </tr>
    <tr>
      <td>交流绕组的基本原理，三相异步电机的原理及结构</td>
      <td>2</td>
      <td>是重点，也是难点！！但是学时比较少。旋转磁场理解起来比较困难。详见文件中的异步电机笔记。</td>
    </tr>
    <tr>
      <td>三相异步电机的等效电路及运行分析，机械特性和调速运行</td>
      <td>约 2.5</td>
      <td>是重点，也是难点！！但是你没看错，2 学时结束了。等效的流程：电路模型 - 频率归算->绕组归算。<b>异步电机可以看成“会动的变压器”！</b> 详见 notes 文件夹下异步电机的笔记。考试基本是定性分析，定量分析（计算题）要求不高，难度不超过作业题。</td>
    </tr>
    <tr>
      <td>单相异步电机的等效电路及运行分析</td>
      <td>约 0.5</td>
      <td>需要理解单相异步电机的启动，有小题。</td>
    </tr>
    <tr>
      <td>小功率同步电机</td>
      <td>0</td>
      <td>没时间了，没讲，考试不涉及。</td>
    </tr>
  </tbody>
</table>

<!--在表格 td 中，有两个属性控制居中显示
	align——表示左右居中——left，center，right
	valign——控制上下居中——left，center，right
	width——控制单元格宽度，单位像素
	cellspacing——单元格之间的间隔，单位像素
-->

## 授课教师

（21 级、22 级情况）

- 隆志力
  - 授课风格：稍显含糊，车轱辘话较多；课件内容较丰富，有别学校课件截下来的内容，不过画质较差，而且比较乱，不适合直接做笔记。
  - 听课建议：基本忠于 PPT（不会自由发挥），由于车轱辘话较多，知识讲解得比较抽象，上课不易听懂，课后要多花时间。
- 李建刚
  - 授课风格：语速很快（因为学时有限、内容又多，到后面会快到起飞）、逻辑较清晰（到后面由于速度快变得不清晰）、答疑有耐心、板书不好看、语气词较多（到后程语速极快，
    但信噪比极低）、课件较美观（但是由于摘选自外校课件，有较多符号的冲突，时有逻辑不连贯）。
  - 听课建议：因为上课节奏较快，上课只求听懂大概即可（更有可能是听不懂），但课后务必（参考前人资料）整理笔记！！！

## 关于考试

> 文 / [Oliver Wu](https://github.com/OliverWu515)，2024.2

- 题量较大，但是含有大量往年题。对于做过往年题的同学来说，完卷并不困难，甚至有较多时间检查。
- 有少数题目不太严谨，不要因为这个影响答题。
- 仅做往年题而不理解概念的后果，就是对于往年题之外的题目无从下手。所以这门课虽说挂科率不高，但考高分的也少。
- 所以，往年题只供大家参考，只靠通过刷往年考试题来获取高分或者保证不挂科是**不可取的**。而且往年题有许多题目并无答案，需要理解并且与同学讨论来得出答案。**希望大家认真复习，把基本概念、方法掌握扎实。**

> 文 / [psp_dada](https://github.com/pspdada), 2024.12

24 秋，对于自控实践 A 这门课考试的复习，最重要的是清楚地知道**我们是自动化专业而不是电气专业**，由于电气专业同步上电机学，和我们的部分内容有相关性，且是同时考试，导致部分同学因为看到电气同学的复习内容而对我们的考试过于担忧，这不仅是 22 级的现象，21 级也有类似现象。通过分析近两年的考题便可发现，我们的考试内容重点和电气的电机学有很大不同，因此不要盲目焦虑。例如有刷直流电机部分的计算是重点，需掌握发电机和电动机的基本平衡方程以及机械特性；而异步电机部分对于功率的计算有一定要求，但归算部分没有要求。因此我在复习的时候直接跳过了变压器和异步电机的归算，直接记归算结果（等效电路）。

24 秋的考试相比 23 年，后面的计算题和综合题（就是复杂一些的计算题）几乎没有变化，但是每道计算题和往年相比都会有细微的差别，导致实际上每道题都需要经过自己的思考。因此**仅仅背题而不理解知识点是完全不够的**。我上传了往年题以及章节题目的详细解析，希望其中的思考过程可以帮助大家更好地理解知识点。（与其他同学进行过多次讨论校对，但如果仍有错误欢迎修改，也欢迎补充更多的解题思路及技巧）

此外，前面的选择题、填空题、简答题的比重有所上升，所包含的知识点范围也很广，复习的面面俱到确实难度较大。推荐同学们可以参考 notes 文件夹下 wjd 学长 [Oliver Wu](https://github.com/OliverWu515) 的笔记，他对课程中出现的每个知识点都有仔细地思考和详尽的解释，对于复习时理解知识点有很大的帮助。

24 秋考试可以携带计算器。

## 关于实验

> 文 / [psp_dada](https://github.com/pspdada), 2025.1

自控实践 A 的课内实验内容较为简单，每个实验的内容都很少，可以速通，但是最后给分的情况比较玄妙。

## 资料下载

如果你是校内学生，可点击如下「内网网盘」按钮查看本门课程的电子书、课件和实验软件等。

{{< hoa-filetree/container driveURL="https://open.osa.moe/openauto/AUTO3002A" repoURL="https://github.com/HITSZ-OpenAuto/AUTO3002A" >}}
{{< hoa-filetree/folder name="assignments" date="" state="closed" >}}
{{< hoa-filetree/folder name="2022" date="" state="closed" >}}
{{< hoa-filetree/file name="ACPP_HW1" type="pdf" size="819.8 KB" date="2024/12/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/2022/ACPP_HW1.pdf" >}}
{{< hoa-filetree/file name="ACPP_HW2" type="pdf" size="302.3 KB" date="2024/12/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/2022/ACPP_HW2.pdf" >}}
{{< hoa-filetree/file name="ACPP_HW3" type="pdf" size="232.3 KB" date="2024/12/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/2022/ACPP_HW3.pdf" >}}
{{< hoa-filetree/file name="作业 3" type="pdf" size="141.8 KB" date="2024/12/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/2022/%E4%BD%9C%E4%B8%9A3.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2023" date="" state="closed" >}}
{{< hoa-filetree/file name="后半程作业答案" type="pdf" size="426.7 KB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/2023/%E5%90%8E%E5%8D%8A%E7%A8%8B%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="异步电机部分作业" type="pdf" size="43.4 KB" date="2024/12/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/2023/%E5%BC%82%E6%AD%A5%E7%94%B5%E6%9C%BA%E9%83%A8%E5%88%86%E4%BD%9C%E4%B8%9A.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2024" date="" state="closed" >}}
{{< hoa-filetree/folder name="psp" date="" state="closed" >}}
{{< hoa-filetree/file name="1 直流电机" type="pdf" size="1.5 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/2024/psp/1%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA.pdf" >}}
{{< hoa-filetree/file name="2 变压器" type="pdf" size="447.7 KB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/2024/psp/2%20%E5%8F%98%E5%8E%8B%E5%99%A8.pdf" >}}
{{< hoa-filetree/file name="3 异步电机" type="pdf" size="1.5 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/2024/psp/3%20%E5%BC%82%E6%AD%A5%E7%94%B5%E6%9C%BA.pdf" >}}
{{< hoa-filetree/file name="5 步进电机" type="pdf" size="531.7 KB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/2024/psp/5%20%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA.pdf" >}}
{{< hoa-filetree/file name="6 无刷直流电机与交流伺服电机" type="pdf" size="770.4 KB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/2024/psp/6%20%E6%97%A0%E5%88%B7%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E4%B8%8E%E4%BA%A4%E6%B5%81%E4%BC%BA%E6%9C%8D%E7%94%B5%E6%9C%BA.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="exams" date="" state="closed" >}}
{{< hoa-filetree/folder name="本部 - 往年题" date="" state="closed" >}}
{{< hoa-filetree/file name="哈工大自动控制元件及线路历年考题" type="pdf" size="4.8 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E5%BE%80%E5%B9%B4%E9%A2%98/%E5%93%88%E5%B7%A5%E5%A4%A7%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%85%83%E4%BB%B6%E5%8F%8A%E7%BA%BF%E8%B7%AF%E5%8E%86%E5%B9%B4%E8%80%83%E9%A2%98.pdf" >}}
{{< hoa-filetree/file name="自动控制元件及线路 2012 秋期末试卷" type="pdf" size="1.8 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E5%BE%80%E5%B9%B4%E9%A2%98/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%85%83%E4%BB%B6%E5%8F%8A%E7%BA%BF%E8%B7%AF2012%E7%A7%8B%E6%9C%9F%E6%9C%AB%E8%AF%95%E5%8D%B7.pdf" >}}
{{< hoa-filetree/file name="自动控制元件及线路 2019 秋期末试卷" type="pdf" size="2.7 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E5%BE%80%E5%B9%B4%E9%A2%98/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%85%83%E4%BB%B6%E5%8F%8A%E7%BA%BF%E8%B7%AF2019%E7%A7%8B%E6%9C%9F%E6%9C%AB%E8%AF%95%E5%8D%B7.pdf" >}}
{{< hoa-filetree/file name="自动控制元件及线路 2020 秋期末试卷" type="pdf" size="1.4 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E5%BE%80%E5%B9%B4%E9%A2%98/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%85%83%E4%BB%B6%E5%8F%8A%E7%BA%BF%E8%B7%AF2020%E7%A7%8B%E6%9C%9F%E6%9C%AB%E8%AF%95%E5%8D%B7.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="本部 - 试题汇编" date="" state="closed" >}}
{{< hoa-filetree/file name="1 绪论相关试题 - 答案" type="docx" size="51.6 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/1%20%E7%BB%AA%E8%AE%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx" >}}
{{< hoa-filetree/file name="1 绪论相关试题" type="docx" size="15.1 KB" date="2023/12/17" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/1%20%E7%BB%AA%E8%AE%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx" >}}
{{< hoa-filetree/file name="10 变压器相关试题 - 答案" type="docx" size="595.6 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/10%20%E5%8F%98%E5%8E%8B%E5%99%A8%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx" >}}
{{< hoa-filetree/file name="10 变压器相关试题" type="docx" size="579.8 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/10%20%E5%8F%98%E5%8E%8B%E5%99%A8%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx" >}}
{{< hoa-filetree/file name="13 异步电机相关试题 - 答案" type="docx" size="172.1 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/13%20%E5%BC%82%E6%AD%A5%E7%94%B5%E6%9C%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx" >}}
{{< hoa-filetree/file name="13 异步电机相关试题" type="docx" size="88.1 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/13%20%E5%BC%82%E6%AD%A5%E7%94%B5%E6%9C%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx" >}}
{{< hoa-filetree/file name="14 小功率同步电机相关试题" type="docx" size="13.2 KB" date="2023/12/17" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/14%20%E5%B0%8F%E5%8A%9F%E7%8E%87%E5%90%8C%E6%AD%A5%E7%94%B5%E6%9C%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx" >}}
{{< hoa-filetree/file name="15 步进电机相关试题 - 答案" type="docx" size="20.6 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/15%20%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx" >}}
{{< hoa-filetree/file name="15 步进电机相关试题" type="docx" size="12.9 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/15%20%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx" >}}
{{< hoa-filetree/file name="16 无刷直流电机相关试题 - 答案" type="docx" size="11.3 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/16%20%E6%97%A0%E5%88%B7%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx" >}}
{{< hoa-filetree/file name="16 无刷直流电机相关试题" type="docx" size="11.0 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/16%20%E6%97%A0%E5%88%B7%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx" >}}
{{< hoa-filetree/file name="2 磁路基础知识相关例题 - 答案" type="docx" size="16.9 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/2%20%E7%A3%81%E8%B7%AF%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E7%9B%B8%E5%85%B3%E4%BE%8B%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx" >}}
{{< hoa-filetree/file name="2 磁路基础知识相关例题" type="docx" size="11.7 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/2%20%E7%A3%81%E8%B7%AF%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E7%9B%B8%E5%85%B3%E4%BE%8B%E9%A2%98.docx" >}}
{{< hoa-filetree/file name="22 测量元件相关试题  - 答案" type="docx" size="62.1 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/22%20%E6%B5%8B%E9%87%8F%E5%85%83%E4%BB%B6%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20%20-%20%E7%AD%94%E6%A1%88.docx" >}}
{{< hoa-filetree/file name="22 测量元件相关试题 " type="docx" size="18.1 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/22%20%E6%B5%8B%E9%87%8F%E5%85%83%E4%BB%B6%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20.docx" >}}
{{< hoa-filetree/file name="3 直流电机的原理与基本结构相关例题 - 答案" type="docx" size="19.8 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/3%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9A%84%E5%8E%9F%E7%90%86%E4%B8%8E%E5%9F%BA%E6%9C%AC%E7%BB%93%E6%9E%84%E7%9B%B8%E5%85%B3%E4%BE%8B%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx" >}}
{{< hoa-filetree/file name="3 直流电机的原理与基本结构相关例题" type="docx" size="12.1 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/3%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9A%84%E5%8E%9F%E7%90%86%E4%B8%8E%E5%9F%BA%E6%9C%AC%E7%BB%93%E6%9E%84%E7%9B%B8%E5%85%B3%E4%BE%8B%E9%A2%98.docx" >}}
{{< hoa-filetree/file name="4 直流电机的特性与控制方法相关试题 - 答案" type="docx" size="267.3 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/4%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9A%84%E7%89%B9%E6%80%A7%E4%B8%8E%E6%8E%A7%E5%88%B6%E6%96%B9%E6%B3%95%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx" >}}
{{< hoa-filetree/file name="4 直流电机的特性与控制方法相关试题" type="docx" size="238.0 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/4%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9A%84%E7%89%B9%E6%80%A7%E4%B8%8E%E6%8E%A7%E5%88%B6%E6%96%B9%E6%B3%95%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx" >}}
{{< hoa-filetree/file name="5 直流电机的动特性与选择相关试题 - 答案" type="docx" size="135.4 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/5%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9A%84%E5%8A%A8%E7%89%B9%E6%80%A7%E4%B8%8E%E9%80%89%E6%8B%A9%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx" >}}
{{< hoa-filetree/file name="5 直流电机的动特性与选择相关试题" type="docx" size="46.7 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/5%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9A%84%E5%8A%A8%E7%89%B9%E6%80%A7%E4%B8%8E%E9%80%89%E6%8B%A9%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx" >}}
{{< hoa-filetree/file name="9 功率放大器相关试题 - 答案" type="docx" size="355.9 KB" date="2024/12/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/9%20%E5%8A%9F%E7%8E%87%E6%94%BE%E5%A4%A7%E5%99%A8%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx" >}}
{{< hoa-filetree/file name="9 功率放大器相关试题" type="docx" size="45.7 KB" date="2023/12/17" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/9%20%E5%8A%9F%E7%8E%87%E6%94%BE%E5%A4%A7%E5%99%A8%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="深圳" date="" state="closed" >}}
{{< hoa-filetree/file name="2023 秋自动控制实践 A 试题回忆版" type="pdf" size="551.3 KB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%B7%B1%E5%9C%B3/2023%E7%A7%8B%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A%E8%AF%95%E9%A2%98%E5%9B%9E%E5%BF%86%E7%89%88.pdf" >}}
{{< hoa-filetree/file name="2023 秋自动控制实践 A 试题回忆版参考答案" type="docx" size="1.3 MB" date="2025/06/27" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%B7%B1%E5%9C%B3/2023%E7%A7%8B%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A%E8%AF%95%E9%A2%98%E5%9B%9E%E5%BF%86%E7%89%88%E5%8F%82%E8%80%83%E7%AD%94%E6%A1%88.docx" >}}
{{< hoa-filetree/file name="2024 秋自动控制实践 A 期末试题参考答案 v2.2 版" type="pdf" size="5.4 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%B7%B1%E5%9C%B3/2024%E7%A7%8B%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A%E6%9C%9F%E6%9C%AB%E8%AF%95%E9%A2%98%E5%8F%82%E8%80%83%E7%AD%94%E6%A1%88v2.2%E7%89%88.pdf" >}}
{{< hoa-filetree/file name="2024 秋自控实践期末（回忆 v2.0 版） " type="pdf" size="433.5 KB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%B7%B1%E5%9C%B3/2024%E7%A7%8B%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5%E6%9C%9F%E6%9C%AB%EF%BC%88%E5%9B%9E%E5%BF%86v2.0%E7%89%88%EF%BC%89%20.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="labs" date="" state="closed" >}}
{{< hoa-filetree/folder name="2021" date="" state="closed" >}}
{{< hoa-filetree/folder name="LMH_2021" date="" state="closed" >}}
{{< hoa-filetree/file name="实验报告 - 实验 1" type="pdf" size="4.5 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2021/LMH_2021/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A-%E5%AE%9E%E9%AA%8C1.pdf" >}}
{{< hoa-filetree/file name="实验报告 - 实验 2" type="pdf" size="6.0 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2021/LMH_2021/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A-%E5%AE%9E%E9%AA%8C2.pdf" >}}
{{< hoa-filetree/file name="实验报告 - 实验 3" type="pdf" size="7.6 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2021/LMH_2021/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A-%E5%AE%9E%E9%AA%8C3.pdf" >}}
{{< hoa-filetree/file name="实验报告 - 实验 4" type="pdf" size="6.2 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2021/LMH_2021/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A-%E5%AE%9E%E9%AA%8C4.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2022" date="" state="closed" >}}
{{< hoa-filetree/folder name="Tintin" date="" state="closed" >}}
{{< hoa-filetree/folder name="实验一" date="" state="closed" >}}
{{< hoa-filetree/file name="实验一图片" type="zip" size="27.8 KB" date="2025/01/18" icon="icons/zip.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2022/Tintin/%E5%AE%9E%E9%AA%8C%E4%B8%80/%E5%AE%9E%E9%AA%8C%E4%B8%80%E5%9B%BE%E7%89%87.zip" >}}
{{< hoa-filetree/file name="自动控制实践 A 实验报告 1" type="docx" size="1.1 MB" date="2025/01/18" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2022/Tintin/%E5%AE%9E%E9%AA%8C%E4%B8%80/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A1.docx" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="实验三" date="" state="closed" >}}
{{< hoa-filetree/file name="自动控制实践 A 实验报告 3" type="docx" size="1.6 MB" date="2025/01/18" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2022/Tintin/%E5%AE%9E%E9%AA%8C%E4%B8%89/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A3.docx" >}}
{{< hoa-filetree/file name="自控实践实验三数据" type="xlsx" size="21.0 KB" date="2025/01/18" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2022/Tintin/%E5%AE%9E%E9%AA%8C%E4%B8%89/%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5%E5%AE%9E%E9%AA%8C%E4%B8%89%E6%95%B0%E6%8D%AE.xlsx" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="实验二" date="" state="closed" >}}
{{< hoa-filetree/file name="20221018 实验数据" type="xlsx" size="15.0 KB" date="2025/01/18" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2022/Tintin/%E5%AE%9E%E9%AA%8C%E4%BA%8C/20221018%E5%AE%9E%E9%AA%8C%E6%95%B0%E6%8D%AE.xlsx" >}}
{{< hoa-filetree/file name="实验二图片" type="zip" size="71.9 KB" date="2025/01/18" icon="icons/zip.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2022/Tintin/%E5%AE%9E%E9%AA%8C%E4%BA%8C/%E5%AE%9E%E9%AA%8C%E4%BA%8C%E5%9B%BE%E7%89%87.zip" >}}
{{< hoa-filetree/file name="自动控制实践 A 实验报告 2" type="docx" size="1.1 MB" date="2025/01/18" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2022/Tintin/%E5%AE%9E%E9%AA%8C%E4%BA%8C/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A2.docx" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="实验四" date="" state="closed" >}}
{{< hoa-filetree/file name="实验四图片" type="zip" size="275.1 KB" date="2025/01/18" icon="icons/zip.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2022/Tintin/%E5%AE%9E%E9%AA%8C%E5%9B%9B/%E5%AE%9E%E9%AA%8C%E5%9B%9B%E5%9B%BE%E7%89%87.zip" >}}
{{< hoa-filetree/file name="自动控制实践 A 实验报告 4" type="docx" size="1.5 MB" date="2025/01/18" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2022/Tintin/%E5%AE%9E%E9%AA%8C%E5%9B%9B/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A4.docx" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="lab manual" date="" state="closed" >}}
{{< hoa-filetree/file name="1 电机 PWM 控制与驱动电路实验指导书" type="pdf" size="7.8 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2022/lab%20manual/1%20%E7%94%B5%E6%9C%BAPWM%E6%8E%A7%E5%88%B6%E4%B8%8E%E9%A9%B1%E5%8A%A8%E7%94%B5%E8%B7%AF%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6.pdf" >}}
{{< hoa-filetree/file name="2 交流伺服电机特性实验指导书" type="pdf" size="7.4 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2022/lab%20manual/2%20%E4%BA%A4%E6%B5%81%E4%BC%BA%E6%9C%8D%E7%94%B5%E6%9C%BA%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6.pdf" >}}
{{< hoa-filetree/file name="3 步进电机特性实验" type="pdf" size="3.6 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2022/lab%20manual/3%20%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C.pdf" >}}
{{< hoa-filetree/file name="4 传感与测量反馈元件特性实验" type="pdf" size="4.4 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2022/lab%20manual/4%20%E4%BC%A0%E6%84%9F%E4%B8%8E%E6%B5%8B%E9%87%8F%E5%8F%8D%E9%A6%88%E5%85%83%E4%BB%B6%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2023" date="" state="closed" >}}
{{< hoa-filetree/folder name="LJH_2023" date="" state="closed" >}}
{{< hoa-filetree/file name="实验一 - 电机 PWM 控制与驱动电路" type="pdf" size="866.1 KB" date="2024/02/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2023/LJH_2023/%E5%AE%9E%E9%AA%8C%E4%B8%80-%E7%94%B5%E6%9C%BAPWM%E6%8E%A7%E5%88%B6%E4%B8%8E%E9%A9%B1%E5%8A%A8%E7%94%B5%E8%B7%AF.pdf" >}}
{{< hoa-filetree/file name="实验三 - 交流伺服电机特性" type="pdf" size="802.2 KB" date="2024/02/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2023/LJH_2023/%E5%AE%9E%E9%AA%8C%E4%B8%89-%E4%BA%A4%E6%B5%81%E4%BC%BA%E6%9C%8D%E7%94%B5%E6%9C%BA%E7%89%B9%E6%80%A7.pdf" >}}
{{< hoa-filetree/file name="实验二 - 步进电机特性" type="pdf" size="856.5 KB" date="2024/02/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2023/LJH_2023/%E5%AE%9E%E9%AA%8C%E4%BA%8C-%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA%E7%89%B9%E6%80%A7.pdf" >}}
{{< hoa-filetree/file name="实验四 - 传感与测量反馈元件特性" type="pdf" size="1.4 MB" date="2024/02/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2023/LJH_2023/%E5%AE%9E%E9%AA%8C%E5%9B%9B-%E4%BC%A0%E6%84%9F%E4%B8%8E%E6%B5%8B%E9%87%8F%E5%8F%8D%E9%A6%88%E5%85%83%E4%BB%B6%E7%89%B9%E6%80%A7.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="WJD_2023" date="" state="closed" >}}
{{< hoa-filetree/file name="210320621-吴俊达 - 交流伺服电机特性实验" type="docx" size="1.3 MB" date="2024/02/02" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2023/WJD_2023/210320621-%E5%90%B4%E4%BF%8A%E8%BE%BE-%E4%BA%A4%E6%B5%81%E4%BC%BA%E6%9C%8D%E7%94%B5%E6%9C%BA%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C.docx" >}}
{{< hoa-filetree/file name="210320621-吴俊达 - 传感与测量反馈元件特性实验" type="docx" size="811.0 KB" date="2024/02/02" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2023/WJD_2023/210320621-%E5%90%B4%E4%BF%8A%E8%BE%BE-%E4%BC%A0%E6%84%9F%E4%B8%8E%E6%B5%8B%E9%87%8F%E5%8F%8D%E9%A6%88%E5%85%83%E4%BB%B6%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C.docx" >}}
{{< hoa-filetree/file name="210320621-吴俊达 - 步进电机特性实验" type="docx" size="1.1 MB" date="2024/02/02" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2023/WJD_2023/210320621-%E5%90%B4%E4%BF%8A%E8%BE%BE-%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C.docx" >}}
{{< hoa-filetree/file name="210320621-吴俊达 - 电机 PWM 控制与驱动电路实验" type="docx" size="5.5 MB" date="2024/02/02" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2023/WJD_2023/210320621-%E5%90%B4%E4%BF%8A%E8%BE%BE-%E7%94%B5%E6%9C%BAPWM%E6%8E%A7%E5%88%B6%E4%B8%8E%E9%A9%B1%E5%8A%A8%E7%94%B5%E8%B7%AF%E5%AE%9E%E9%AA%8C.docx" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="lab manual" date="" state="closed" >}}
{{< hoa-filetree/file name="交流伺服电机特性实验指导书" type="pdf" size="7.4 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2023/lab%20manual/%E4%BA%A4%E6%B5%81%E4%BC%BA%E6%9C%8D%E7%94%B5%E6%9C%BA%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6.pdf" >}}
{{< hoa-filetree/file name="传感与测量反馈元件特性实验 2023" type="pdf" size="4.4 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2023/lab%20manual/%E4%BC%A0%E6%84%9F%E4%B8%8E%E6%B5%8B%E9%87%8F%E5%8F%8D%E9%A6%88%E5%85%83%E4%BB%B6%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C2023.pdf" >}}
{{< hoa-filetree/file name="步进电机特性实验" type="pdf" size="3.6 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2023/lab%20manual/%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C.pdf" >}}
{{< hoa-filetree/file name="电机 PWM 控制与驱动电路实验指导书" type="pdf" size="7.8 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2023/lab%20manual/%E7%94%B5%E6%9C%BAPWM%E6%8E%A7%E5%88%B6%E4%B8%8E%E9%A9%B1%E5%8A%A8%E7%94%B5%E8%B7%AF%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2024" date="" state="closed" >}}
{{< hoa-filetree/folder name="lab manual" date="" state="closed" >}}
{{< hoa-filetree/file name="lab1 步进电机特性实验" type="pdf" size="3.6 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2024/lab%20manual/lab1%20%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C.pdf" >}}
{{< hoa-filetree/file name="lab2 电机 PWM 控制与驱动电路实验" type="pdf" size="7.8 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2024/lab%20manual/lab2%20%E7%94%B5%E6%9C%BAPWM%E6%8E%A7%E5%88%B6%E4%B8%8E%E9%A9%B1%E5%8A%A8%E7%94%B5%E8%B7%AF%E5%AE%9E%E9%AA%8C.pdf" >}}
{{< hoa-filetree/file name="lab3 交流伺服电机特性实验" type="pdf" size="7.4 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2024/lab%20manual/lab3%20%E4%BA%A4%E6%B5%81%E4%BC%BA%E6%9C%8D%E7%94%B5%E6%9C%BA%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C.pdf" >}}
{{< hoa-filetree/file name="lab4 传感与测量反馈元件特性实验" type="pdf" size="4.4 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2024/lab%20manual/lab4%20%E4%BC%A0%E6%84%9F%E4%B8%8E%E6%B5%8B%E9%87%8F%E5%8F%8D%E9%A6%88%E5%85%83%E4%BB%B6%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="psp" date="" state="closed" >}}
{{< hoa-filetree/folder name="code" date="" state="closed" >}}
{{< hoa-filetree/file name="Lab1" type="m" size="2.0 KB" date="2025/01/13" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2024/psp/code/Lab1.m" >}}
{{< hoa-filetree/file name="Lab3" type="m" size="1.2 KB" date="2025/01/13" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2024/psp/code/Lab3.m" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="reports" date="" state="closed" >}}
{{< hoa-filetree/file name="Lab1 步进电机" type="docx" size="923.3 KB" date="2025/06/27" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2024/psp/reports/Lab1%20%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA.docx" >}}
{{< hoa-filetree/file name="Lab2 PWM 控制与驱动电路" type="docx" size="814.7 KB" date="2025/06/27" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2024/psp/reports/Lab2%20PWM%E6%8E%A7%E5%88%B6%E4%B8%8E%E9%A9%B1%E5%8A%A8%E7%94%B5%E8%B7%AF.docx" >}}
{{< hoa-filetree/file name="Lab3 交流伺服" type="docx" size="912.3 KB" date="2025/06/27" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2024/psp/reports/Lab3%20%E4%BA%A4%E6%B5%81%E4%BC%BA%E6%9C%8D.docx" >}}
{{< hoa-filetree/file name="Lab4 传感与反馈元件特性" type="docx" size="1.5 MB" date="2025/06/27" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/2024/psp/reports/Lab4%20%E4%BC%A0%E6%84%9F%E4%B8%8E%E5%8F%8D%E9%A6%88%E5%85%83%E4%BB%B6%E7%89%B9%E6%80%A7.docx" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="materials" date="" state="closed" >}}
{{< hoa-filetree/file name="自动控制元件习题资料" type="pdf" size="3.4 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/materials/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%85%83%E4%BB%B6%E4%B9%A0%E9%A2%98%E8%B5%84%E6%96%99.pdf" >}}
{{< hoa-filetree/file name="自动控制元件及线路课后题答案（百度文库）" type="pdf" size="1.6 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/materials/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%85%83%E4%BB%B6%E5%8F%8A%E7%BA%BF%E8%B7%AF%E8%AF%BE%E5%90%8E%E9%A2%98%E7%AD%94%E6%A1%88%EF%BC%88%E7%99%BE%E5%BA%A6%E6%96%87%E5%BA%93%EF%BC%89.pdf" >}}
{{< hoa-filetree/file name="自动控制元件教材课后题答案" type="pdf" size="17.4 MB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/materials/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%85%83%E4%BB%B6%E6%95%99%E6%9D%90%E8%AF%BE%E5%90%8E%E9%A2%98%E7%AD%94%E6%A1%88.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="notes" date="" state="closed" >}}
{{< hoa-filetree/folder name="2021_LMH" date="" state="closed" >}}
{{< hoa-filetree/file name="自控实践笔记" type="pdf" size="46.2 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/notes/2021_LMH/%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5%E7%AC%94%E8%AE%B0.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2023_WJD" date="" state="closed" >}}
{{< hoa-filetree/file name="自动控制实践 A_ 1. 磁路、直流电机 (V1.2.1)" type="pdf" size="14.5 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/notes/2023_WJD/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A_%201.%20%E7%A3%81%E8%B7%AF%E3%80%81%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%28V1.2.1%29.pdf" >}}
{{< hoa-filetree/file name="自动控制实践 A_ 2.1 电力电子技术概述" type="pdf" size="619.7 KB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/notes/2023_WJD/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A_%202.1%20%E7%94%B5%E5%8A%9B%E7%94%B5%E5%AD%90%E6%8A%80%E6%9C%AF%E6%A6%82%E8%BF%B0.pdf" >}}
{{< hoa-filetree/file name="自动控制实践 A_ 2.2 PWM" type="pdf" size="4.5 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/notes/2023_WJD/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A_%202.2%20PWM.pdf" >}}
{{< hoa-filetree/file name="自动控制实践 A_ 3. 变压器 (V1.1)" type="pdf" size="5.2 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/notes/2023_WJD/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A_%203.%20%E5%8F%98%E5%8E%8B%E5%99%A8%28V1.1%29.pdf" >}}
{{< hoa-filetree/file name="自动控制实践 A_ 4. 步进电机 (V1.1)" type="pdf" size="10.7 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/notes/2023_WJD/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A_%204.%20%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA%28V1.1%29.pdf" >}}
{{< hoa-filetree/file name="自动控制实践 A_ 5. 交流绕组、异步电机 (V1.0.1)" type="pdf" size="22.5 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/notes/2023_WJD/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A_%205.%20%E4%BA%A4%E6%B5%81%E7%BB%95%E7%BB%84%E3%80%81%E5%BC%82%E6%AD%A5%E7%94%B5%E6%9C%BA%28V1.0.1%29.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/file name="自控实践_by_Spar Océsel_2023" type="apkg" size="2.3 MB" date="2024/01/06" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/notes/%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5_by_Spar%20Oc%C3%A9sel_2023.apkg" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/file name="readme" type="toml" size="10.6 KB" date="2026/02/08" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/readme.toml" >}}
{{< hoa-filetree/folder name="slides" date="" state="closed" >}}
{{< hoa-filetree/folder name="24-psp-带笔记" date="" state="closed" >}}
{{< hoa-filetree/file name="0 绪论与磁路" type="pdf" size="2.2 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/slides/24-psp-%E5%B8%A6%E7%AC%94%E8%AE%B0/0%20%E7%BB%AA%E8%AE%BA%E4%B8%8E%E7%A3%81%E8%B7%AF.pdf" >}}
{{< hoa-filetree/file name="1 有刷直流电机" type="pdf" size="7.4 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/slides/24-psp-%E5%B8%A6%E7%AC%94%E8%AE%B0/1%20%E6%9C%89%E5%88%B7%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA.pdf" >}}
{{< hoa-filetree/file name="2 电力电子技术与 PWM" type="pdf" size="4.2 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/slides/24-psp-%E5%B8%A6%E7%AC%94%E8%AE%B0/2%20%E7%94%B5%E5%8A%9B%E7%94%B5%E5%AD%90%E6%8A%80%E6%9C%AF%E4%B8%8EPWM.pdf" >}}
{{< hoa-filetree/file name="3 变压器" type="pdf" size="1.5 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/slides/24-psp-%E5%B8%A6%E7%AC%94%E8%AE%B0/3%20%E5%8F%98%E5%8E%8B%E5%99%A8.pdf" >}}
{{< hoa-filetree/file name="4 步进电机" type="pdf" size="15.1 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/slides/24-psp-%E5%B8%A6%E7%AC%94%E8%AE%B0/4%20%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA.pdf" >}}
{{< hoa-filetree/file name="5.1 测量元件概述" type="pdf" size="6.7 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/slides/24-psp-%E5%B8%A6%E7%AC%94%E8%AE%B0/5.1%20%E6%B5%8B%E9%87%8F%E5%85%83%E4%BB%B6%E6%A6%82%E8%BF%B0.pdf" >}}
{{< hoa-filetree/file name="5.2 旋转变压器与感应同步器" type="pdf" size="10.5 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/slides/24-psp-%E5%B8%A6%E7%AC%94%E8%AE%B0/5.2%20%E6%97%8B%E8%BD%AC%E5%8F%98%E5%8E%8B%E5%99%A8%E4%B8%8E%E6%84%9F%E5%BA%94%E5%90%8C%E6%AD%A5%E5%99%A8.pdf" >}}
{{< hoa-filetree/file name="5.3 光电编码器与光栅" type="pdf" size="11.2 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/slides/24-psp-%E5%B8%A6%E7%AC%94%E8%AE%B0/5.3%20%E5%85%89%E7%94%B5%E7%BC%96%E7%A0%81%E5%99%A8%E4%B8%8E%E5%85%89%E6%A0%85.pdf" >}}
{{< hoa-filetree/file name="6 无刷直流电机和交流伺服电机" type="pdf" size="12.5 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/slides/24-psp-%E5%B8%A6%E7%AC%94%E8%AE%B0/6%20%E6%97%A0%E5%88%B7%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E5%92%8C%E4%BA%A4%E6%B5%81%E4%BC%BA%E6%9C%8D%E7%94%B5%E6%9C%BA.pdf" >}}
{{< hoa-filetree/file name="7.1 交流电机概述" type="pdf" size="7.6 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/slides/24-psp-%E5%B8%A6%E7%AC%94%E8%AE%B0/7.1%20%E4%BA%A4%E6%B5%81%E7%94%B5%E6%9C%BA%E6%A6%82%E8%BF%B0.pdf" >}}
{{< hoa-filetree/file name="7.2 交流电机的旋转磁场与感应电势" type="pdf" size="10.7 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/slides/24-psp-%E5%B8%A6%E7%AC%94%E8%AE%B0/7.2%20%E4%BA%A4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9A%84%E6%97%8B%E8%BD%AC%E7%A3%81%E5%9C%BA%E4%B8%8E%E6%84%9F%E5%BA%94%E7%94%B5%E5%8A%BF.pdf" >}}
{{< hoa-filetree/file name="7.3 异步电机的运行分析和等效电路" type="pdf" size="7.0 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/slides/24-psp-%E5%B8%A6%E7%AC%94%E8%AE%B0/7.3%20%E5%BC%82%E6%AD%A5%E7%94%B5%E6%9C%BA%E7%9A%84%E8%BF%90%E8%A1%8C%E5%88%86%E6%9E%90%E5%92%8C%E7%AD%89%E6%95%88%E7%94%B5%E8%B7%AF.pdf" >}}
{{< hoa-filetree/file name="7.4 异步电机的机械特性和调速运行" type="pdf" size="11.0 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/slides/24-psp-%E5%B8%A6%E7%AC%94%E8%AE%B0/7.4%20%E5%BC%82%E6%AD%A5%E7%94%B5%E6%9C%BA%E7%9A%84%E6%9C%BA%E6%A2%B0%E7%89%B9%E6%80%A7%E5%92%8C%E8%B0%83%E9%80%9F%E8%BF%90%E8%A1%8C.pdf" >}}
{{< hoa-filetree/file name="7.5 单相异步电机和异步电机参数" type="pdf" size="3.1 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/slides/24-psp-%E5%B8%A6%E7%AC%94%E8%AE%B0/7.5%20%E5%8D%95%E7%9B%B8%E5%BC%82%E6%AD%A5%E7%94%B5%E6%9C%BA%E5%92%8C%E5%BC%82%E6%AD%A5%E7%94%B5%E6%9C%BA%E5%8F%82%E6%95%B0.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/container >}}

## 参与

《HITSZ 自动化课程攻略共享计划》是所有同学都可以参与编写的，如果你有好的笔记或者资料，欢迎前往我们的 [GitHub](https://github.com/HITSZ-OpenAuto) 进行参与，也可以发邮件至 [📮hi@hoa.moe](mailto:hi@hoa.moe) 联系我们，我们会在收到的第一时间进行答复。

{{< callout type="" >}}
  © 版权声明：[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-nc-sa/4.0/)
{{< /callout >}}

