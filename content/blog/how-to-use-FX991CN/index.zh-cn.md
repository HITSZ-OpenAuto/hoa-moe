---
title: 卡西欧 FX-991CNX 计算器使用指南
description: 更适合自动化学子的计算器使用教程
date: 2024-07-13
authors:
  - name: drq-48
    link: https://github.com/drq-48
    image: https://github.com/drq-48.png
excludeSearch: false
math: true
tags:
  - 学习
  - 数学
  - 计算器
---

​期末月期间在自救群里看到了一些关于卡西欧 FX-991CNX 计算器使用的讨论，才发觉其实有很多同学不那么擅长使用该计算器。

本人高中时曾经旁听物竞课程，记得当时的第一课既不是运动学，也不是速通微积分，而是 991 使用教学，本人从此开始使用这款功能完备的计算器，也算是略有一些经验。

​目前，无论是 991 自带的说明书还是网上的教程，对该计算器的介绍都相当全面，但是作为一名自动化学生，这些教程要么过于基础，要么过于驳杂，很难让人有看下去的欲望。

因此，本文旨在为大家奉上更简洁、更实用、更适合自动化学子的计算器使用教程。本文也可作速查手册使用，可先翻阅右侧的目录以大致了解文档结构。本人对该计算器的使用也并非尽善尽美，欢迎各位批评、指正。

---

# **更适合自动化学子的计算器使用教程**

## 1. 标记与指示符简介

​991 的功能按键存在非常多的复用，即一个按键对应多个功能，不同功能的图标颜色不同。例如

- sin 上面有黄色的 <font face='黑体' color=#DEB887 size=4>sin<sup>-1</sup></font>、红色的 <font face='黑体' color=#DC143C size=4>D</font>，D 被蓝色中括号<font face='黑体' color=#00BFFF size=4>⌈ ⌉</font>括起来；

- ENG 上面有紫色的 <font face='黑体' color=#9400D3 size=4>i</font>、
黄色的 <font face='黑体' color=#DEB887 size=4>∠</font>，
黄色的箭头 <font face='黑体' color=#DEB887 size=4>←</font>
由 <font face='黑体' color=#9400D3 size=4>i</font>
指向 <font face='黑体' color=#DEB887 size=4>∠</font>，
<font face='黑体' color=#DEB887 size=4>∠</font>
被紫色中括号 <font face='黑体' color=#9400D3 size=4>⌈ ⌉</font>
括起来。

它们调用的方式不尽相同。
1. 黄色标记的功能需要先按
<font face='黑体' color=#DEB887 size=4>SHIFT</font>
再按对应按键，以下记为
<font face='黑体' color=#DEB887 size=4>SHIFT+xx(yy)</font>，括号内为对应的按键标记；
2. 红色标记的功能需要先按
<font face='黑体' color=#DC143C size=4>ALPHA</font>
再按对应按键，以下记为
<font face='黑体' color=#DC143C size=4>ALPHA+xx(yy)</font>，括号内为对应的按键标记；
3. 蓝色标记的功能在基数模式里调用；
4. 紫色标记的功能在复数模式里调用。

​部分按键按下、部分功能启用或部分设置变化时，屏幕最上方会出现对应的提示符。常用的提示符如下：

1. 按下 <font face='黑体' color=#DEB887 size=4>SHIFT</font> 会出现 S，
2. 按下 <font face='黑体' color=#DC143C size=4>ALPHA</font> 会出现 A；
3. 按下 STO 会出现 **→**x，表示计算器正在等待输入变量名称（ABCDEFxyM），从而为该变量赋值；
4. D, R, G 表示缺省的角度单位，分别为角度、弧度、百分度，可在设置的角度单位子菜单中切换；
5. FIX, SCI 分别表示结果输出格式为固定位数的小数或者有效数字，可在设置中的显示格式子菜单切换；
6. i 和 ∠ 分别表示复数的默认输出格式为 $a+bi$ 或 $r∠θ$，可在设置中的复数子菜单中切换。

## 2. 按键简介

​此处略去各种较为基础的运算按键，如加减乘除、指数对数、三角函数相关、定积分等，只讲一些可能被忽视的功能，按照个人认为的重要性依次排列。

