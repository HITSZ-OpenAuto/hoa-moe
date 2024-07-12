---
title: （必修）自动控制实践B
weight: 39
toc: true
editURL: "https://github.com/HITSZ-OpenAuto/AUTO3002B/edit/main/README.md"
math: true
---
最近由 吴俊达 更新于 2024.6.25，更新内容：增加复习笔记一份


![Static Badge](https://img.shields.io/badge/%E8%80%83%E8%AF%95%E8%AF%BE-red)![Static Badge](https://img.shields.io/badge/%E5%AD%A6%E5%88%86-6-moccasin)

![Static Badge](https://img.shields.io/badge/%E6%88%90%E7%BB%A9%E6%9E%84%E6%88%90-gold)
![Static Badge](https://img.shields.io/badge/作业-10%25-wheat)
![Static Badge](https://img.shields.io/badge/实验-40%25-wheat)
![Static Badge](https://img.shields.io/badge/%E6%9C%9F%E6%9C%AB%E8%80%83%E8%AF%95-50%25-wheat)


## 授课教师

- 教师 1: 董广忠
  - 授课风格：
  - 听课建议：

## 关于考试

- 考试难度：较难
- 说明：注意老师给出的重点。同时对于理论部分的学习主要是一些固定的模型，注意公式推导和转换即可。实践部分听重点，过一遍PPT即可。

> 文/[xander-2077](https://github.com/xander-2077)

## 实验

21级实验课的内容是 STM32 开发，实验涵盖了：GPIO、外部中断、串口通信、DMA 等功能的上手。开发板的 MCU 型号是 STM32F407ZGT6，软件是 MDK v5 + CubeMX。

实验软件所使用的 CubeMX 是 STM32Cube ———— 目前 STM32 最主流的开发方式的重要一环。而2019年推出的 STM32CubeIDE，则是这个生态系统的集大成者。

与 MDK 不同的是，STM32CubeIDE 还提供对 MacOS 或者 Linux 操作系统的支持。我非常推荐大家使用 STM32CubeIDE 这个 All in one 的软件（包含了 CubeMX，可以不用单独下载）进行使用。

以下是一些有用的链接：

- [STM32StepByStep:Step2 Blink LED](https://wiki.stmicroelectronics.cn/stm32mcu/wiki/STM32StepByStep:Step2_Blink_LED)：通过点灯，快速熟悉 IDE 的开发流程。
- [CH341 串口驱动](https://www.wch-ic.com/downloads/CH341SER_EXE.html)：除了老师一般会发的 Windows 版本外，还含有 MacOS 和 Linux 的版本。
- [printf 重定向](https://github.com/STMicroelectronics/STM32CubeH7/blob/master/Projects/STM32H743I-EVAL/Examples/UART/UART_Printf/Src/main.c): STM32 官方文档中的重定向方法。

> 文/[Kowyo](https://github.com/kowyo)

 


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
    {{< filetree/file name="☆老师官方版stm32题库★.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E2%98%86%E8%80%81%E5%B8%88%E5%AE%98%E6%96%B9%E7%89%88stm32%E9%A2%98%E5%BA%93%E2%98%85.pdf" >}}
    {{< filetree/file name="《黄瑞宁漏出》.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E3%80%8A%E9%BB%84%E7%91%9E%E5%AE%81%E6%BC%8F%E5%87%BA%E3%80%8B.pdf" >}}
    {{< filetree/file name="本部2020答案.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/exams/%E6%9C%AC%E9%83%A82020%E7%AD%94%E6%A1%88.pdf" >}}
  {{< /filetree/folder >}}
  {{< filetree/folder name="notes" state="closed" >}}
    {{< filetree/file name="Revision of Auto-Practical.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/notes/Revision%20of%20Auto-Practical.pdf" >}}
    {{< filetree/file name="自控实践B复习_Tintin.pdf" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO3002B/raw/main/notes/%E8%87%AA%E6%8E%A7%E5%AE%9E%E8%B7%B5B%E5%A4%8D%E4%B9%A0_Tintin.pdf" >}}
  {{< /filetree/folder >}}
{{< /filetree/container >}}

如果你是校内学生，可移步至 <a href='https://open.osa.moe/openauto/AUTO3002B'>open.osa.moe</a> 查看本门课程的电子书、课件和实验软件等。

## 参与

《HITSZ 自动化课程攻略共享计划》是所有同学都可以参与编写的，如果你有好的笔记或者资料，欢迎前往我们的 [GitHub](https://github.com/HITSZ-OpenAuto) 进行参与，也可以发邮件至 [📮hi@hoa.moe](mailto:hi@hoa.moe) 联系我们，我们会在收到的第一时间进行答复。

{{< callout type="" >}}
  © 版权声明：[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-nc-sa/4.0/)
{{< /callout >}}
