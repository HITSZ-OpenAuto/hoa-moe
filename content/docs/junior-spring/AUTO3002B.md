---
title: （必修）自动控制实践 B
weight: 10
toc: true
editURL: "https://github.com/HITSZ-OpenAuto/AUTO3002B/edit/main/README.md"
math: true
---

{{< update-info update_time="2026 年 1 月 21 日" author="Hye" message="调整 README 结构，删去了 tabs 组件，修复页面构建的问题。 (#28)" >}}

<div class="hoa-badge">

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

本部相关课程：**《智能系统控制实践》**。

<div class="hoa-badge">

![Static Badge](https://img.shields.io/badge/%E8%80%83%E8%AF%95%E8%AF%BE-red)![Static Badge](https://img.shields.io/badge/%E5%AD%A6%E5%88%86（23%E7%BA%A7）-5.5-moccasin)

![Static Badge](https://img.shields.io/badge/%E6%88%90%E7%BB%A9%E6%9E%84%E6%88%90（23%E7%BA%A7）-gold)
![Static Badge](https://img.shields.io/badge/%E4%BD%9C%E4%B8%9A-10%25-wheat)
![Static Badge](https://img.shields.io/badge/%E5%AE%9E%E9%AA%8C-30%25-wheat)
![Static Badge](https://img.shields.io/badge/%E6%9C%9F%E6%9C%AB%E8%80%83%E8%AF%95-60%25-wheat)

![Static Badge](https://img.shields.io/badge/%E5%AD%A6%E6%97%B6%E5%AE%89%E6%8E%92（23%E7%BA%A7）-gold)
![Static Badge](https://img.shields.io/badge/%E6%80%BB%E5%AD%A6%E6%97%B6-88-wheat)
![Static Badge](https://img.shields.io/badge/%E6%8E%88%E8%AF%BE-56-wheat)
![Static Badge](https://img.shields.io/badge/%E5%AE%9E%E9%AA%8C-32-wheat)

</div>

本课程为校本部未来技术学院自动化、探测制导与控制技术、智能装备与系统及相关专业本科生的必修课程。

注意，该课程为哈工大本部/深圳的考研复试课程。

## 教材及参考书

- （深圳 + 本部）王广雄、何朕，控制系统设计，清华大学出版社。
- （本部）梅晓榕主编，自动控制元件及线路（第五版），科学出版社。
- （本部）丛爽，智能控制系统及应用，中国科学技术大学出版社。

## 授课教师

- 理论课：董广忠
  - 授课风格：通过加入密度极高的无意义衬词以及含糊其辞的表述，成功达到让人听不懂的效果。答疑态度十分一般。
  - 听课建议：不考勤。上课会提示重点，建议课后倍速听回放。课件在教师主页，不在 qq 群发放。

> 文 / [Oliver Wu](https://github.com/oliverwu515)

- 实验课：王彬彬、刘瑞
  - 如遇到问题，建议自行 Google。

<!-- 下为本部情况 -->

- （本部）理论课：马克茂
  - 授课风格：讲课节奏十分奇怪，课件内容较其他老师相对更少。
  - 听课建议：不考勤。课前会发放 PPT 和作业题，建议基于作业加以预习，事半功倍。
- （本部）理论课：霍鑫
  - 授课风格：讲课生动有趣，课件内容丰富，非常精美。历年风评极佳。
  - 听课建议：考勤情况未知。上课会提示重点。有课程后半部分的讲解视频 [自动控制实践第十九讲 (1)_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1x54y1Z7To/) 。

> 文 / [Costannt](https://github.com/Costannt)，2026.1

- （本部）实验课：姜宇
  - 答疑态度非常一般，但实验给分相对宽松。

> 文 / [Costannt](https://github.com/Costannt)，2026.1

## 关于考试

### 深圳校区情况

- 考试难度：较难
- 说明：注意老师给出的重点。同时对于理论部分的学习主要是一些固定的模型，注意公式推导和转换即可。实践部分听重点，过一遍 PPT 即可。

> 文 / [xander-2077](https://github.com/xander-2077)

- 主要是大背诵。

> 文 / [Oliver Wu](https://github.com/oliverwu515)

从回忆卷子就可以看出，25 年的考试如往常一样的大背诵，我考试时不到一个小时手就写酸了。不过虽然老师上课的时候讲了很多次题目会完全重新出，但是实际上（除了那一道 Anti Windup 简答题）大部分题目还都是原题，甚至最后一道设计大题完完全全没有变化，因此只要把往年题都做做好，考试的时候就不会有太大问题。

虽然听大家多会抱怨这门课，我个人觉得这门课在逻辑性和知识点密度上还是很不错的（相比自控实践 A 好了不是一点半点），大部分问题估计就是学生和老师之间沟通不够及时，很多问题没法有效解决，因此我写了往年题目的详解并放在 exams 文件夹下，供大家参考，大家做题时可以多和同学们交流，大部分情况都只能将大多数人认同的答案作为参考。

> 文 / [psp_dada](https://github.com/pspdada), 2025.6

### 本部情况

- 考试难度：较难
- 超级大背诵。

{{% details title="[Costannt](https://github.com/Costannt)认为的重点" closed="true"%}}

- 对元件部分的要求是：

  - 应该了解直流电机、三相交流异步电机的几个重要公式及其调速方法；
  - 若干种测量元件的工作原理及其各类指标的计算方法；
  - 本课程涉及的各种元件的优缺点和注意事项等。

- 对设计部分的要求是：

  - 能够背诵控制系统设计的完整流程，并指出流程中各步骤的作用；

  - 能够理解并正确在设计中应用输入信号分析的结果。注意，DFT / FFT 的计算并非此处重点；

  - 能够正确推导和使用静态、动态误差系数法；能够理解并运用课程讲解的所有动态误差系数求取方法；能够理解并背诵两种误差系数的关系；能够理解并背诵各种跟踪误差计算方法的优缺点；

  - 能够理解噪声是一种随机过程；能理解并背诵谱密度与样本函数、相关函数的关系；能理解并背诵均方误差和等效噪声带宽定义及其设计原则。

    是否需要熟练掌握有关计算方法，请询任课老师。

  - 能够理解并背诵课程讲解的全部误差抑制方法及其适用范围、优缺点和注意事项。特别是扰动观测器中低通滤波器的设计。

  - 能够理解并计算灵敏度函数，背诵课程给出的灵敏度函数；能够理解 Bode 积分定理的约束及有关易错点；能够理解并背诵对象不确定性的定义及其产生原因；能够理解并背诵、推导鲁棒稳定性条件；能够理解并背诵系统的响应特性和反馈特性及其重要性；能够理解并背诵、推导机械谐振的自由转子模型，了解其与系统带宽的关系和谐振的抑制方法；能够理解并背诵、运用带宽的设计思想和方法及有关注意事项。

  - 能够理解 windup 现象及其出现的原因；能够理解并背诵 Anti-windup 设计思想；能够理解并应用课程讲解的全部设计方法改造控制器。

  - 能够理解并背诵伺服系统的定义、特点及其基本特性；能够理解并应用课程讲解的所有校正方法来设计满足要求的伺服系统。

  - 能够理解并背诵调节系统的定义、特点及其基本特性；能够理解并背诵调节系统的控制规律设计原则；能够理解过程控制系统的设计特点及其形成原因；能够理解并背诵过程控制系统整定方法。

  - 能够理解并背诵单回路设计矛盾、多回路设计优缺点及其设计原则；能够应用有关知识设计一个多回路系统；能够理解串级调节系统的特点；能够理解复合控制系统的作用

- 对智能控制部分的要求是：

  - 关于专家控制，课程讲解、考试和作业中完全未涉及，因此未知其考察重点。*请注意，此为 23 级情况*
  - 能够理解并背诵模糊控制的优缺点；能够理解并背诵模糊控制的流程；理解模糊控制的关键。{{% /details %}}

> 文 / [Costannt](https://github.com/Costannt)，2026.1

## 关于授课内容

### 本部情况

> 以下为本部课程《智能系统控制实践》23 级情况。

具体参见当年的「智能系统控制实践 - 课程教学大纲」

{{% details title="理论授课（56 学时）"closed="true" %}}

- 绪论（2 学时）
  - 掌握控制系统的基本组成、控制元件在控制系统中的作用、基本要求与指标；
  - 掌握控制系统模拟、数字、总线等接口；
  - 了解控制系统发展历史，把握发展脉络，预测未来发展趋势，明确控制系统的当前的主要研究内容；
  - 明确课程任务及考核方式。
- 直流电机原理（2 学时）
  - 掌握直流电机的工作原理、直流电机的基本结构；
  - 掌握直流电机的基本关系式；
  - 掌握直流电机的铭牌和额定值。
- 直流电机特性及选型（2 学时）
  - 掌握直流电机的静态特性和动态特性；
  - 掌握直流电机的控制方法和调节特性；
  - 掌握直流伺服电机特点与应用；
  - 掌握直流电动机的选择原理与应用。
- 交流同步电机原理及特性（2 学时）
  - 掌握交流电机的旋转磁场；
  - 掌握同步电机的结构与工作原理；
  - 掌握同步电机的机械特性。
- 感应电机及步进电机原理及特性（2 学时）
  - 掌握感应电机的结构与工作原理；
  - 掌握步进电机的结构与工作原理。
- 传感器（2 学时）
  - 掌握测量元件的基本要求；
  - 掌握编码器的结构与工作原理；
  - 掌握光栅的结构与工作原理。
- 控制系统设计流程（2 学时）
  - 掌握控制系统设计的主要内容，关键要素，基本流程，所涉及的学科和知识，以及对控制工程师的基本能力要求。
- 典型输入信号（2 学时）
  - 掌握控制系统性能需求分析方法；
  - 典型输入信号确定方法；
  - 典型输入信号的特性分析、傅里叶分析。
- 静态误差及控制方法（2 学时）
  - 掌握控制系统误差公式，误差系数计算方法；
  - 分析影响误差的主要因素；
  - 掌握减小静态误差的控制方法。
- 动态误差分析及控制方法（2 学时）
  - 掌握动态误差系数计算方法；
  - 掌握影响动态误差的主要因素；
  - 掌握动态跟踪误差的方法。
- 噪声及其引起的误差（4 学时）
  - 掌握噪声的定义、特性、作用点和作用机理；
  - 掌握噪声描述方法、噪声的危害、噪声的抑制方法及其评价指标等。
- 干扰及其抑制方法（4 学时）
  - 掌握干扰的定义，特性、作用点、作用机理，以及与噪声的区别；
  - 掌握干扰分类方法以及各种干扰抑制方法以及特点、适用范围等。
- 干扰观测器设计（2 学时）
  - 掌握干扰观测器设计结构及组成；
  - 掌握干扰观测器的参数设计原则；
  - 掌握应用干扰观测器实现干扰补偿的实现方法。
- 控制系统不确定性的设计约束（2 学时）
  - 掌握不确定性的概念、来源及其对系统的影响；
  - 掌握不确定性的描述方法，以及不确定性界的求取方法；
  - 掌握鲁棒稳定性定理给控制系统设计带来的约束。
- 控制系统的带宽设计约束（4 学时）
  - 理解控制系统的带宽的定义，具体指标、设计原则；
  - 掌握各种压低带宽和拓展带宽的各种方法及适用条件和副作用。
- 控制系统的抗饱和设计（2 学时）
  - 掌握系统饱和的原因、现象和危害，以及饱和环节的描述方法；
  - 掌握 PI 控制器的抗饱和方法，还有一般的控制器抗饱和方法。
- 伺服系统（4 学时）
  - 掌握伺服系统的定义、特点和模型描述方法；
  - 掌握基本 I 型和改进 I 的设计方法；
  - 案例分析。
- 调节系统（4 学时）
  - 掌握调节系统的定义，特点和模型描述方法；
  - 掌握调节系统的 PID 控制器设计的几种方法。
- 多回路控制设计（4 学时）
  - 掌握多回路的基本概念，结构和类型；
  - 掌握多回路控制设计要解决的问题，以及具体的设计原则和方法。
- 专家控制及应用（2 学时）
  - 掌握智能系统控制特点；
  - 掌握专家控制基本方法；
  - 掌握专家控制应用特点。
- 模糊控制及应用（4 学时）
  - 掌握模糊控制的基本原理；
  - 掌握模糊控制器的设计方法；
  - 掌握模糊控制器应用方法。{{% /details %}}

{{% details title="实验" closed="true"%}}

{{% details title="实物实验" closed="true"%}}

- 实验一：电机位置伺服系统模型辨识（4 学时）
  - 掌握电机位置伺服系统被控对象频率特性测试方法；
  - 掌握电机位置伺服系统被控对象传递函数模型辨识方法。
- 实验二：电机位置伺服系统频域控制器实验验证（4 学时）
  - 掌握电机位置伺服系统频域校正实现方法；
  - 掌握闭环伺服系统性能测试实现方法。
- 实验三：电机位置伺服系统 PID+ 干扰观测器控制器设计与仿真验证（4 学时）
  - 掌握伺服系统中干扰对系统性能影响；
  - 掌握扰动响应的测试方法；
  - 掌握干扰观测器设计的实现方法。
- 实验四：电机位置伺服系统多回路控制器实验验证（4 学时）
  - 掌握电机位置伺服系统角位置、角速度、电流等多回路控制系统实现方式；
  - 掌握多回路设计、调试准则；
  - 掌握多回路性能测试的工程实现。{{% /details %}}

{{% details title="仿真实验" closed="true"%}}

- 实验五：倒立摆的模糊自适应 PID 控制器设计（8 学时）
  - 掌握倒立摆的建模仿真；
  - 掌握倒立摆系统的不确定性分析；
  - 掌握模糊自适应 PID 控制器的实现；
  - 控制系统性能的影响因素分析。

- 实验六：伺服系统模糊控制设计与分析（8 学时）
  - 伺服系统的建模仿真；
  - 构建伺服系统的模糊推理规则；
  - 设计模糊控制器；
  - 系统调试；
  - 实现模糊控制系统的参数优化。{{% /details %}} {{% /details %}}

> 文 / [Costannt](https://github.com/Costannt)，2026.1

## 关于作业

### 本部情况

- 布置频率较低，主要集中在控制系统设计部分。
- 马克茂老师的作业风格类似考试习题，因此特别建议基于作业问题进行预习并认真完成。
- 霍鑫老师的作业主要为各种仿真实验。

> 文 / [Costannt](https://github.com/Costannt)，2026.1

## 学习建议

### 来自本部

- 请认真看书。

  由于本课的大背诵特质，老师课上提出的、作业中给出的很多难度较大的问题往往想不出来，如果课上老师未讲解，PPT 上也未记录，此时推荐仔细读书，很可能得到答案。

- 请不要钻牛角尖。

  由于本课的大背诵特质，课程中很多内容（如：直流电机特性方程的推导、DFT / FFT 的计算）是不要求掌握的，请量力而行。

> 文 / [Costannt](https://github.com/Costannt)，2026.1

## 资料下载

如果你是校内学生，可点击如下「内网网盘」按钮查看本门课程的电子书、课件和实验软件等。

{{< hoa-filetree/container driveURL="https://open.osa.moe/openauto/AUTO3002B" repoURL="https://github.com/HITSZ-OpenAuto/AUTO3002B" >}}
{{< hoa-filetree/folder name="assignments" date="" state="closed" >}}
{{< hoa-filetree/folder name="本部" date="" state="closed" >}}
{{< hoa-filetree/folder name="2025" date="" state="closed" >}}
{{< hoa-filetree/folder name="Costannt 解答" date="" state="closed" >}}
{{< hoa-filetree/file name="作业 1" type="pdf" size="390.4 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/Costannt%E8%A7%A3%E7%AD%94/%E4%BD%9C%E4%B8%9A1.pdf" >}}
{{< hoa-filetree/file name="作业 10" type="pdf" size="583.2 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/Costannt%E8%A7%A3%E7%AD%94/%E4%BD%9C%E4%B8%9A10.pdf" >}}
{{< hoa-filetree/file name="作业 2" type="pdf" size="763.3 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/Costannt%E8%A7%A3%E7%AD%94/%E4%BD%9C%E4%B8%9A2.pdf" >}}
{{< hoa-filetree/file name="作业 3" type="pdf" size="2.8 MB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/Costannt%E8%A7%A3%E7%AD%94/%E4%BD%9C%E4%B8%9A3.pdf" >}}
{{< hoa-filetree/file name="作业 4" type="pdf" size="1.0 MB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/Costannt%E8%A7%A3%E7%AD%94/%E4%BD%9C%E4%B8%9A4.pdf" >}}
{{< hoa-filetree/file name="作业 5" type="pdf" size="454.0 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/Costannt%E8%A7%A3%E7%AD%94/%E4%BD%9C%E4%B8%9A5.pdf" >}}
{{< hoa-filetree/file name="作业 6" type="pdf" size="341.4 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/Costannt%E8%A7%A3%E7%AD%94/%E4%BD%9C%E4%B8%9A6.pdf" >}}
{{< hoa-filetree/file name="作业 7" type="pdf" size="611.6 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/Costannt%E8%A7%A3%E7%AD%94/%E4%BD%9C%E4%B8%9A7.pdf" >}}
{{< hoa-filetree/file name="作业 8" type="pdf" size="462.0 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/Costannt%E8%A7%A3%E7%AD%94/%E4%BD%9C%E4%B8%9A8.pdf" >}}
{{< hoa-filetree/file name="作业 9" type="pdf" size="86.1 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/Costannt%E8%A7%A3%E7%AD%94/%E4%BD%9C%E4%B8%9A9.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="马克茂老师作业题" date="" state="closed" >}}
{{< hoa-filetree/file name="HW1" type="pdf" size="277.7 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/%E9%A9%AC%E5%85%8B%E8%8C%82%E8%80%81%E5%B8%88%E4%BD%9C%E4%B8%9A%E9%A2%98/HW1.pdf" >}}
{{< hoa-filetree/file name="HW10" type="pdf" size="425.2 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/%E9%A9%AC%E5%85%8B%E8%8C%82%E8%80%81%E5%B8%88%E4%BD%9C%E4%B8%9A%E9%A2%98/HW10.pdf" >}}
{{< hoa-filetree/file name="HW2" type="pdf" size="284.8 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/%E9%A9%AC%E5%85%8B%E8%8C%82%E8%80%81%E5%B8%88%E4%BD%9C%E4%B8%9A%E9%A2%98/HW2.pdf" >}}
{{< hoa-filetree/file name="HW3" type="pdf" size="207.3 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/%E9%A9%AC%E5%85%8B%E8%8C%82%E8%80%81%E5%B8%88%E4%BD%9C%E4%B8%9A%E9%A2%98/HW3.pdf" >}}
{{< hoa-filetree/file name="HW4" type="pdf" size="382.4 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/%E9%A9%AC%E5%85%8B%E8%8C%82%E8%80%81%E5%B8%88%E4%BD%9C%E4%B8%9A%E9%A2%98/HW4.pdf" >}}
{{< hoa-filetree/file name="HW5" type="pdf" size="373.9 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/%E9%A9%AC%E5%85%8B%E8%8C%82%E8%80%81%E5%B8%88%E4%BD%9C%E4%B8%9A%E9%A2%98/HW5.pdf" >}}
{{< hoa-filetree/file name="HW6" type="pdf" size="225.3 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/%E9%A9%AC%E5%85%8B%E8%8C%82%E8%80%81%E5%B8%88%E4%BD%9C%E4%B8%9A%E9%A2%98/HW6.pdf" >}}
{{< hoa-filetree/file name="HW7" type="pdf" size="251.1 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/%E9%A9%AC%E5%85%8B%E8%8C%82%E8%80%81%E5%B8%88%E4%BD%9C%E4%B8%9A%E9%A2%98/HW7.pdf" >}}
{{< hoa-filetree/file name="HW8" type="pdf" size="317.8 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/%E9%A9%AC%E5%85%8B%E8%8C%82%E8%80%81%E5%B8%88%E4%BD%9C%E4%B8%9A%E9%A2%98/HW8.pdf" >}}
{{< hoa-filetree/file name="HW9" type="pdf" size="190.0 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%9C%AC%E9%83%A8/2025/%E9%A9%AC%E5%85%8B%E8%8C%82%E8%80%81%E5%B8%88%E4%BD%9C%E4%B8%9A%E9%A2%98/HW9.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="深圳" date="" state="closed" >}}
{{< hoa-filetree/folder name="LL" date="" state="closed" >}}
{{< hoa-filetree/file name="HW1" type="pdf" size="63.1 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%B7%B1%E5%9C%B3/LL/HW1.pdf" >}}
{{< hoa-filetree/file name="HW2" type="pdf" size="617.6 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%B7%B1%E5%9C%B3/LL/HW2.pdf" >}}
{{< hoa-filetree/file name="HW3" type="pdf" size="84.1 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%B7%B1%E5%9C%B3/LL/HW3.pdf" >}}
{{< hoa-filetree/file name="HW4" type="pdf" size="118.8 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%B7%B1%E5%9C%B3/LL/HW4.pdf" >}}
{{< hoa-filetree/file name="HW5" type="pdf" size="221.2 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%B7%B1%E5%9C%B3/LL/HW5.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="psp" date="" state="closed" >}}
{{< hoa-filetree/folder name="hw1" date="" state="closed" >}}
{{< hoa-filetree/folder name="code" date="" state="closed" >}}
{{< hoa-filetree/file name="hw1_a" type="m" size="1.7 KB" date="2026/01/20" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%B7%B1%E5%9C%B3/psp/hw1/code/hw1_a.m" >}}
{{< hoa-filetree/file name="hw1_b" type="m" size="1.1 KB" date="2026/01/20" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%B7%B1%E5%9C%B3/psp/hw1/code/hw1_b.m" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/file name="hw1-psp" type="docx" size="687.1 KB" date="2026/01/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%B7%B1%E5%9C%B3/psp/hw1/hw1-psp.docx" >}}
{{< hoa-filetree/file name="hw1" type="pdf" size="109.5 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%B7%B1%E5%9C%B3/psp/hw1/hw1.pdf" >}}
{{< hoa-filetree/folder name="simu" date="" state="closed" >}}
{{< hoa-filetree/file name="simu_22a" type="slx" size="42.3 KB" date="2026/01/20" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%B7%B1%E5%9C%B3/psp/hw1/simu/simu_22a.slx" >}}
{{< hoa-filetree/file name="simu_25a" type="slx" size="40.7 KB" date="2026/01/20" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%B7%B1%E5%9C%B3/psp/hw1/simu/simu_25a.slx" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="hw2" date="" state="closed" >}}
{{< hoa-filetree/file name="hw2-psp" type="docx" size="589.9 KB" date="2026/01/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%B7%B1%E5%9C%B3/psp/hw2/hw2-psp.docx" >}}
{{< hoa-filetree/file name="hw2" type="pdf" size="62.3 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%B7%B1%E5%9C%B3/psp/hw2/hw2.pdf" >}}
{{< hoa-filetree/folder name="simu" date="" state="closed" >}}
{{< hoa-filetree/file name="simu_22a" type="slx" size="43.8 KB" date="2026/01/20" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%B7%B1%E5%9C%B3/psp/hw2/simu/simu_22a.slx" >}}
{{< hoa-filetree/file name="simu_25a" type="slx" size="46.4 KB" date="2026/01/20" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/assignments/%E6%B7%B1%E5%9C%B3/psp/hw2/simu/simu_25a.slx" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="exams" date="" state="closed" >}}
{{< hoa-filetree/folder name="本部" date="" state="closed" >}}
{{< hoa-filetree/folder name="答案" date="" state="closed" >}}
{{< hoa-filetree/file name="2020 控制系统实践 II 试题-psp 详解" type="pdf" size="5.5 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%9C%AC%E9%83%A8/%E7%AD%94%E6%A1%88/2020%20%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E5%AE%9E%E8%B7%B5II%E8%AF%95%E9%A2%98-psp%E8%AF%A6%E8%A7%A3.pdf" >}}
{{< hoa-filetree/file name="2020 控制系统实践 II 试题答案" type="pdf" size="5.6 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%9C%AC%E9%83%A8/%E7%AD%94%E6%A1%88/2020%20%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E5%AE%9E%E8%B7%B5II%E8%AF%95%E9%A2%98%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="2025 秋本部回忆试题答案-Costannt" type="pdf" size="770.1 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%9C%AC%E9%83%A8/%E7%AD%94%E6%A1%88/2025%E7%A7%8B%E6%9C%AC%E9%83%A8%E5%9B%9E%E5%BF%86%E8%AF%95%E9%A2%98%E7%AD%94%E6%A1%88-Costannt.pdf" >}}
{{< hoa-filetree/file name="控制系统实践 II 复习题-psp 详解" type="pdf" size="15.8 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%9C%AC%E9%83%A8/%E7%AD%94%E6%A1%88/%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E5%AE%9E%E8%B7%B5II%E5%A4%8D%E4%B9%A0%E9%A2%98-psp%E8%AF%A6%E8%A7%A3.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="题目" date="" state="closed" >}}
{{< hoa-filetree/file name="2020 控制系统实践 II 试题" type="pdf" size="1.7 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%9C%AC%E9%83%A8/%E9%A2%98%E7%9B%AE/2020%20%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E5%AE%9E%E8%B7%B5II%E8%AF%95%E9%A2%98.pdf" >}}
{{< hoa-filetree/file name="2025 秋本部回忆试题-Costannt" type="pdf" size="327.2 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%9C%AC%E9%83%A8/%E9%A2%98%E7%9B%AE/2025%E7%A7%8B%E6%9C%AC%E9%83%A8%E5%9B%9E%E5%BF%86%E8%AF%95%E9%A2%98-Costannt.pdf" >}}
{{< hoa-filetree/file name="控制系统实践 II 复习题" type="pdf" size="15.6 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%9C%AC%E9%83%A8/%E9%A2%98%E7%9B%AE/%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E5%AE%9E%E8%B7%B5II%E5%A4%8D%E4%B9%A0%E9%A2%98.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="深圳" date="" state="closed" >}}
{{< hoa-filetree/file name="2021 自动控制实践 B 试题与答案-psp 详解" type="pdf" size="2.3 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%B7%B1%E5%9C%B3/2021%20%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5B%E8%AF%95%E9%A2%98%E4%B8%8E%E7%AD%94%E6%A1%88-psp%E8%AF%A6%E8%A7%A3.pdf" >}}
{{< hoa-filetree/file name="2021 自动控制实践 B 试题与答案" type="pdf" size="652.3 KB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%B7%B1%E5%9C%B3/2021%20%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5B%E8%AF%95%E9%A2%98%E4%B8%8E%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="2024 自动控制实践 B 试题回忆版-psp 详解" type="pdf" size="9.2 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%B7%B1%E5%9C%B3/2024%20%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5B%E8%AF%95%E9%A2%98%E5%9B%9E%E5%BF%86%E7%89%88-psp%E8%AF%A6%E8%A7%A3.pdf" >}}
{{< hoa-filetree/file name="2024 自动控制实践 B 试题回忆版" type="pdf" size="652.8 KB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%B7%B1%E5%9C%B3/2024%20%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5B%E8%AF%95%E9%A2%98%E5%9B%9E%E5%BF%86%E7%89%88.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="labs" date="" state="closed" >}}
{{< hoa-filetree/folder name="本部" date="" state="closed" >}}
{{< hoa-filetree/folder name="2025" date="" state="closed" >}}
{{< hoa-filetree/folder name="Costannt" date="" state="closed" >}}
{{< hoa-filetree/file name="仿真实验报告-Costannt" type="pdf" size="3.2 MB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/Costannt/%E4%BB%BF%E7%9C%9F%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A-Costannt.pdf" >}}
{{< hoa-filetree/file name="实物实验报告-Costannt" type="pdf" size="2.2 MB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/Costannt/%E5%AE%9E%E7%89%A9%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A-Costannt.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="实验指导书" date="" state="closed" >}}
{{< hoa-filetree/file name="1.建模参考流程 (1)" type="docx" size="111.9 KB" date="2026/01/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6/1.%E5%BB%BA%E6%A8%A1%E5%8F%82%E8%80%83%E6%B5%81%E7%A8%8B%281%29.docx" >}}
{{< hoa-filetree/file name="1.建模参考流程" type="docx" size="111.9 KB" date="2026/01/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6/1.%E5%BB%BA%E6%A8%A1%E5%8F%82%E8%80%83%E6%B5%81%E7%A8%8B.docx" >}}
{{< hoa-filetree/file name="2.模型验证参考流程" type="docx" size="194.7 KB" date="2026/01/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6/2.%E6%A8%A1%E5%9E%8B%E9%AA%8C%E8%AF%81%E5%8F%82%E8%80%83%E6%B5%81%E7%A8%8B.docx" >}}
{{< hoa-filetree/file name="3.模型验证方法" type="docx" size="36.8 KB" date="2026/01/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6/3.%E6%A8%A1%E5%9E%8B%E9%AA%8C%E8%AF%81%E6%96%B9%E6%B3%95.docx" >}}
{{< hoa-filetree/file name="伺服系统控制器设计与分析实验指导书 part2" type="pdf" size="334.8 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6/%E4%BC%BA%E6%9C%8D%E7%B3%BB%E7%BB%9F%E6%8E%A7%E5%88%B6%E5%99%A8%E8%AE%BE%E8%AE%A1%E4%B8%8E%E5%88%86%E6%9E%90%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6part2.pdf" >}}
{{< hoa-filetree/file name="信号 FFT 与频谱的关系" type="pdf" size="176.3 KB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6/%E4%BF%A1%E5%8F%B7FFT%E4%B8%8E%E9%A2%91%E8%B0%B1%E7%9A%84%E5%85%B3%E7%B3%BB.pdf" >}}
{{< hoa-filetree/file name="实验 1 直流电机组被控对象辨识（系统频率特性测试）" type="pdf" size="2.6 MB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6/%E5%AE%9E%E9%AA%8C1%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%BB%84%E8%A2%AB%E6%8E%A7%E5%AF%B9%E8%B1%A1%E8%BE%A8%E8%AF%86%EF%BC%88%E7%B3%BB%E7%BB%9F%E9%A2%91%E7%8E%87%E7%89%B9%E6%80%A7%E6%B5%8B%E8%AF%95%EF%BC%89.pdf" >}}
{{< hoa-filetree/file name="实验 2 直流电机组位置单闭环 PID 控制器设计" type="pdf" size="2.2 MB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6/%E5%AE%9E%E9%AA%8C2%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%BB%84%E4%BD%8D%E7%BD%AE%E5%8D%95%E9%97%AD%E7%8E%AFPID%E6%8E%A7%E5%88%B6%E5%99%A8%E8%AE%BE%E8%AE%A1.pdf" >}}
{{< hoa-filetree/file name="实验 3 直流电机组 PID 加干扰观测器控制器设计" type="pdf" size="1.4 MB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6/%E5%AE%9E%E9%AA%8C3%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%BB%84PID%E5%8A%A0%E5%B9%B2%E6%89%B0%E8%A7%82%E6%B5%8B%E5%99%A8%E6%8E%A7%E5%88%B6%E5%99%A8%E8%AE%BE%E8%AE%A1.pdf" >}}
{{< hoa-filetree/file name="实验 4 直流电机组频域控制器设计" type="pdf" size="1.5 MB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6/%E5%AE%9E%E9%AA%8C4%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%BB%84%E9%A2%91%E5%9F%9F%E6%8E%A7%E5%88%B6%E5%99%A8%E8%AE%BE%E8%AE%A1.pdf" >}}
{{< hoa-filetree/file name="实验 5 直流电机组双闭环 PID 控制器设计" type="pdf" size="1.2 MB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6/%E5%AE%9E%E9%AA%8C5%20%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E7%BB%84%E5%8F%8C%E9%97%AD%E7%8E%AFPID%E6%8E%A7%E5%88%B6%E5%99%A8%E8%AE%BE%E8%AE%A1.pdf" >}}
{{< hoa-filetree/file name="智能系统控制实验实验指导书 240428_1430" type="pdf" size="1.1 MB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6/%E6%99%BA%E8%83%BD%E7%B3%BB%E7%BB%9F%E6%8E%A7%E5%88%B6%E5%AE%9E%E9%AA%8C%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6240428_1430.pdf" >}}
{{< hoa-filetree/file name="模糊控制工具箱与模糊控制器" type="docx" size="1.7 MB" date="2026/01/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6/%E6%A8%A1%E7%B3%8A%E6%8E%A7%E5%88%B6%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B8%8E%E6%A8%A1%E7%B3%8A%E6%8E%A7%E5%88%B6%E5%99%A8.docx" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/file name="智能系统控制实践 - 仿真实验报告模板" type="docx" size="55.2 KB" date="2026/01/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/%E6%99%BA%E8%83%BD%E7%B3%BB%E7%BB%9F%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5-%E4%BB%BF%E7%9C%9F%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E6%A8%A1%E6%9D%BF.docx" >}}
{{< hoa-filetree/file name="智能系统控制实践 - 直流电机实验报告模板" type="docx" size="50.5 KB" date="2026/01/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%9C%AC%E9%83%A8/2025/%E6%99%BA%E8%83%BD%E7%B3%BB%E7%BB%9F%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5-%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E6%A8%A1%E6%9D%BF.docx" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="深圳" date="" state="closed" >}}
{{< hoa-filetree/folder name="2024" date="" state="closed" >}}
{{< hoa-filetree/folder name="LJH" date="" state="closed" >}}
{{< hoa-filetree/file name="ljh_综合实验报告_18 号机" type="pdf" size="1.7 MB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%B7%B1%E5%9C%B3/2024/LJH/ljh_%E7%BB%BC%E5%90%88%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A_18%E5%8F%B7%E6%9C%BA.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="WJD" date="" state="closed" >}}
{{< hoa-filetree/file name="wjd_综合" type="pdf" size="2.4 MB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%B7%B1%E5%9C%B3/2024/WJD/wjd_%E7%BB%BC%E5%90%88.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2025" date="" state="closed" >}}
{{< hoa-filetree/folder name="psp" date="" state="closed" >}}
{{< hoa-filetree/file name="2025-psp" type="docx" size="2.3 MB" date="2026/01/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%B7%B1%E5%9C%B3/2025/psp/2025-psp.docx" >}}
{{< hoa-filetree/folder name="simu" date="" state="closed" >}}
{{< hoa-filetree/file name="simu_22a" type="slx" size="36.9 KB" date="2026/01/20" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%B7%B1%E5%9C%B3/2025/psp/simu/simu_22a.slx" >}}
{{< hoa-filetree/file name="simu_25a" type="slx" size="102.4 KB" date="2026/01/20" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%B7%B1%E5%9C%B3/2025/psp/simu/simu_25a.slx" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/file name="实验任务书" type="pdf" size="5.6 MB" date="2026/01/20" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%B7%B1%E5%9C%B3/2025/%E5%AE%9E%E9%AA%8C%E4%BB%BB%E5%8A%A1%E4%B9%A6.pdf" >}}
{{< hoa-filetree/file name="实验报告模板" type="docx" size="976.9 KB" date="2026/01/20" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/labs/%E6%B7%B1%E5%9C%B3/2025/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E6%A8%A1%E6%9D%BF.docx" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="notes" date="" state="closed" >}}
{{< hoa-filetree/file name="November_in_North_自控实践 B 笔记" type="pdf" size="97.5 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/notes/November_in_North_%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5B%E7%AC%94%E8%AE%B0.pdf" >}}
{{< hoa-filetree/file name="Revision of Auto-Practical" type="pdf" size="9.4 MB" date="2024/05/09" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/notes/Revision%20of%20Auto-Practical.pdf" >}}
{{< hoa-filetree/file name="【2025 春季学期】自动控制实践 B 课程总结笔记 -22 级自动化 - 刘劭航-v1.2" type="pdf" size="2.6 MB" date="2025/06/03" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/notes/%E3%80%902025%E6%98%A5%E5%AD%A3%E5%AD%A6%E6%9C%9F%E3%80%91%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%AE%9E%E8%B7%B5B%E8%AF%BE%E7%A8%8B%E6%80%BB%E7%BB%93%E7%AC%94%E8%AE%B0-22%E7%BA%A7%E8%87%AA%E5%8A%A8%E5%8C%96-%E5%88%98%E5%8A%AD%E8%88%AA-v1.2.pdf" >}}
{{< hoa-filetree/file name="自控实践 B 复习_Tintin" type="pdf" size="6.4 MB" date="2024/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/notes/%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5B%E5%A4%8D%E4%B9%A0_Tintin.pdf" >}}
{{< hoa-filetree/file name="自控实践复习整理 byAb1g2he" type="pdf" size="3.4 MB" date="2024/07/16" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/notes/%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5%E5%A4%8D%E4%B9%A0%E6%95%B4%E7%90%86byAb1g2he.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="slides" date="" state="closed" >}}
{{< hoa-filetree/folder name="课件 - 带笔记-psp" date="" state="closed" >}}
{{< hoa-filetree/file name="1 绪论" type="pdf" size="716.7 KB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/1%20%E7%BB%AA%E8%AE%BA.pdf" >}}
{{< hoa-filetree/file name="10 课程习题讲解" type="pdf" size="3.2 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/10%20%E8%AF%BE%E7%A8%8B%E4%B9%A0%E9%A2%98%E8%AE%B2%E8%A7%A3.pdf" >}}
{{< hoa-filetree/file name="2 控制系统的设计流程" type="pdf" size="2.3 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/2%20%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E7%9A%84%E8%AE%BE%E8%AE%A1%E6%B5%81%E7%A8%8B.pdf" >}}
{{< hoa-filetree/file name="3.1 控制系统的输入条件分析 - 输入" type="pdf" size="13.3 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/3.1%20%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E7%9A%84%E8%BE%93%E5%85%A5%E6%9D%A1%E4%BB%B6%E5%88%86%E6%9E%90-%E8%BE%93%E5%85%A5.pdf" >}}
{{< hoa-filetree/file name="3.2 控制系统输入条件分析 - 干扰" type="pdf" size="6.8 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/3.2%20%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E8%BE%93%E5%85%A5%E6%9D%A1%E4%BB%B6%E5%88%86%E6%9E%90-%E5%B9%B2%E6%89%B0.pdf" >}}
{{< hoa-filetree/file name="3.3 控制系统输入条件分析 - 噪声" type="pdf" size="9.1 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/3.3%20%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E8%BE%93%E5%85%A5%E6%9D%A1%E4%BB%B6%E5%88%86%E6%9E%90-%E5%99%AA%E5%A3%B0.pdf" >}}
{{< hoa-filetree/file name="4 控制系统的设计约束" type="pdf" size="12.0 MB" date="2025/06/27" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/4%20%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E7%9A%84%E8%AE%BE%E8%AE%A1%E7%BA%A6%E6%9D%9F.pdf" >}}
{{< hoa-filetree/file name="5 Anti-Windup 设计" type="pdf" size="6.4 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/5%20Anti-Windup%E8%AE%BE%E8%AE%A1.pdf" >}}
{{< hoa-filetree/file name="6 伺服系统" type="pdf" size="6.3 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/6%20%E4%BC%BA%E6%9C%8D%E7%B3%BB%E7%BB%9F.pdf" >}}
{{< hoa-filetree/file name="7 调节系统的设计" type="pdf" size="7.1 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/7%20%E8%B0%83%E8%8A%82%E7%B3%BB%E7%BB%9F%E7%9A%84%E8%AE%BE%E8%AE%A1.pdf" >}}
{{< hoa-filetree/file name="8 多回路系统的设计" type="pdf" size="5.1 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/8%20%E5%A4%9A%E5%9B%9E%E8%B7%AF%E7%B3%BB%E7%BB%9F%E7%9A%84%E8%AE%BE%E8%AE%A1.pdf" >}}
{{< hoa-filetree/file name="9 课程总结" type="pdf" size="1.3 MB" date="2025/06/12" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/slides/%E8%AF%BE%E4%BB%B6-%E5%B8%A6%E7%AC%94%E8%AE%B0-psp/9%20%E8%AF%BE%E7%A8%8B%E6%80%BB%E7%BB%93.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/container >}}

## 参与

《HITSZ 自动化课程攻略共享计划》是所有同学都可以参与编写的，如果你有好的笔记或者资料，欢迎前往我们的 [GitHub](https://github.com/HITSZ-OpenAuto) 进行参与，也可以发邮件至 [📮hi@hoa.moe](mailto:hi@hoa.moe) 联系我们，我们会在收到的第一时间进行答复。

{{< callout type="" >}}
  © 版权声明：[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-nc-sa/4.0/)
{{< /callout >}}