### 数据记录、查询与调用

<table><tr><td bgcolor=orange>很常用</td></tr></table>

​STO 与 <font face='黑体' color=#DEB887 size=4>SHIFT+STO</font>，一般用于记录中间变量以便计算中调用，善用该功能可以简化表达式。

​对于输出的结果，按下 STO，会出现 **→**x。再按任意有变量标记（<font face='黑体' color=#DC143C size=4>ABCDEFMxy</font>）的按键，则该值会被记录至该变量下；

按下 <font face='黑体' color=#DEB887 size=4>SHIFT+STO</font>，则会显示所有变量的赋值，此时再按任意有变量标记（<font face='黑体' color=#DC143C size=4>ABCDEFMxy</font>）的按键，则会在表达式中输入该字母；

也可通过 <font face='黑体' color=#DC143C size=4>ALPHA+任意有变量标记（ABCDEFMxy）的按键</font> 输入该字母。

**e.g.**

输入 1，按下 STO，出现 **→**x，按下 sin（它对应的变量为 <font face='黑体' color=#DC143C size=4>D</font>），则 D 被赋为 1；

按下 <font face='黑体' color=#DEB887 size=4>SHIFT+STO</font> 显示所有变量的赋值，若 D=1，则表明赋值成功。

此时按下 sin（它对应的变量为 <font face='黑体' color=#DC143C size=4>D</font>），则会输入 D，按下 =，结果为 1；按下 <font face='黑体' color=#DC143C size=4>ALPHA+sin（D）</font> 同样可以输入 D，按下 =，结果为 1。

### 科学常数

<table><tr><td bgcolor=orange>较常用</td></tr></table>

​<font face='黑体' color=#DEB887 size=4>SHIFT+7（科学常数）</font>，包括通用常数、电磁常数、原子与核常数、物理化学常数等。

### 分数小数互化与带分数假分数互化

<table><tr><td bgcolor=orange>较常用</td></tr></table>

​S⇔D 与 <font face='黑体' color=#DEB887 size=4>SHIFT+S⇔D</font>。

**e.g.**

若结果为假分数，按下 <font face='黑体' color=#DEB887 size=4>SHIFT+S⇔D</font>，会使其变为带分数，反之亦然；
若结果为分数，按下 S⇔D 会使其变为小数，反之亦然。

### 答案

<table><tr><td bgcolor=orange>较常用</td></tr></table>

​ANS。记录了上一个表达式的结果。

### 选项

<table><tr><td bgcolor=orange>较常用</td></tr></table>

​OPTN。在默认的计算模式下，输入角度的单位默认为设置中的单位，而 OPTN 中可输入角度单位（°、<sup>r</sup>、<sup>g</sup>），将输入角度的单位设置为输入的单位。

在其他模式下会有更多不同功能，在后面模式简介中介绍，此处按下不表。

​**e.g.**

若设置中的角度单位为度，输入 1，按 OPTN 进入选项，按 2 进入角度单位子菜单，再按 1 输入 °，按 =，则输出为 1；

若在角度单位子菜单中选择按 2 输入 <sup>r</sup>，则按下 = 后输出约为 57.3（$1 rad ≈ 57.3°$）。

### 直角坐标与极坐标互化

<table><tr><td bgcolor=orange>不常用</td></tr></table>

​<font face='黑体' color=#DEB887 size=4>SHIFT++（Pol）</font>
与 <font face='黑体' color=#DEB887 size=4>SHIFT+-（Rec）</font>。

**e.g.**

以直角坐标化为极坐标为例，输入 Pol，再输入 $x, y$ 坐标，两者之间以逗号
<font face='黑体' color=#DEB887 size=4>SHITF+ )（,）</font>隔开，则输出对应的 $r$ 和 $θ$。

### 单位换算

<table><tr><td bgcolor=orange>不常用</td></tr></table>

​		<font face='黑体' color=#DEB887 size=4>SHIFT+8（单位换算）</font>。一般仅用于压力和速度的换算。

**e.g.**

输入待换算的数据，按下 <font face='黑体' color=#DEB887 size=4>SHIFT+8（单位换算）</font>，找到所需的换算式，按下对应的数字，则会输入该换算式，再按 =，则会输出换算结果。

