---
title: (必修)自动控制实践A
weight: 2
toc: true
editURL: "https://github.com/HITSZ-OpenAuto/AUTO3002A"
---
文档编写者：Oliver Wu
贡献者：

![Static Badge](https://img.shields.io/badge/%E8%80%83%E8%AF%95%E8%AF%BE-red)![Static Badge](https://img.shields.io/badge/%E5%AD%A6%E5%88%86-3-moccasin)
![Static Badge](https://img.shields.io/badge/%E6%88%90%E7%BB%A9%E6%9E%84%E6%88%90-gold)![Static Badge](https://img.shields.io/badge/%E4%BD%9C%E4%B8%9A-10%25-wheat) ![Static Badge](https://img.shields.io/badge/实验-25%25-wheat)![Static Badge](https://img.shields.io/badge/%E6%9C%9F%E6%9C%AB%E8%80%83%E8%AF%95-65%25-wheat)
## 教材、参考书、学时安排
教材：梅晓榕主编，自动控制元件及线路（第五版），科学出版社。
参考书：


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
  <td>了解即可</td>
</tr>
<tr>
  <td>步进电机的结构与工作原理</td>
  <td>1</td>
  <td>重要</td>
</tr>
<tr>
  <td>步进电机的静态特性、动态特性与驱动</td>
  <td>3</td>
  <td>重要</td>
</tr>
<tr>
  <td>交流电机概述</td>
  <td>2</td>
  <td>重要</td>
</tr>
<tr>
  <td>无刷直流电机与交流伺服电机</td>
  <td>6</td>
</tr>
<tr>
  <td>测量元件</td>
  <td>2</td>
  <td>开始起飞，大家从这里开始只要尽量听明白就行，笔记课后再做。</td>
</tr>
<tr>
  <td>三相异步电机的原理及结构</td>
  <td>2</td>
  <td>非常重要</td>
</tr>
<tr>
  <td>三相异步电机的等效电路及运行分析</td>
  <td>2</td>
  <td>非常重要</td>
</tr>
<tr>
  <td>单相异步电机的等效电路及运行分析</td>
  <td>1</td>
  <td>需要理解，有小题</td>
</tr>
<tr>
  <td>小功率同步电机</td>
  <td>0</td>
<td>考试不涉及，几乎没讲</td>
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
  - 授课风格：语速很快（因为学时有限，到后面会快到起飞）、逻辑较清晰（到后面由于速度快变得不清晰）、答疑有耐心、板书不好看、语气词较多（到后程由于速度极快，
    语气词的数量甚至会超过传递信息的词）、课件较美观
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
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/assignments/%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5%E4%BD%9C%E4%B8%9A1.pdf">assignments/自控实践作业1.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/books/%E7%94%B5%E5%AD%90%E4%B9%A6-%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%85%83%E4%BB%B6%E5%8F%8A%E7%BA%BF%E8%B7%AF.pdf">books/电子书-自动控制元件及线路.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/exams/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5%E5%8E%86%E5%B9%B4%E8%80%83%E9%A2%98.pdf">exams/自动控制实践历年考题.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A-%E5%AE%9E%E9%AA%8C1.pdf">labs/实验报告-实验1.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A-%E5%AE%9E%E9%AA%8C2.pdf">labs/实验报告-实验2.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A-%E5%AE%9E%E9%AA%8C3.pdf">labs/实验报告-实验3.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/labs/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A-%E5%AE%9E%E9%AA%8C4.pdf">labs/实验报告-实验4.pdf</a>
<br>
<a href="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002A/raw/main/notes/%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5%E7%AC%94%E8%AE%B0.pdf">notes/自控实践笔记.pdf</a>
<br>
<br>


## 支持我们

如果你喜欢 HITSZ 自动化课程攻略共享计划，想支持我们，以下是几种支持我们的方式:

- HITSZ 自动化课程攻略共享计划 是所有同学都可以参与编写贡献的，如果你有好的笔记或者资料，欢迎前往我们的[GitHub](https://github.com/HITSZ-OpenAuto)进行贡献，也可以发邮件至[📮hi@hoa.moe](mailto:hi@hoa.moe)联系我们，我们会在收到的第一时间进行答复。

- 将本网站分享给你的同学也是支持我们的重要方式。

- 如果您认为本页面提供的信息对您有帮助，请考虑捐赠 ¥2 给我们。每一份慷慨支持都将大幅减轻我们承担的域名及对象存储服务的费用负担。我们鼓励选择“向对方展示我的名字”，你的ID和留言将会显示在我们的[Sponsor](https://hoa.moe/sponsor/)页面中。

<br>
<img src="https://mitcher-1316637614.cos.ap-nanjing.myqcloud.com/hoa/20231112170457.png?imageSlim" alt="Reward_Code" style="zoom:25%; display: block; margin: 0 auto;" />