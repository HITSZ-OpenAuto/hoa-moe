---
title: (必修)自动控制实践A
weight: 2
toc: true
editURL: "https://github.com/HITSZ-OpenAuto/AUTO3002A"
---
**new: 步进电机笔记&答案更新**

文档编写者：[Oliver Wu](https://github.com/OliverWu515)（撰写有关21级部分）

![Static Badge](https://img.shields.io/badge/%E8%80%83%E8%AF%95%E8%AF%BE-red)![Static Badge](https://img.shields.io/badge/%E5%AD%A6%E5%88%86-3-moccasin)

![Static Badge](https://img.shields.io/badge/%E6%88%90%E7%BB%A9%E6%9E%84%E6%88%90（21级）-gold)![Static Badge](https://img.shields.io/badge/%E4%BD%9C%E4%B8%9A-10%25-wheat) ![Static Badge](https://img.shields.io/badge/实验-25%25-wheat)![Static Badge](https://img.shields.io/badge/%E6%9C%9F%E6%9C%AB%E8%80%83%E8%AF%95-65%25-wheat)

![Static Badge](https://img.shields.io/badge/总学时48-wheat) ![Static Badge](https://img.shields.io/badge/讲课学时-40-wheat) ![Static Badge](https://img.shields.io/badge/实验-2学时*4-wheat)

该课程有配套的课程设计（[(必修)自动控制实践A课程设计](https://hoa.moe/docs/junior-autumn/auto3016/)），独立设课，1学分、40学时。

## 教材、参考书、学时安排

教材：梅晓榕主编，自动控制元件及线路（第五版），科学出版社。

参考书及网课：

本课程涵盖三部分内容：电机驱动与拖动；传感与测量元件；简单的电力电子技术（PWM）。以第一块内容为最重。

电机学：

- （哈尔滨理工大学）戈宝军,梁艳萍,温嘉斌，电机学（第三版），中国电力出版社。

  配套网课：[电机学（哈尔滨理工大学）bilibili](https://www.bilibili.com/video/BV1cx411Z76w/?spm_id_from=333.337.search-card.all.click)

- （哈尔滨理工大学）汤蕴璆编著，电机学（第5版），机械工业出版社。

- （大连理工大学）孙建忠、刘凤春等编，电机与拖动（第4版），机械工业出版社。

上面的是传统电机学教材，可以看里面的直流电机、变压器、异步电机和同步电机。关于伺服电机和步进电机，可以参考以下书目：

- [日]坂本正文著，王自强译，步进电机应用技术，科学出版社2010年版。（翻译有些错误，凑合着看）
- （一些奇怪的论坛里的pdf，找到后放上来）

关于电力电子技术，本门课要求很低。如果大家想拓展（学电气的专业课[bushi]），可以参考的书目有：（请大家量力而行，学有余力再去看拓展提高的内容！）

- （西安交通大学）王兆安等，电力电子技术（第5版），机械工业出版社。
- Erickson，Fundamental of power electronics（3rd ed.)，Springer。
- https://space.bilibili.com/519909115
- [西瓜粥西瓜粥的个人空间-西瓜粥西瓜粥个人主页-哔哩哔哩视频 (bilibili.com)](https://space.bilibili.com/287344644?spm_id_from=333.337.search-card.all.click)

<h4>学时安排表（21级）</h4>   <!--标题-->
<table border="1" cellspacing="10">
<tr>
  <th align="center">授课教师</th>
  <th align="center">授课内容</th>
  <th align="center">学时安排</th>
  <th align="center">建议</th>
</tr>
<tr>
  <td rowspan="10" align="center">Long Zhili</td>
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
  <td>很重要，需要理解一个周期PWM元件上的电流流向、导通关断与否以及元件的作用。</td>
</tr>
<tr>
  <td>变压器</td>
  <td>2</td>
  <td>很重要，学时很少，要记忆的东西却很多。重点在负载运行和空载运行的基本方程和T形等效电路。笔记文件夹里的笔记整理得很清楚。</td>
</tr>
<tr>
  <td rowspan="10" align="center">Li Jiangang</td>
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
  <td>讲得最细致的部分，但其实原理相对比较简单，重点理解六步换向和Clark-Park/d-q变换，理解如何将伺服电机的驱动变得像有刷直流那样简单。</td>
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
  <td>约2.5</td>
  <td>是重点，也是难点！！但是你没看错，2学时结束了。等效的流程：电路模型-频率归算-绕组归算。<b>异步电机可以看成“会动的变压器”！</b> 详见文件中的异步电机笔记。</td>
</tr>
<tr>
  <td>单相异步电机的等效电路及运行分析</td>
  <td>约0.5</td>
  <td>需要理解，有小题。</td>
</tr>
<tr>
  <td>小功率同步电机</td>
  <td>0</td>
<td>没时间了，几乎没讲，考试不涉及。</td>
</tr>
</table>


<!--在表格td中，有两个属性控制居中显示
	align——表示左右居中——left，center，right
	valign——控制上下居中——left，center，right
	width——控制单元格宽度，单位像素
	cellspacing——单元格之间的间隔，单位像素
-->

## 授课教师

（21级情况）

- 教师1：Long Zhili
  - 授课风格：稍显含糊，车轱辘话较多；课件内容较丰富，有别学校课件截下来的内容，不过画质较差，而且比较乱，不适合直接做笔记。
  - 听课建议：基本忠于ppt（不会自由发挥），由于车轱辘话较多，知识讲解得比较抽象，上课不易听懂，课后要多花时间。
- 教师2：Li Jiangang
  - 授课风格：语速很快（因为学时有限、内容又多，到后面会快到起飞）、逻辑较清晰（到后面由于速度快变得不清晰）、答疑有耐心、板书不好看、语气词较多（到后程由于速度极快，
    语气词的数量甚至会超过传递信息的词）、课件较美观（但是由于摘选自外校课件，有时会出现符号的冲突或逻辑不连贯）。
  - 听课建议：因为上课节奏较快，上课只求听懂大概即可，但课后务必整理笔记！！！

## 关于考试

- 考试难度：

## Tips

## 课程建议
<br>
<br>
<br>


## 资料下载

<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/ACPP_HW1.pdf">assignments/ACPP_HW1.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/ACPP_HW2.pdf">assignments/ACPP_HW2.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/ACPP_HW3.pdf">assignments/ACPP_HW3.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%85%83%E4%BB%B6%E6%95%99%E6%9D%90%E8%AF%BE%E5%90%8E%E9%A2%98%E7%AD%94%E6%A1%88.pdf">assignments/自动控制元件教材课后题答案.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5%E4%BD%9C%E4%B8%9A3.pdf">assignments/自控实践作业3.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/books/%E7%94%B5%E5%AD%90%E4%B9%A6-%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%85%83%E4%BB%B6%E5%8F%8A%E7%BA%BF%E8%B7%AF.pdf">books/电子书-自动控制元件及线路.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/1%20%E7%BB%AA%E8%AE%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx">exams/本部-试题汇编/1 绪论相关试题 - 答案.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/1%20%E7%BB%AA%E8%AE%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx">exams/本部-试题汇编/1 绪论相关试题.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/10%20%E5%8F%98%E5%8E%8B%E5%99%A8%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx">exams/本部-试题汇编/10 变压器相关试题 - 答案.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/10%20%E5%8F%98%E5%8E%8B%E5%99%A8%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx">exams/本部-试题汇编/10 变压器相关试题.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/13%20%E5%BC%82%E6%AD%A5%E7%94%B5%E6%9C%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx">exams/本部-试题汇编/13 异步电机相关试题 - 答案.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/13%20%E5%BC%82%E6%AD%A5%E7%94%B5%E6%9C%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx">exams/本部-试题汇编/13 异步电机相关试题.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/14%20%E5%B0%8F%E5%8A%9F%E7%8E%87%E5%90%8C%E6%AD%A5%E7%94%B5%E6%9C%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx">exams/本部-试题汇编/14 小功率同步电机相关试题.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/15%20%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20-%20%E7%AD%94%E6%A1%88%28%E6%9B%B4%E6%96%B0%29.docx">exams/本部-试题汇编/15 步进电机相关试题 - 答案(更新).docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/15%20%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx">exams/本部-试题汇编/15 步进电机相关试题.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/16%20%E6%97%A0%E5%88%B7%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx">exams/本部-试题汇编/16 无刷直流电机相关试题 - 答案.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/16%20%E6%97%A0%E5%88%B7%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx">exams/本部-试题汇编/16 无刷直流电机相关试题.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/2%20%E7%A3%81%E8%B7%AF%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E7%9B%B8%E5%85%B3%E4%BE%8B%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx">exams/本部-试题汇编/2 磁路基础知识相关例题 - 答案.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/2%20%E7%A3%81%E8%B7%AF%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E7%9B%B8%E5%85%B3%E4%BE%8B%E9%A2%98.docx">exams/本部-试题汇编/2 磁路基础知识相关例题.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/22%20%E6%B5%8B%E9%87%8F%E5%85%83%E4%BB%B6%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20%20-%20%E7%AD%94%E6%A1%88.docx">exams/本部-试题汇编/22 测量元件相关试题  - 答案.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/22%20%E6%B5%8B%E9%87%8F%E5%85%83%E4%BB%B6%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20.docx">exams/本部-试题汇编/22 测量元件相关试题 .docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/3%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9A%84%E5%8E%9F%E7%90%86%E4%B8%8E%E5%9F%BA%E6%9C%AC%E7%BB%93%E6%9E%84%E7%9B%B8%E5%85%B3%E4%BE%8B%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx">exams/本部-试题汇编/3 直流电机的原理与基本结构相关例题 - 答案.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/3%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9A%84%E5%8E%9F%E7%90%86%E4%B8%8E%E5%9F%BA%E6%9C%AC%E7%BB%93%E6%9E%84%E7%9B%B8%E5%85%B3%E4%BE%8B%E9%A2%98.docx">exams/本部-试题汇编/3 直流电机的原理与基本结构相关例题.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/4%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9A%84%E7%89%B9%E6%80%A7%E4%B8%8E%E6%8E%A7%E5%88%B6%E6%96%B9%E6%B3%95%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx">exams/本部-试题汇编/4 直流电机的特性与控制方法相关试题 - 答案.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/4%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9A%84%E7%89%B9%E6%80%A7%E4%B8%8E%E6%8E%A7%E5%88%B6%E6%96%B9%E6%B3%95%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx">exams/本部-试题汇编/4 直流电机的特性与控制方法相关试题.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/5%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9A%84%E5%8A%A8%E7%89%B9%E6%80%A7%E4%B8%8E%E9%80%89%E6%8B%A9%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx">exams/本部-试题汇编/5 直流电机的动特性与选择相关试题 - 答案.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/5%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%9A%84%E5%8A%A8%E7%89%B9%E6%80%A7%E4%B8%8E%E9%80%89%E6%8B%A9%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx">exams/本部-试题汇编/5 直流电机的动特性与选择相关试题.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/9%20%E5%8A%9F%E7%8E%87%E6%94%BE%E5%A4%A7%E5%99%A8%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98%20-%20%E7%AD%94%E6%A1%88.docx">exams/本部-试题汇编/9 功率放大器相关试题 - 答案.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E6%9C%AC%E9%83%A8-%E8%AF%95%E9%A2%98%E6%B1%87%E7%BC%96/9%20%E5%8A%9F%E7%8E%87%E6%94%BE%E5%A4%A7%E5%99%A8%E7%9B%B8%E5%85%B3%E8%AF%95%E9%A2%98.docx">exams/本部-试题汇编/9 功率放大器相关试题.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%85%83%E4%BB%B62012%E6%9C%9F%E6%9C%AB%E8%AF%95%E5%8D%B7.pdf">exams/自动控制元件2012期末试卷.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%85%83%E4%BB%B62019%E7%A7%8B%E6%9C%9F%E6%9C%AB%E8%AF%95%E5%8D%B7.pdf">exams/自动控制元件2019秋期末试卷.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%85%83%E4%BB%B62020%E7%A7%8B%E6%9C%9F%E6%9C%AB%E8%AF%95%E5%8D%B7.pdf">exams/自动控制元件2020秋期末试卷.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5%E5%8E%86%E5%B9%B4%E8%80%83%E9%A2%98.pdf">exams/自动控制实践历年考题.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/LMH_VERSION_2021/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A-%E5%AE%9E%E9%AA%8C1.pdf">labs/LMH_VERSION_2021/实验报告-实验1.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/LMH_VERSION_2021/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A-%E5%AE%9E%E9%AA%8C2.pdf">labs/LMH_VERSION_2021/实验报告-实验2.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/LMH_VERSION_2021/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A-%E5%AE%9E%E9%AA%8C3.pdf">labs/LMH_VERSION_2021/实验报告-实验3.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/LMH_VERSION_2021/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A-%E5%AE%9E%E9%AA%8C4.pdf">labs/LMH_VERSION_2021/实验报告-实验4.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/WJD_VERSION_2023/210320621-%E5%90%B4%E4%BF%8A%E8%BE%BE-%E4%BA%A4%E6%B5%81%E4%BC%BA%E6%9C%8D%E7%94%B5%E6%9C%BA%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C.docx">labs/WJD_VERSION_2023/210320621-吴俊达-交流伺服电机特性实验.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/WJD_VERSION_2023/210320621-%E5%90%B4%E4%BF%8A%E8%BE%BE-%E4%BC%A0%E6%84%9F%E4%B8%8E%E6%B5%8B%E9%87%8F%E5%8F%8D%E9%A6%88%E5%85%83%E4%BB%B6%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C.docx">labs/WJD_VERSION_2023/210320621-吴俊达-传感与测量反馈元件特性实验.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/WJD_VERSION_2023/210320621-%E5%90%B4%E4%BF%8A%E8%BE%BE-%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C.docx">labs/WJD_VERSION_2023/210320621-吴俊达-步进电机特性实验.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/WJD_VERSION_2023/210320621-%E5%90%B4%E4%BF%8A%E8%BE%BE-%E7%94%B5%E6%9C%BAPWM%E6%8E%A7%E5%88%B6%E4%B8%8E%E9%A9%B1%E5%8A%A8%E7%94%B5%E8%B7%AF%E5%AE%9E%E9%AA%8C.docx">labs/WJD_VERSION_2023/210320621-吴俊达-电机PWM控制与驱动电路实验.docx</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/WJD_VERSION_2023/%E4%BA%A4%E6%B5%81%E4%BC%BA%E6%9C%8D%E7%94%B5%E6%9C%BA%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6.pdf">labs/WJD_VERSION_2023/交流伺服电机特性实验指导书.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/WJD_VERSION_2023/%E4%BC%A0%E6%84%9F%E4%B8%8E%E6%B5%8B%E9%87%8F%E5%8F%8D%E9%A6%88%E5%85%83%E4%BB%B6%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C2023.pdf">labs/WJD_VERSION_2023/传感与测量反馈元件特性实验2023.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/WJD_VERSION_2023/%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA%E7%89%B9%E6%80%A7%E5%AE%9E%E9%AA%8C.pdf">labs/WJD_VERSION_2023/步进电机特性实验.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/WJD_VERSION_2023/%E7%94%B5%E6%9C%BAPWM%E6%8E%A7%E5%88%B6%E4%B8%8E%E9%A9%B1%E5%8A%A8%E7%94%B5%E8%B7%AF%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6.pdf">labs/WJD_VERSION_2023/电机PWM控制与驱动电路实验指导书.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/notes/LMH_VERSION/%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5%E7%AC%94%E8%AE%B0.pdf">notes/LMH_VERSION/自控实践笔记.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/notes/WJD_VERSION/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A_%201.%20%E7%A3%81%E8%B7%AF%E3%80%81%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%28V1.1%29.pdf">notes/WJD_VERSION/自动控制实践A_ 1. 磁路、直流电机(V1.1).pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/notes/WJD_VERSION/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A_%203.%20%E5%8F%98%E5%8E%8B%E5%99%A8%28V1.1%29.pdf">notes/WJD_VERSION/自动控制实践A_ 3. 变压器(V1.1).pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/notes/WJD_VERSION/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A_%204.%20%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA%28V1.0%29.pdf">notes/WJD_VERSION/自动控制实践A_ 4. 步进电机(V1.0).pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/notes/WJD_VERSION/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5A_%205.%20%E4%BA%A4%E6%B5%81%E7%BB%95%E7%BB%84%E3%80%81%E5%BC%82%E6%AD%A5%E7%94%B5%E6%9C%BA%28V1.0%29.pdf">notes/WJD_VERSION/自动控制实践A_ 5. 交流绕组、异步电机(V1.0).pdf</a>
<br>
<br>


## 支持我们

如果你喜欢 HITSZ 自动化课程攻略共享计划，想支持我们，以下是几种支持我们的方式:

- HITSZ 自动化课程攻略共享计划 是所有同学都可以参与编写贡献的，如果你有好的笔记或者资料，欢迎前往我们的[GitHub](https://github.com/HITSZ-OpenAuto)进行贡献，也可以发邮件至[📮hi@hoa.moe](mailto:hi@hoa.moe)联系我们，我们会在收到的第一时间进行答复。

- 将本网站分享给你的同学也是支持我们的重要方式。

- 如果您认为本页面提供的信息对您有帮助，请考虑捐赠 ¥2 给我们。每一份慷慨支持都将大幅减轻我们承担的域名及对象存储服务的费用负担。我们鼓励选择“向对方展示我的名字”，你的ID和留言将会显示在我们的[Sponsor](https://hoa.moe/sponsor/)页面中。

<br>
<img src="https://mitcher-1316637614.cos.ap-nanjing.myqcloud.com/hoa/20231112170457.png?imageSlim" alt="Reward_Code" style="zoom:25%; display: block; margin: 0 auto;" />