### 质因数分解

<table><tr><td bgcolor=orange>不常用</td></tr></table>

​<font face='黑体' color=#DEB887 size=4>SHIFT+°'"（FACT）</font>。

**e.g.**

输入 10 位及以内的整数，按下 =，再按
<font face='黑体' color=#DEB887 size=4>SHIFT+°'"（FACT）</font>，则会输出分解结果。

注意，计算器无法分解过大的整数（7 位及以上），此类整数会用括号标注。

## 3. 模式简介

​	此处仅介绍常用模式及其功能，大部分功能都集成在 OPTN 选项下，可以在相应模式下按 OPTN 查看。菜单中可以切换模式。

### 计算

<table><tr><td bgcolor=orange>最常用</td></tr></table>

​默认模式，无特殊功能。

### 复数

<table><tr><td bgcolor=orange>很常用</td></tr></table>

​可计算辐角、共轭，提取实部、虚部，进行直角坐标与极坐标转换。**不能计算 $e^{iθ}$！**

​在复数模式下，按下 ENG 会输入 i，按下
<font face='黑体' color=#DEB887 size=4>SHIFT+ENG（∠）</font>
会输入 ∠。

### 矩阵

<table><tr><td bgcolor=orange>很常用</td></tr></table>

​可定义、编辑最大 4 x 4 的矩阵，计算矩阵加法、乘法，乘方、逆，行列式、转置，记录上一个矩阵表达式的答案，输入单位矩阵。**不能求矩阵的秩！**

​定义、编辑矩阵时，需要在相应位置输入各元素的值，输入完成之后按 = 结束对该元素值的编辑。所有元素编辑完成之后，可以直接按 AC 退出编辑、进入计算，也可以按 OPTN 选择继续定义、编辑其他矩阵，或者进入计算。

​定义或编辑方阵后，按 OPTN 进入选项，选择相应的方阵输入，按 x<sup>-1</sup>，然后按 =，即可求出该方阵的逆矩阵。

同理，输入方阵后，按
x<sup>2</sup> 或者 <font face='黑体' color=#DEB887 size=4>SHIFT+x<sup>2</sup>（x<sup>3</sup>）</font>，然后按 =，即可求出该方阵的平方或者立方。

### 向量

<table><tr><td bgcolor=orange>较常用</td></tr></table>

​可定义、编辑最大三维向量，计算向量加法、乘法、内积、夹角、模长。

​定义、编辑向量时，需要在相应位置输入各元素的值，输入完成之后按 = 结束对该元素值的编辑。

所有元素编辑完成之后，可以直接按 AC 退出编辑、进入计算，也可以按 OPTN 选择继续定义、编辑其他向量，或者进入计算。

​定义或编辑向量后，按<font face='黑体' color=#DEB887 size=4>SHIFT+（（ABS）</font>，再按 OPTN 进入选项，选择相应的向量输入，按 =，即可求出该向量的模长；

按 OPTN 进入选项，选择两个向量形成的夹角（输入 Angle），然后输入相应的向量，两者之间以逗号
<font face='黑体' color=#DEB887 size=4>SHITF+)（,）</font>
隔开，按 =，即可求出两向量之间的夹角。

### 方程

<table><tr><td bgcolor=orange>很常用</td></tr></table>

​可求解四元及以下的一次线性方程组、四次及以下的一元线性方程。对于二次方程，还可以求解相应二次函数的最值大小和最值点。

### 不等式

<table><tr><td bgcolor=orange>较常用</td></tr></table>

​可求解四次及以下的一元不等式。

### 统计

<table><tr><td bgcolor=orange>较常用</td></tr></table>

​可计算期望、方差、标准差等统计数据，还可以用最小二乘法，根据指定形式函数进行拟合。

### 基数

<table><tr><td bgcolor=orange>不常用</td></tr></table>

​用于 2、8、10、16 进制之间的转换。

DEC 表示十进制，HEX 表示十六进制，BIN 表示二进制，OCT 表示八进制。

​在十六进制（HEX）模式下，按下(-)、°'"、x<sup>-1</sup>、sin、cos、tan 会分别输入 A、B、C、D、E、F。

## 4. 设置简介

