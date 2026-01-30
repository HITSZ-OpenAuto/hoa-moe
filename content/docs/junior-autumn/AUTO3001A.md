---
title: （必修）自动控制理论 A
weight: 7
toc: true
editURL: "https://github.com/HITSZ-OpenAuto/AUTO3001A/edit/main/README.md"
math: true
---

{{< update-info update_time="2026 年 1 月 13 日" author="Jiao Ziang" message="增加新 toml 并且修改错误链接" >}}

**课程代码：** AUTO3001A

## 授课教师

### 张宏伟

负责课程的前半部分。
              上课和聊天一样，会将知识引申到课外的领域中。
              考勤频率低。
              上课以吹水为主，对于想快速掌握本课程知识而不想浪费时间的同学，不建议听课。
              思维发散，但是例题有给比较充分时间上课完成，且对例题比较好的讲解。

> 文 / Maxwell Jay & Oliver Wu & Gaster, 2025.6

### 张颖

负责课程的后半部分。
              教学节奏较慢，有一种回到中学课堂的感觉。
              几乎每节课都会考勤点名，一次点名一个班。
              上课思维较为连贯，但是 PPT 有大量的例题没有给时间完成。

> 文 / Maxwell Jay & Gaster, 2025.6

## 教材与参考书

**自动控制原理（上下册）**
作者：裴润，宋申民 | 出版社：哈尔滨工业大学出版社 | 版本：2006

**自动控制原理**
作者：胡寿松 | 出版社：科学出版社 | 版本：第七版/第八版

**现代控制理论**
作者：刘豹，唐万生 | 出版社：机械工业出版社 | 版本：2006

**Modern Control Systems (现代控制系统)**
作者：Richard Dorf, Robert Bishop | 出版社：Pearson | 版本：14th Edition

**Modern Control Engineering (现代控制工程)**
作者：Katsuhiko Ogata | 出版社：Pearson | 版本：5th Edition

**Feedback Control of Dynamic Systems (自动控制原理与设计)**
作者：G.Franklin, J.Powell, A.Emami-Naeini | 出版社：Pearson | 版本：8th Edition

**控制之美（卷 1）**
作者：王天威 (DR_CAN) | 出版社：清华大学出版社

## 在线资源