​<font face='黑体' color=#DEB887 size=4>SHIFT+菜单(设置)</font>
即可进入设置，设置一般默认即可，也可以按需调整。
<font face='黑体' color=#DEB887 size=4>SHIFT+9(复位)</font>
可将所有设置数据重置为默认值。

以下介绍顺序按照个人认为的重要性依次排列。

### 角度单位

<table><tr><td bgcolor=orange>经常需要调整</td></tr></table>

​可将输出默认角度单位设置为角度、弧度或者百分度，对应提示符分别为 D、R、G，默认为角度 D，一般只用前两个。

### 复数

<table><tr><td bgcolor=orange>偶尔需要调整</td></tr></table>

​可将输出复数结果的默认格式设置为 $a+bi$ 或者 $ρ∠θ$，对应提示符分别为 i 与 ∠，默认为 $a+bi$。

### 分数结果

<table><tr><td bgcolor=orange>一般无需调整</td></tr></table>

​可将输出分数结果的默认格式设置为带分数或者假分数，默认为假分数。

### 方程/函数

<table><tr><td bgcolor=orange>一般无需调整</td></tr></table>

​		可打开/关闭高次方程复数结果的输出，默认为开。

### 输入/输出

<table><tr><td bgcolor=orange>一般无需调整</td></tr></table>

​可设置输入 / 输出默认格式，默认为数学输入 / 数学输出，一般默认即可。

## 5. 常用技巧

此处为本人一些小小的心得体会，欢迎补充。

### 解单变量方程

​<font face='黑体' color=#DC143C size=4>ALPHA+CALC（=）</font>
输入等号，等式两侧输入单变量表达式，<font face='黑体' color=#DEB887 size=4>SHIFT+CALC（SOLVE）</font>
输入变量迭代初值后求解距离初值最近的解。

若解距离初值过远可能显示无解，求解过程可通过 AC 打断。

可用于求解非线性方程、高次方程。
注意：对于有解的方程，如果迭代初值不合适，可能会提示无解。

​**e.g.**

输入 ln(x)，<font face='黑体' color=#DC143C size=4>ALPHA+CALC（=）</font>输入等号，再输入 1，按下
<font face='黑体' color=#DEB887 size=4>SHIFT+CALC（SOLVE）</font>后输入变量迭代初值 0，按下 = 即可求解，解得 x = 0。

### 含参表达式求解

​输入含参数的表达式，按下 CALC 后可依次输入各参数的值，最后得到计算结果。

可使用此功能快速求得单变量方程的数值解，在部分情况下（如自控理论 B 的频率特性校正计算）有奇效，具体操作如下：
1. 自己化简等式，使等式一侧只含常量，另一侧为含参表达式；
2. 输入含参表达式，通过前述 CALC 功能求出参量取不同值时的结果；
3. 结果与常量足够接近时，参量的值即可视为近似解。

该技巧相当于手动迭代求解代数方程的数值解，每次迭代只需 3 次按键操作（CALC, 数值, =），若能熟练掌握，求近似数值解的速度可以比前述 solve 功能快。

​**e.g.**

已知 $90-\arctan(0.5x)+\arctan(0.1x)-\arctan(0.01x)-\arctan(0.005x)=0$，求解 $x$。

解：
1. 输入表达式 $90 - \tan^{-1}(0.5x)+ \tan^{-1}(0.1x) - \tan^{-1}(0.01x)- \tan^{-1}(0.005x)$。
2. 按下 CALC 后输入 0（即变量 x 的值），按下 = 后即可求得 x = 0 时表达式的值。
3. 重复前述过程，可以求出参量取不同值时表达式的结果，当结果与 0 较为接近时，此时 x 的值即可作为近似解。

## 一些链接

如果想更全面地了解 991 的基础功能，可以参考
- [CASIO fx-991CN X 说明书 - CASIO](https://support.casio.com/cn/manual/manualresult.php?cid=004009101&keyword=)
- [师生资料下载 - CASIO](https://www.casio.com.cn/support/calculators/content/download/shishengziliao/)

如果想了解各路大神在 991 上整出来的花活，可以参考 [fx-991cnx计算器:利用ROP漏洞执行任意代码 - 知乎](https://zhuanlan.zhihu.com/p/618704031)。