- [卢老爷带你学系列 | 深入浅出《自动控制原理》]([https://space.bilibili.com/443689502/lists/1784905](https://space.bilibili.com/443689502/lists/1784905))
  Bilibili 视频教程

- [【自动控制原理】_DR_CAN 合集]([https://space.bilibili.com/230105574/lists/1814627](https://space.bilibili.com/230105574/lists/1814627))
  Bilibili 视频教程，科普性强

- [《自动控制原理 480 题》]([https://hitpress.hit.edu.cn/2017/1213/c12593a195955/page.htm](https://hitpress.hit.edu.cn/2017/1213/c12593a195955/page.htm))
  哈尔滨工业大学出版社，习题集

- [Gaster 的控制理论笔记]([https://github.com/WDGaster703/ControlTheory](https://github.com/WDGaster703/ControlTheory))
  深入学习控制理论的笔记

- [SSC 的电机驱动学习笔记]([https://github.com/SSC202/Engine/tree/V3.0/Note/](https://github.com/SSC202/Engine/tree/V3.0/Note/))
  包含相关控制理论应用

## 课程评价

### 1. 原 4.5 学分版（自动化大三秋）
*   **绪论**：控制论历史、基本结构。
*   **数学模型**：微分方程、传递函数、方框图、离散建模、状态空间。
*   **时域分析**：连续/离散系统时域分析、状态空间时域分析。
*   **稳定性及稳态误差**：劳斯判据、稳态误差、Lyapunov 稳定性、根轨迹法。
*   **频域分析**：频率特性、奈奎斯特判据。

### 2. 《系统与控制》3.0 学分版（电气大二春）
*   主要包含：线性连续系统的数学模型、时域分析、稳定性分析（劳斯/根轨迹）、频域分析（奈奎斯特）。
*   **注**：不包含离散系统和现代控制理论（状态空间）部分。

### 3. 新《自动控制理论 A》2.0 学分版（自动化大三秋）
*   **内容**：线性离散系统建模与时域分析、状态空间表达式建模与时域分析、Lyapunov 稳定性分析。
*   **定位**：作为《系统与控制》的后续补充课程。

> 文 / [Gaster]([https://github.com/WDGaster703](https://github.com/WDGaster703)), 2025.7

## 考试

*   **难度波动**：2024 年期末考试题目较难，但给分较松；2025 春《系统与控制》回归往年难度，低于考研题，考察较细。
*   **备考建议**：本校考试风格与考研题接近，建议刷哈工大的考研真题练手。

> 文 / Maxwell Jay & Oliver Wu & Gaster, 2025.6

## 实验

**硬件实验 (8 学时)**：
1. 直流伺服系统的时域特性分析
2. 连续系统和离散系统的稳定性分析
3. 直流伺服系统的根轨迹分析
4. 直流伺服系统的频率特性分析

**上机实验 (4 学时)**：
1. 控制系统的模型描述与时域分析
2. 线性系统的根轨迹和频域分析

> 文 / [Gaster]([https://github.com/WDGaster703](https://github.com/WDGaster703)), 2025.7

## 建议

1.  **多参考书策略**：课程未指定单一教材，建议向不同的参考书学习，同一知识点不同解释有助于理解。
2.  **网络资源**：作为考研科目，网络资源极丰富，搞不明白的题型直接搜索。
3.  **核心关注**：重点是时域分析（快准稳），关注**时域 - 频域 - 复频域**的联系和转化。根轨迹要掌握绘制方法，频域响应掌握 Nyquist 图和 Bode 图绘制。

## 其他信息

### 作业频率

*   自控理论的作业布置频率较高，基本每周一次。
*   张宏伟老师的作业部分原创，具挑战性；张颖老师作业多来自课后题。

> 文 / [Maxwell Jay]([https://github.com/MaxwellJay256](https://github.com/MaxwellJay256)), 2025.1

## 资料下载

如果你是校内学生，可点击如下「内网网盘」按钮查看本门课程的电子书、课件和实验软件等。

{{< hoa-filetree/container driveURL="https://open.osa.moe/openauto/AUTO3001A" repoURL="https://github.com/HITSZ-OpenAuto/AUTO3001A" >}}
{{< hoa-filetree/file name="AUTO3001A" type="toml" size="10.4 KB" date="2026/01/13" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/AUTO3001A.toml" >}}
{{< hoa-filetree/folder name="assignments" date="" state="closed" >}}
{{< hoa-filetree/folder name="2019" date="" state="closed" >}}
{{< hoa-filetree/file name="自控理论 A—作业 10 及答案" type="pdf" size="2.3 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2019/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E2%80%94%E4%BD%9C%E4%B8%9A10%E5%8F%8A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控理论 A—作业 11 及答案" type="pdf" size="969.0 KB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2019/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E2%80%94%E4%BD%9C%E4%B8%9A11%E5%8F%8A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控理论 A—作业 12 及答案 (1)" type="pdf" size="1.7 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2019/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E2%80%94%E4%BD%9C%E4%B8%9A12%E5%8F%8A%E7%AD%94%E6%A1%88%281%29.pdf" >}}
{{< hoa-filetree/file name="自控理论 A—作业 12 及答案 (2)" type="pdf" size="2.3 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2019/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E2%80%94%E4%BD%9C%E4%B8%9A12%E5%8F%8A%E7%AD%94%E6%A1%88%282%29.pdf" >}}
{{< hoa-filetree/file name="自控理论 A—作业 1 及答案" type="pdf" size="567.6 KB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2019/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E2%80%94%E4%BD%9C%E4%B8%9A1%E5%8F%8A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控理论 A—作业 2 及答案" type="pdf" size="1.3 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2019/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E2%80%94%E4%BD%9C%E4%B8%9A2%E5%8F%8A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控理论 A—作业 3 及答案" type="pdf" size="2.1 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2019/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E2%80%94%E4%BD%9C%E4%B8%9A3%E5%8F%8A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控理论 A—作业 4 及答案" type="pdf" size="281.5 KB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2019/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E2%80%94%E4%BD%9C%E4%B8%9A4%E5%8F%8A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控理论 A—作业 5 及答案" type="pdf" size="801.4 KB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2019/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E2%80%94%E4%BD%9C%E4%B8%9A5%E5%8F%8A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控理论 A—作业 6 及答案" type="pdf" size="1.5 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2019/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E2%80%94%E4%BD%9C%E4%B8%9A6%E5%8F%8A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控理论 A—作业 7 及答案 (1)" type="pdf" size="2.7 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2019/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E2%80%94%E4%BD%9C%E4%B8%9A7%E5%8F%8A%E7%AD%94%E6%A1%88%281%29.pdf" >}}
{{< hoa-filetree/file name="自控理论 A—作业 7 及答案 (2)" type="pdf" size="573.4 KB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2019/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E2%80%94%E4%BD%9C%E4%B8%9A7%E5%8F%8A%E7%AD%94%E6%A1%88%282%29.pdf" >}}
{{< hoa-filetree/file name="自控理论 A—作业 8 及答案" type="pdf" size="1.9 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2019/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E2%80%94%E4%BD%9C%E4%B8%9A8%E5%8F%8A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控理论 A—作业 9 及答案 (1)" type="pdf" size="1.7 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2019/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E2%80%94%E4%BD%9C%E4%B8%9A9%E5%8F%8A%E7%AD%94%E6%A1%88%281%29.pdf" >}}
{{< hoa-filetree/file name="自控理论 A—作业 9 及答案 (2)" type="pdf" size="440.6 KB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2019/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E2%80%94%E4%BD%9C%E4%B8%9A9%E5%8F%8A%E7%AD%94%E6%A1%88%282%29.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2022_FWI_Version" date="" state="closed" >}}
{{< hoa-filetree/folder name="1" date="" state="closed" >}}
{{< hoa-filetree/file name="自动控制原理 A 第一次作业答案" type="pdf" size="558.0 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/1/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86A%E7%AC%AC%E4%B8%80%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控作业 -1" type="pdf" size="273.7 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/1/%E8%87%AA%E6%8E%A7%E4%BD%9C%E4%B8%9A-1.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="10" date="" state="closed" >}}
{{< hoa-filetree/file name="自动控制原理 A 第十次作业答案" type="pdf" size="237.5 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/10/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86A%E7%AC%AC%E5%8D%81%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控理论 -10" type="pdf" size="151.8 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/10/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BA-10.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="11" date="" state="closed" >}}
{{< hoa-filetree/file name="自动控制原理 A 第十一次作业答案" type="pdf" size="16.7 MB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/11/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86A%E7%AC%AC%E5%8D%81%E4%B8%80%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控理论 -11" type="pdf" size="334.8 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/11/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BA-11.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2" date="" state="closed" >}}
{{< hoa-filetree/file name="自动控制原理 A 第二次作业答案" type="pdf" size="412.8 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/2/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86A%E7%AC%AC%E4%BA%8C%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控作业 -2" type="pdf" size="265.3 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/2/%E8%87%AA%E6%8E%A7%E4%BD%9C%E4%B8%9A-2.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="3" date="" state="closed" >}}
{{< hoa-filetree/file name="自动控制原理 A 第三次作业答案" type="pdf" size="555.2 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/3/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86A%E7%AC%AC%E4%B8%89%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控作业 -3" type="pdf" size="197.3 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/3/%E8%87%AA%E6%8E%A7%E4%BD%9C%E4%B8%9A-3.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="4" date="" state="closed" >}}
{{< hoa-filetree/file name="自动控制原理 A 第四次作业答案" type="pdf" size="535.0 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/4/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86A%E7%AC%AC%E5%9B%9B%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控作业 -4" type="pdf" size="446.4 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/4/%E8%87%AA%E6%8E%A7%E4%BD%9C%E4%B8%9A-4.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="5" date="" state="closed" >}}
{{< hoa-filetree/file name="自动控制原理 A 第五次作业答案" type="pdf" size="540.0 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/5/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86A%E7%AC%AC%E4%BA%94%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控作业 -5" type="pdf" size="186.2 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/5/%E8%87%AA%E6%8E%A7%E4%BD%9C%E4%B8%9A-5.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="6" date="" state="closed" >}}
{{< hoa-filetree/file name="自动控制原理 A 第六次作业答案" type="pdf" size="329.3 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/6/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86A%E7%AC%AC%E5%85%AD%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控作业 -6" type="pdf" size="172.1 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/6/%E8%87%AA%E6%8E%A7%E4%BD%9C%E4%B8%9A-6.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="7" date="" state="closed" >}}
{{< hoa-filetree/file name="自动控制原理 A 第七次作业答案" type="pdf" size="339.5 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/7/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86A%E7%AC%AC%E4%B8%83%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控作业 -7" type="pdf" size="170.4 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/7/%E8%87%AA%E6%8E%A7%E4%BD%9C%E4%B8%9A-7.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="8" date="" state="closed" >}}
{{< hoa-filetree/file name="自动控制原理 A 第八次作业答案" type="pdf" size="555.3 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/8/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86A%E7%AC%AC%E5%85%AB%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控作业 -8" type="pdf" size="322.4 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/8/%E8%87%AA%E6%8E%A7%E4%BD%9C%E4%B8%9A-8.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="9" date="" state="closed" >}}
{{< hoa-filetree/file name="自动控制原理 A 第九次作业答案" type="pdf" size="528.8 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/9/%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86A%E7%AC%AC%E4%B9%9D%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控作业 -9" type="pdf" size="295.9 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/9/%E8%87%AA%E6%8E%A7%E4%BD%9C%E4%B8%9A-9.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="标准答案" date="" state="closed" >}}
{{< hoa-filetree/file name="自控原理 A 作业 1-6 答案" type="pdf" size="268.7 KB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/%E6%A0%87%E5%87%86%E7%AD%94%E6%A1%88/%E8%87%AA%E6%8E%A7%E5%8E%9F%E7%90%86A%E4%BD%9C%E4%B8%9A1-6%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 11 答案" type="pdf" size="1.7 MB" date="2024/03/02" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2022_FWI_Version/%E6%A0%87%E5%87%86%E7%AD%94%E6%A1%88/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A11%E7%AD%94%E6%A1%88.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2024" date="" state="closed" >}}
{{< hoa-filetree/folder name="homework" date="" state="closed" >}}
{{< hoa-filetree/file name="自控理论 A 作业 1" type="pdf" size="268.8 KB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/homework/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A1.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 10" type="pdf" size="437.2 KB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/homework/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A10.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 11" type="pdf" size="285.6 KB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/homework/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A11.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 12" type="pdf" size="581.9 KB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/homework/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A12.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 2" type="pdf" size="491.7 KB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/homework/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A2.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 3" type="pdf" size="344.0 KB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/homework/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A3.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 4" type="pdf" size="270.6 KB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/homework/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A4.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 5" type="pdf" size="411.1 KB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/homework/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A5.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 6" type="pdf" size="297.9 KB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/homework/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A6.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 8" type="pdf" size="350.1 KB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/homework/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A8.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 9" type="pdf" size="594.5 KB" date="2025/01/13" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/homework/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A9.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="psp_answer" date="" state="closed" >}}
{{< hoa-filetree/folder name="code" date="" state="closed" >}}
{{< hoa-filetree/file name="hw5_T3" type="m" size="1.5 KB" date="2025/06/25" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/psp_answer/code/hw5_T3.m" >}}
{{< hoa-filetree/file name="hw5_T4" type="m" size="1.5 KB" date="2025/01/17" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/psp_answer/code/hw5_T4.m" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/file name="自控理论 A 作业 1-psp" type="pdf" size="1.7 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/psp_answer/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A1-psp.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 10-psp" type="pdf" size="2.8 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/psp_answer/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A10-psp.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 11-psp" type="pdf" size="1.1 MB" date="2025/01/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/psp_answer/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A11-psp.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 12-psp" type="pdf" size="2.7 MB" date="2025/01/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/psp_answer/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A12-psp.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 2-psp" type="pdf" size="1.6 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/psp_answer/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A2-psp.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 3-psp" type="pdf" size="1.9 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/psp_answer/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A3-psp.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 4-psp" type="pdf" size="895.7 KB" date="2025/01/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/psp_answer/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A4-psp.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 5-psp" type="pdf" size="2.2 MB" date="2025/01/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/psp_answer/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A5-psp.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 6-psp" type="pdf" size="2.2 MB" date="2025/01/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/psp_answer/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A6-psp.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 8-psp" type="pdf" size="2.4 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/psp_answer/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A8-psp.pdf" >}}
{{< hoa-filetree/file name="自控理论 A 作业 9-psp" type="pdf" size="1.8 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2024/psp_answer/%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E4%BD%9C%E4%B8%9A9-psp.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2025 春（系统与控制）" date="" state="closed" >}}
{{< hoa-filetree/folder name="Gaster 解答" date="" state="closed" >}}
{{< hoa-filetree/file name="系统与控制作业 1-Gaster" type="pdf" size="339.8 KB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2025%E6%98%A5%EF%BC%88%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%EF%BC%89/Gaster%E8%A7%A3%E7%AD%94/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%BD%9C%E4%B8%9A1-Gaster.pdf" >}}
{{< hoa-filetree/file name="系统与控制作业 2-Gaster" type="pdf" size="492.5 KB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2025%E6%98%A5%EF%BC%88%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%EF%BC%89/Gaster%E8%A7%A3%E7%AD%94/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%BD%9C%E4%B8%9A2-Gaster.pdf" >}}
{{< hoa-filetree/file name="系统与控制作业 3-Gaster" type="pdf" size="406.9 KB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2025%E6%98%A5%EF%BC%88%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%EF%BC%89/Gaster%E8%A7%A3%E7%AD%94/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%BD%9C%E4%B8%9A3-Gaster.pdf" >}}
{{< hoa-filetree/file name="系统与控制作业 4-Gaster" type="pdf" size="398.6 KB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2025%E6%98%A5%EF%BC%88%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%EF%BC%89/Gaster%E8%A7%A3%E7%AD%94/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%BD%9C%E4%B8%9A4-Gaster.pdf" >}}
{{< hoa-filetree/file name="系统与控制作业 5-Gaster" type="pdf" size="287.2 KB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2025%E6%98%A5%EF%BC%88%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%EF%BC%89/Gaster%E8%A7%A3%E7%AD%94/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%BD%9C%E4%B8%9A5-Gaster.pdf" >}}
{{< hoa-filetree/file name="系统与控制作业 6-Gaster" type="pdf" size="738.1 KB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2025%E6%98%A5%EF%BC%88%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%EF%BC%89/Gaster%E8%A7%A3%E7%AD%94/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%BD%9C%E4%B8%9A6-Gaster.pdf" >}}
{{< hoa-filetree/file name="系统与控制作业 7-Gaster" type="pdf" size="741.5 KB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2025%E6%98%A5%EF%BC%88%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%EF%BC%89/Gaster%E8%A7%A3%E7%AD%94/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%BD%9C%E4%B8%9A7-Gaster.pdf" >}}
{{< hoa-filetree/file name="系统与控制作业 8-Gaster" type="pdf" size="770.4 KB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2025%E6%98%A5%EF%BC%88%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%EF%BC%89/Gaster%E8%A7%A3%E7%AD%94/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%BD%9C%E4%B8%9A8-Gaster.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/file name="系统与控制作业 -1" type="pdf" size="197.4 KB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2025%E6%98%A5%EF%BC%88%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%EF%BC%89/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%BD%9C%E4%B8%9A-1.pdf" >}}
{{< hoa-filetree/file name="系统与控制作业 -2" type="pdf" size="294.3 KB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2025%E6%98%A5%EF%BC%88%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%EF%BC%89/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%BD%9C%E4%B8%9A-2.pdf" >}}
{{< hoa-filetree/file name="系统与控制作业 -3" type="pdf" size="284.1 KB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2025%E6%98%A5%EF%BC%88%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%EF%BC%89/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%BD%9C%E4%B8%9A-3.pdf" >}}
{{< hoa-filetree/file name="系统与控制作业 -4" type="pdf" size="305.4 KB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2025%E6%98%A5%EF%BC%88%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%EF%BC%89/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%BD%9C%E4%B8%9A-4.pdf" >}}
{{< hoa-filetree/file name="系统与控制作业 -5" type="pdf" size="267.2 KB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2025%E6%98%A5%EF%BC%88%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%EF%BC%89/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%BD%9C%E4%B8%9A-5.pdf" >}}
{{< hoa-filetree/file name="系统与控制作业 -6" type="pdf" size="285.0 KB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2025%E6%98%A5%EF%BC%88%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%EF%BC%89/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%BD%9C%E4%B8%9A-6.pdf" >}}
{{< hoa-filetree/file name="系统与控制作业 -7" type="pdf" size="387.5 KB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2025%E6%98%A5%EF%BC%88%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%EF%BC%89/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%BD%9C%E4%B8%9A-7.pdf" >}}
{{< hoa-filetree/file name="系统与控制作业 -8" type="pdf" size="337.5 KB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/assignments/2025%E6%98%A5%EF%BC%88%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%EF%BC%89/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%BD%9C%E4%B8%9A-8.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="exams" date="" state="closed" >}}
{{< hoa-filetree/folder name="本部" date="" state="closed" >}}
{{< hoa-filetree/folder name="2019_本部试题" date="" state="closed" >}}
{{< hoa-filetree/file name="哈工大 2019 自控原理 C 试题与答案" type="pdf" size="754.7 KB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/exams/%E6%9C%AC%E9%83%A8/2019_%E6%9C%AC%E9%83%A8%E8%AF%95%E9%A2%98/%E5%93%88%E5%B7%A5%E5%A4%A72019%E8%87%AA%E6%8E%A7%E5%8E%9F%E7%90%86C%E8%AF%95%E9%A2%98%E4%B8%8E%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/folder name="详解-psp" date="" state="closed" >}}
{{< hoa-filetree/file name="哈工大 2019 自控原理 C 试题与答案 (含批注)" type="pdf" size="1.1 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/exams/%E6%9C%AC%E9%83%A8/2019_%E6%9C%AC%E9%83%A8%E8%AF%95%E9%A2%98/%E8%AF%A6%E8%A7%A3-psp/%E5%93%88%E5%B7%A5%E5%A4%A72019%E8%87%AA%E6%8E%A7%E5%8E%9F%E7%90%86C%E8%AF%95%E9%A2%98%E4%B8%8E%E7%AD%94%E6%A1%88%28%E5%90%AB%E6%89%B9%E6%B3%A8%29.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2022 以前_本部试题合集" date="" state="closed" >}}
{{< hoa-filetree/file name="[网盘计划]自动控制原理" type="pdf" size="25.8 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/exams/%E6%9C%AC%E9%83%A8/2022%E4%BB%A5%E5%89%8D_%E6%9C%AC%E9%83%A8%E8%AF%95%E9%A2%98%E5%90%88%E9%9B%86/%5B%E7%BD%91%E7%9B%98%E8%AE%A1%E5%88%92%5D%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86.pdf" >}}
{{< hoa-filetree/folder name="详解-psp" date="" state="closed" >}}
{{< hoa-filetree/file name="[网盘计划]自动控制原理 -10-18" type="pdf" size="5.4 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/exams/%E6%9C%AC%E9%83%A8/2022%E4%BB%A5%E5%89%8D_%E6%9C%AC%E9%83%A8%E8%AF%95%E9%A2%98%E5%90%88%E9%9B%86/%E8%AF%A6%E8%A7%A3-psp/%5B%E7%BD%91%E7%9B%98%E8%AE%A1%E5%88%92%5D%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86-10-18.pdf" >}}
{{< hoa-filetree/file name="[网盘计划]自动控制原理 -19-24" type="pdf" size="2.8 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/exams/%E6%9C%AC%E9%83%A8/2022%E4%BB%A5%E5%89%8D_%E6%9C%AC%E9%83%A8%E8%AF%95%E9%A2%98%E5%90%88%E9%9B%86/%E8%AF%A6%E8%A7%A3-psp/%5B%E7%BD%91%E7%9B%98%E8%AE%A1%E5%88%92%5D%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86-19-24.pdf" >}}
{{< hoa-filetree/file name="[网盘计划]自动控制原理 -3-9" type="pdf" size="3.0 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/exams/%E6%9C%AC%E9%83%A8/2022%E4%BB%A5%E5%89%8D_%E6%9C%AC%E9%83%A8%E8%AF%95%E9%A2%98%E5%90%88%E9%9B%86/%E8%AF%A6%E8%A7%A3-psp/%5B%E7%BD%91%E7%9B%98%E8%AE%A1%E5%88%92%5D%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86-3-9.pdf" >}}
{{< hoa-filetree/file name="[网盘计划]自动控制原理 -61-67" type="pdf" size="1.0 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/exams/%E6%9C%AC%E9%83%A8/2022%E4%BB%A5%E5%89%8D_%E6%9C%AC%E9%83%A8%E8%AF%95%E9%A2%98%E5%90%88%E9%9B%86/%E8%AF%A6%E8%A7%A3-psp/%5B%E7%BD%91%E7%9B%98%E8%AE%A1%E5%88%92%5D%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86-61-67.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="深圳" date="" state="closed" >}}
{{< hoa-filetree/folder name="2019" date="" state="closed" >}}
{{< hoa-filetree/file name="2019 秋自控理论 A 期中考试答案" type="pdf" size="467.6 KB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/exams/%E6%B7%B1%E5%9C%B3/2019/2019%E7%A7%8B%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E6%9C%9F%E4%B8%AD%E8%80%83%E8%AF%95%E7%AD%94%E6%A1%88.pdf" >}}
{{< hoa-filetree/file name="2019 秋自控理论 A 期末考试 A 试题" type="pdf" size="527.3 KB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/exams/%E6%B7%B1%E5%9C%B3/2019/2019%E7%A7%8B%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E6%9C%9F%E6%9C%AB%E8%80%83%E8%AF%95A%E8%AF%95%E9%A2%98.pdf" >}}
{{< hoa-filetree/folder name="详解-psp" date="" state="closed" >}}
{{< hoa-filetree/file name="2019 秋自控理论 A 期中考试答案 (含批注)" type="pdf" size="1.1 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/exams/%E6%B7%B1%E5%9C%B3/2019/%E8%AF%A6%E8%A7%A3-psp/2019%E7%A7%8B%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E6%9C%9F%E4%B8%AD%E8%80%83%E8%AF%95%E7%AD%94%E6%A1%88%28%E5%90%AB%E6%89%B9%E6%B3%A8%29.pdf" >}}
{{< hoa-filetree/file name="2019 秋自控理论 A 期末考试 A 试题解答" type="pdf" size="2.6 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/exams/%E6%B7%B1%E5%9C%B3/2019/%E8%AF%A6%E8%A7%A3-psp/2019%E7%A7%8B%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E6%9C%9F%E6%9C%AB%E8%80%83%E8%AF%95A%E8%AF%95%E9%A2%98%E8%A7%A3%E7%AD%94.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/file name="2023 自动控制原理 A 试题考点回忆版" type="pdf" size="98.9 KB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/exams/%E6%B7%B1%E5%9C%B3/2023%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E5%8E%9F%E7%90%86A%E8%AF%95%E9%A2%98%E8%80%83%E7%82%B9%E5%9B%9E%E5%BF%86%E7%89%88.pdf" >}}
{{< hoa-filetree/folder name="2024" date="" state="closed" >}}
{{< hoa-filetree/file name="2024 秋自控理论 A 期末（参考答案 v2.0 版）" type="pdf" size="11.0 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/exams/%E6%B7%B1%E5%9C%B3/2024/2024%E7%A7%8B%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E6%9C%9F%E6%9C%AB%EF%BC%88%E5%8F%82%E8%80%83%E7%AD%94%E6%A1%88v2.0%E7%89%88%EF%BC%89.pdf" >}}
{{< hoa-filetree/file name="2024 秋自控理论 A 期末（回忆 v2.1 版）" type="pdf" size="1.3 MB" date="2025/06/25" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/exams/%E6%B7%B1%E5%9C%B3/2024/2024%E7%A7%8B%E8%87%AA%E6%8E%A7%E7%90%86%E8%AE%BAA%E6%9C%9F%E6%9C%AB%EF%BC%88%E5%9B%9E%E5%BF%86v2.1%E7%89%88%EF%BC%89.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/file name="2025 春系统与控制期末试题（回忆版）" type="pdf" size="1.2 MB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/exams/%E6%B7%B1%E5%9C%B3/2025%E6%98%A5%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E6%9C%9F%E6%9C%AB%E8%AF%95%E9%A2%98%EF%BC%88%E5%9B%9E%E5%BF%86%E7%89%88%EF%BC%89.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="labs" date="" state="closed" >}}
{{< hoa-filetree/folder name="2021_lmh(仅实物实验)" date="" state="closed" >}}
{{< hoa-filetree/file name="实验 1 报告" type="pdf" size="13.6 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2021_lmh%28%E4%BB%85%E5%AE%9E%E7%89%A9%E5%AE%9E%E9%AA%8C%29/%E5%AE%9E%E9%AA%8C1%E6%8A%A5%E5%91%8A.pdf" >}}
{{< hoa-filetree/file name="实验 2 系统的稳定性分析 (连续 + 离散) 实验报告 2020" type="pdf" size="7.8 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2021_lmh%28%E4%BB%85%E5%AE%9E%E7%89%A9%E5%AE%9E%E9%AA%8C%29/%E5%AE%9E%E9%AA%8C2%20%E7%B3%BB%E7%BB%9F%E7%9A%84%E7%A8%B3%E5%AE%9A%E6%80%A7%E5%88%86%E6%9E%90%28%E8%BF%9E%E7%BB%AD%2B%E7%A6%BB%E6%95%A3%29%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A2020.pdf" >}}
{{< hoa-filetree/file name="实验 3 线性系统的根轨迹分析实验报告 2020" type="pdf" size="7.5 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2021_lmh%28%E4%BB%85%E5%AE%9E%E7%89%A9%E5%AE%9E%E9%AA%8C%29/%E5%AE%9E%E9%AA%8C3%20%E7%BA%BF%E6%80%A7%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A0%B9%E8%BD%A8%E8%BF%B9%E5%88%86%E6%9E%90%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A2020.pdf" >}}
{{< hoa-filetree/file name="实验 4 系统频域特性测试与分析实验报告更正版" type="pdf" size="4.0 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2021_lmh%28%E4%BB%85%E5%AE%9E%E7%89%A9%E5%AE%9E%E9%AA%8C%29/%E5%AE%9E%E9%AA%8C4%20%E7%B3%BB%E7%BB%9F%E9%A2%91%E5%9F%9F%E7%89%B9%E6%80%A7%E6%B5%8B%E8%AF%95%E4%B8%8E%E5%88%86%E6%9E%90%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E6%9B%B4%E6%AD%A3%E7%89%88.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2021_lym(仅上机实验)" date="" state="closed" >}}
{{< hoa-filetree/file name="第一次上机报告 - 刘宇明" type="docx" size="339.3 KB" date="2025/01/18" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2021_lym%28%E4%BB%85%E4%B8%8A%E6%9C%BA%E5%AE%9E%E9%AA%8C%29/%E7%AC%AC%E4%B8%80%E6%AC%A1%E4%B8%8A%E6%9C%BA%E6%8A%A5%E5%91%8A-%E5%88%98%E5%AE%87%E6%98%8E.docx" >}}
{{< hoa-filetree/file name="自控上机 2" type="docx" size="1.5 MB" date="2025/01/18" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2021_lym%28%E4%BB%85%E4%B8%8A%E6%9C%BA%E5%AE%9E%E9%AA%8C%29/%E8%87%AA%E6%8E%A7%E4%B8%8A%E6%9C%BA2.docx" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2022_FWI" date="" state="closed" >}}
{{< hoa-filetree/file name="自控 A 上机 1 报告" type="pdf" size="816.4 KB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_FWI/%E8%87%AA%E6%8E%A7A%E4%B8%8A%E6%9C%BA1%E6%8A%A5%E5%91%8A.pdf" >}}
{{< hoa-filetree/file name="自控 A 上机 2 报告" type="pdf" size="1.9 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_FWI/%E8%87%AA%E6%8E%A7A%E4%B8%8A%E6%9C%BA2%E6%8A%A5%E5%91%8A.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2022_Tintin" date="" state="closed" >}}
{{< hoa-filetree/folder name="上机 1" date="" state="closed" >}}
{{< hoa-filetree/file name="SecondOrder" type="m" size="162 bytes" date="2025/01/18" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E4%B8%8A%E6%9C%BA1/SecondOrder.m" >}}
{{< hoa-filetree/file name="first_order" type="slx" size="18.7 KB" date="2025/01/18" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E4%B8%8A%E6%9C%BA1/first_order.slx" >}}
{{< hoa-filetree/file name="第一次上机" type="docx" size="590.8 KB" date="2025/01/18" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E4%B8%8A%E6%9C%BA1/%E7%AC%AC%E4%B8%80%E6%AC%A1%E4%B8%8A%E6%9C%BA.docx" >}}
{{< hoa-filetree/file name="自控 A 上机 1.一二阶系统时域分析" type="docx" size="8.5 MB" date="2025/01/18" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E4%B8%8A%E6%9C%BA1/%E8%87%AA%E6%8E%A7A%E4%B8%8A%E6%9C%BA1.%E4%B8%80%E4%BA%8C%E9%98%B6%E7%B3%BB%E7%BB%9F%E6%97%B6%E5%9F%9F%E5%88%86%E6%9E%90.docx" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="上机 2" date="" state="closed" >}}
{{< hoa-filetree/file name="ex1" type="m" size="156 bytes" date="2025/01/18" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E4%B8%8A%E6%9C%BA2/ex1.m" >}}
{{< hoa-filetree/file name="ex2" type="m" size="188 bytes" date="2025/01/18" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E4%B8%8A%E6%9C%BA2/ex2.m" >}}
{{< hoa-filetree/file name="rlocus" type="m" size="171 bytes" date="2025/01/18" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E4%B8%8A%E6%9C%BA2/rlocus.m" >}}
{{< hoa-filetree/file name="testbode" type="m" size="119 bytes" date="2025/01/18" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E4%B8%8A%E6%9C%BA2/testbode.m" >}}
{{< hoa-filetree/file name="testnyquist" type="m" size="109 bytes" date="2025/01/18" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E4%B8%8A%E6%9C%BA2/testnyquist.m" >}}
{{< hoa-filetree/file name="图片" type="zip" size="265.2 KB" date="2025/01/18" icon="icons/zip.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E4%B8%8A%E6%9C%BA2/%E5%9B%BE%E7%89%87.zip" >}}
{{< hoa-filetree/file name="自控 A 上机 2.一根轨迹分析和 Bode 图分析" type="pdf" size="2.2 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E4%B8%8A%E6%9C%BA2/%E8%87%AA%E6%8E%A7A%E4%B8%8A%E6%9C%BA2.%E4%B8%80%E6%A0%B9%E8%BD%A8%E8%BF%B9%E5%88%86%E6%9E%90%E5%92%8CBode%E5%9B%BE%E5%88%86%E6%9E%90.pdf" >}}
{{< hoa-filetree/file name="自控 A 上机 2.报告" type="docx" size="1.4 MB" date="2025/01/18" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E4%B8%8A%E6%9C%BA2/%E8%87%AA%E6%8E%A7A%E4%B8%8A%E6%9C%BA2.%E6%8A%A5%E5%91%8A.docx" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="实验 1" date="" state="closed" >}}
{{< hoa-filetree/file name="图片" type="zip" size="166.5 KB" date="2025/01/18" icon="icons/zip.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E5%AE%9E%E9%AA%8C1/%E5%9B%BE%E7%89%87.zip" >}}
{{< hoa-filetree/file name="实验 1 典型系统的时域响应实验报告 2022" type="docx" size="501.7 KB" date="2025/01/18" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E5%AE%9E%E9%AA%8C1/%E5%AE%9E%E9%AA%8C1%20%E5%85%B8%E5%9E%8B%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%97%B6%E5%9F%9F%E5%93%8D%E5%BA%94%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A2022.docx" >}}
{{< hoa-filetree/file name="实验 1 典型系统的时域响应实验指导书 2022" type="docx" size="3.8 MB" date="2025/01/18" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E5%AE%9E%E9%AA%8C1/%E5%AE%9E%E9%AA%8C1%20%E5%85%B8%E5%9E%8B%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%97%B6%E5%9F%9F%E5%93%8D%E5%BA%94%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A62022.docx" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="实验 2" date="" state="closed" >}}
{{< hoa-filetree/file name="图片" type="zip" size="107.3 KB" date="2025/01/18" icon="icons/zip.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E5%AE%9E%E9%AA%8C2/%E5%9B%BE%E7%89%87.zip" >}}
{{< hoa-filetree/file name="实验 2 系统的稳定性分析 (连续 + 离散) 实验报告 2022" type="docx" size="506.3 KB" date="2025/01/18" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E5%AE%9E%E9%AA%8C2/%E5%AE%9E%E9%AA%8C2%20%E7%B3%BB%E7%BB%9F%E7%9A%84%E7%A8%B3%E5%AE%9A%E6%80%A7%E5%88%86%E6%9E%90%28%E8%BF%9E%E7%BB%AD%2B%E7%A6%BB%E6%95%A3%29%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A2022.docx" >}}
{{< hoa-filetree/file name="实验 2 系统的稳定性分析 (连续 + 离散) 实验指导书 2022" type="pdf" size="5.1 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E5%AE%9E%E9%AA%8C2/%E5%AE%9E%E9%AA%8C2%20%E7%B3%BB%E7%BB%9F%E7%9A%84%E7%A8%B3%E5%AE%9A%E6%80%A7%E5%88%86%E6%9E%90%28%E8%BF%9E%E7%BB%AD%2B%E7%A6%BB%E6%95%A3%29%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A62022.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="实验 3" date="" state="closed" >}}
{{< hoa-filetree/file name="图片" type="zip" size="241.9 KB" date="2025/01/18" icon="icons/zip.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E5%AE%9E%E9%AA%8C3/%E5%9B%BE%E7%89%87.zip" >}}
{{< hoa-filetree/file name="实验 3 线性系统的根轨迹分析实验报告 2022" type="docx" size="716.0 KB" date="2025/01/18" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E5%AE%9E%E9%AA%8C3/%E5%AE%9E%E9%AA%8C3%20%E7%BA%BF%E6%80%A7%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A0%B9%E8%BD%A8%E8%BF%B9%E5%88%86%E6%9E%90%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A2022.docx" >}}
{{< hoa-filetree/file name="实验 3 线性系统的根轨迹分析实验指导书" type="pdf" size="1.1 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E5%AE%9E%E9%AA%8C3/%E5%AE%9E%E9%AA%8C3%20%E7%BA%BF%E6%80%A7%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A0%B9%E8%BD%A8%E8%BF%B9%E5%88%86%E6%9E%90%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC%E4%B9%A6.pdf" >}}
{{< hoa-filetree/file name="实验 3：驱动器速度模式修改方法" type="pdf" size="504.3 KB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E5%AE%9E%E9%AA%8C3/%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E9%A9%B1%E5%8A%A8%E5%99%A8%E9%80%9F%E5%BA%A6%E6%A8%A1%E5%BC%8F%E4%BF%AE%E6%94%B9%E6%96%B9%E6%B3%95.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="实验 4" date="" state="closed" >}}
{{< hoa-filetree/file name="实验 4 系统频域特性测试与分析" type="pdf" size="1.0 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E5%AE%9E%E9%AA%8C4/%E5%AE%9E%E9%AA%8C4%20%E7%B3%BB%E7%BB%9F%E9%A2%91%E5%9F%9F%E7%89%B9%E6%80%A7%E6%B5%8B%E8%AF%95%E4%B8%8E%E5%88%86%E6%9E%90.pdf" >}}
{{< hoa-filetree/file name="实验 4 系统频域特性测试与分析实验报告 2022" type="docx" size="404.7 KB" date="2025/01/18" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2022_Tintin/%E5%AE%9E%E9%AA%8C4/%E5%AE%9E%E9%AA%8C4%20%E7%B3%BB%E7%BB%9F%E9%A2%91%E5%9F%9F%E7%89%B9%E6%80%A7%E6%B5%8B%E8%AF%95%E4%B8%8E%E5%88%86%E6%9E%90%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A2022.docx" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2024_psp" date="" state="closed" >}}
{{< hoa-filetree/folder name="上机实验" date="" state="closed" >}}
{{< hoa-filetree/folder name="上机一" date="" state="closed" >}}
{{< hoa-filetree/file name="lab1" type="m" size="6.5 KB" date="2025/06/25" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2024_psp/%E4%B8%8A%E6%9C%BA%E5%AE%9E%E9%AA%8C/%E4%B8%8A%E6%9C%BA%E4%B8%80/lab1.m" >}}
{{< hoa-filetree/file name="lab1" type="slx" size="81.3 KB" date="2025/06/25" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2024_psp/%E4%B8%8A%E6%9C%BA%E5%AE%9E%E9%AA%8C/%E4%B8%8A%E6%9C%BA%E4%B8%80/lab1.slx" >}}
{{< hoa-filetree/file name="上机 1 一二阶系统时域分析-psp" type="docx" size="1.7 MB" date="2025/06/25" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2024_psp/%E4%B8%8A%E6%9C%BA%E5%AE%9E%E9%AA%8C/%E4%B8%8A%E6%9C%BA%E4%B8%80/%E4%B8%8A%E6%9C%BA1%20%E4%B8%80%E4%BA%8C%E9%98%B6%E7%B3%BB%E7%BB%9F%E6%97%B6%E5%9F%9F%E5%88%86%E6%9E%90-psp.docx" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="上机二" date="" state="closed" >}}
{{< hoa-filetree/file name="lab2_1" type="m" size="2.1 KB" date="2025/06/25" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2024_psp/%E4%B8%8A%E6%9C%BA%E5%AE%9E%E9%AA%8C/%E4%B8%8A%E6%9C%BA%E4%BA%8C/lab2_1.m" >}}
{{< hoa-filetree/file name="lab2_2" type="m" size="5.8 KB" date="2025/06/25" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2024_psp/%E4%B8%8A%E6%9C%BA%E5%AE%9E%E9%AA%8C/%E4%B8%8A%E6%9C%BA%E4%BA%8C/lab2_2.m" >}}
{{< hoa-filetree/file name="上机 2 根轨迹分析和 Bode 图分析-psp" type="docx" size="4.6 MB" date="2025/06/25" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2024_psp/%E4%B8%8A%E6%9C%BA%E5%AE%9E%E9%AA%8C/%E4%B8%8A%E6%9C%BA%E4%BA%8C/%E4%B8%8A%E6%9C%BA2%20%E6%A0%B9%E8%BD%A8%E8%BF%B9%E5%88%86%E6%9E%90%E5%92%8CBode%E5%9B%BE%E5%88%86%E6%9E%90-psp.docx" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="实物实验" date="" state="closed" >}}
{{< hoa-filetree/file name="lab4_analyse_data" type="py" size="2.7 KB" date="2025/06/25" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2024_psp/%E5%AE%9E%E7%89%A9%E5%AE%9E%E9%AA%8C/lab4_analyse_data.py" >}}
{{< hoa-filetree/file name="实验 1 典型系统的时域响应实验-psp" type="docx" size="2.0 MB" date="2025/06/25" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2024_psp/%E5%AE%9E%E7%89%A9%E5%AE%9E%E9%AA%8C/%E5%AE%9E%E9%AA%8C1%20%E5%85%B8%E5%9E%8B%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%97%B6%E5%9F%9F%E5%93%8D%E5%BA%94%E5%AE%9E%E9%AA%8C-psp.docx" >}}
{{< hoa-filetree/file name="实验 2 系统的稳定性分析 (连续 + 离散)-psp" type="docx" size="567.2 KB" date="2025/06/25" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2024_psp/%E5%AE%9E%E7%89%A9%E5%AE%9E%E9%AA%8C/%E5%AE%9E%E9%AA%8C2%20%E7%B3%BB%E7%BB%9F%E7%9A%84%E7%A8%B3%E5%AE%9A%E6%80%A7%E5%88%86%E6%9E%90%28%E8%BF%9E%E7%BB%AD%2B%E7%A6%BB%E6%95%A3%29-psp.docx" >}}
{{< hoa-filetree/file name="实验 3 线性系统的根轨迹分析-psp" type="docx" size="861.3 KB" date="2025/06/25" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2024_psp/%E5%AE%9E%E7%89%A9%E5%AE%9E%E9%AA%8C/%E5%AE%9E%E9%AA%8C3%20%E7%BA%BF%E6%80%A7%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A0%B9%E8%BD%A8%E8%BF%B9%E5%88%86%E6%9E%90-psp.docx" >}}
{{< hoa-filetree/file name="实验 4 系统频域特性测试与分析-psp" type="docx" size="399.8 KB" date="2025/06/25" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2024_psp/%E5%AE%9E%E7%89%A9%E5%AE%9E%E9%AA%8C/%E5%AE%9E%E9%AA%8C4%20%E7%B3%BB%E7%BB%9F%E9%A2%91%E5%9F%9F%E7%89%B9%E6%80%A7%E6%B5%8B%E8%AF%95%E4%B8%8E%E5%88%86%E6%9E%90-psp.docx" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="2025_Gaster" date="" state="closed" >}}
{{< hoa-filetree/file name="系统与控制上机 1 报告-Gaster" type="pdf" size="1.5 MB" date="2025/06/28" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2025_Gaster/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%B8%8A%E6%9C%BA1%E6%8A%A5%E5%91%8A-Gaster.pdf" >}}
{{< hoa-filetree/file name="系统与控制上机 2 报告-Gaster" type="pdf" size="2.4 MB" date="2025/06/28" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2025_Gaster/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E4%B8%8A%E6%9C%BA2%E6%8A%A5%E5%91%8A-Gaster.pdf" >}}
{{< hoa-filetree/file name="系统与控制实验 1 报告-Gaster" type="pdf" size="2.2 MB" date="2025/06/28" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2025_Gaster/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E5%AE%9E%E9%AA%8C1%E6%8A%A5%E5%91%8A-Gaster.pdf" >}}
{{< hoa-filetree/file name="系统与控制实验 2 报告（仅连续部分）-Gaster" type="pdf" size="1.4 MB" date="2025/06/28" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2025_Gaster/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E5%AE%9E%E9%AA%8C2%E6%8A%A5%E5%91%8A%EF%BC%88%E4%BB%85%E8%BF%9E%E7%BB%AD%E9%83%A8%E5%88%86%EF%BC%89-Gaster.pdf" >}}
{{< hoa-filetree/file name="系统与控制实验 3 报告-Gaster" type="pdf" size="1.8 MB" date="2025/06/28" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2025_Gaster/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E5%AE%9E%E9%AA%8C3%E6%8A%A5%E5%91%8A-Gaster.pdf" >}}
{{< hoa-filetree/file name="系统与控制实验 4 报告-Gaster" type="pdf" size="1.6 MB" date="2025/06/28" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/labs/2025_Gaster/%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E5%AE%9E%E9%AA%8C4%E6%8A%A5%E5%91%8A-Gaster.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="notes" date="" state="closed" >}}
{{< hoa-filetree/file name="2022_自控原理 A 笔记" type="pdf" size="74.8 MB" date="2025/01/18" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/notes/2022_%E8%87%AA%E6%8E%A7%E5%8E%9F%E7%90%86A%E7%AC%94%E8%AE%B0.pdf" >}}
{{< hoa-filetree/file name="2023_Spar Océsel_自控原理" type="apkg" size="1.1 MB" date="2025/01/18" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/notes/2023_Spar%20Oce%CC%81sel_%E8%87%AA%E6%8E%A7%E5%8E%9F%E7%90%86.apkg" >}}
{{< hoa-filetree/file name="2025 春系统与控制笔记-Gaster" type="pdf" size="2.8 MB" date="2025/07/17" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/notes/2025%20%E6%98%A5%E7%B3%BB%E7%BB%9F%E4%B8%8E%E6%8E%A7%E5%88%B6%E7%AC%94%E8%AE%B0-Gaster.pdf" >}}
{{< hoa-filetree/file name="2025 自控 A 笔记" type="pdf" size="4.5 MB" date="2025/11/24" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/notes/2025%E8%87%AA%E6%8E%A7A%E7%AC%94%E8%AE%B0.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="slides" date="" state="closed" >}}
{{< hoa-filetree/file name="2023 课件合订本" type="pdf" size="134 bytes" date="2024/10/30" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3001A/raw/main/slides/2023%E8%AF%BE%E4%BB%B6%E5%90%88%E8%AE%A2%E6%9C%AC.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/container >}}

## 参与

《HITSZ 自动化课程攻略共享计划》是所有同学都可以参与编写的，如果你有好的笔记或者资料，欢迎前往我们的 [GitHub](https://github.com/HITSZ-OpenAuto) 进行参与，也可以发邮件至 [📮hi@hoa.moe](mailto:hi@hoa.moe) 联系我们，我们会在收到的第一时间进行答复。

{{< callout type="" >}}
  © 版权声明：[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-nc-sa/4.0/)
{{< /callout >}}

