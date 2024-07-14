---
title: 卡西欧FX-991CNX计算器使用指南
description: 更适合自动化学子的计算器使用教程
date: 2024-07-13
authors:
  - name: drq-48
    link: https://github.com/MaxwellJay256
    image: https://github.com/MaxwellJay256.png
excludeSearch: false
math: true
tags:
  - 学习

---

​		期末月期间在自救群里看到了一些关于卡西欧FX-991CNX计算器使用的讨论，才发觉其实有很多同学不那么擅长使用该计算器。本人高中时曾经旁听物竞课程，记得当时的第一课既不是运动学，也不是速通微积分，而是991使用教学，本人从此开始使用这款功能完备的计算器，也算是略有一些经验。目前，无论是991自带的说明书还是网上的教程，对该计算器的介绍都相当全面，但是作为一名自动化学子，这些教程要么过于基础，要么过于驳杂，很难让人有看下去的欲望。因此，本文旨在以面向课程的方式，为大家奉上更适合自动化学子的计算器使用教程。本人对该计算器的使用也并非尽善尽美，欢迎各位批评、指正。

---

## **更适合自动化学子的计算器使用教程**

### 1. 标记与指示符简介

​		991的功能按键存在非常多的复用，即一个按键对应多个功能，不同功能的图标颜色不同。比如sin上面有黄色的$\color{olive}{sin<sup>-1</sup>}$、红色的$\color{red}{D}$，D被蓝色中括号$\color{blue}{⌈ ⌉}$括起来；再比如ENG上面有紫色的$\color{purple}{i}$，黄色的$\color{olive}{∠}$，黄色的箭头$\color{olive}{←}$由$\color{purple}{i}$指向$\color{olive}{∠}$，$\color{olive}{∠}$被紫色中括号$\color{purple}{⌈ ⌉}$括起来。它们调用的方式不尽相同：黄色标记的功能需要先按$\color{olive}{SHIFT}$再按对应按键，以下记为$\color{olive}{SHIFT+xx（yy）}$，括号内为对应的按键标记；红色标记的功能需要先按$\color{red}{ALPHA}$再按对应按键，以下记为$\color{red}{ALPHA}+xx（yy）$，括号内为对应的按键标记；蓝色标记的功能在基数模式里调用；紫色标记的功能在复数模式里调用。

​		部分按键按下、部分功能启用或部分设置变化时，屏幕最上方会出现对应的提示符。常用的提示符如下：按下$\color{olive}{SHIFT}$会出现S，按下$\color{red}{ALPHA}$会出现A；按下STO会出现**→**x，表示计算器正在等待输入变量名称（ABCDEFxyM），从而为该变量赋值；D、R、G表示缺省的角度单位，分别为角度、弧度、百分度，可在设置的角度单位子菜单中切换；FIX、SCI分别表示结果输出格式为固定位数的小数或者有效数字，可在设置中的显示格式子菜单切换；i和∠分别表示复数的默认输出格式为a+bi与r∠θ，可在设置中的复数子菜单中切换。

### 2. 按键简介

​		此处略去各种较为基础的运算按键，如加减乘除、指数对数、三角函数相关、定积分等，只讲一些可能被忽视的功能，按照个人认为的重要性依次排列。

#### 数据记录、查询与调用

<table><tr><td bgcolor=orange>非常实用</td></tr></table>

​		STO与$\color{olive}{SHIFT+STO（调用）}$，一般用于记录中间变量以便计算中调用，善用该功能可以简化表达式。

​		对于输出的结果，按下STO，会出现**→**x。再按任意有变量标记（$\color{red}{ABCDEFMxy}$）的按键，则该值会被记录至该变量下；按下$\color{olive}{SHIFT+STO（调用）}$，则会显示所有变量的赋值，此时再按任意有变量标记（$\color{red}{ABCDEFMxy}$）的按键，则会在表达式中输入该字母；也可通过$\color{red}{ALPHA+任意有变量标记（ABCDEFMxy）的按键}$输入该字母。

​		e.g. 输入1，按下STO，出现**→**x，按下sin（它对应的变量为$\color{red}{D}$），则D被赋为1；按下$\color{olive}{SHIFT+STO（调用）}$，则会显示所有变量的赋值，若D=1，则表明赋值成功；此时按下sin（它对应的变量为$\color{red}{D}$），则会输入D，按下=，结果为1；按下$\color{red}{ALPHA+sin（D）}$同样可以输入D，按下=，结果为1。

#### 科学常数

<table><tr><td bgcolor=orange>非常实用</td></tr></table>

​		$\color{olive}{SHIFT+7（科学常数）}$，包括通用常数、电磁常数、物理化学常数等。

#### 分数小数互化与带分数假分数互化

<table><tr><td bgcolor=orange>较常用</td></tr></table>

​		S⇔D与$\color{olive}{SHIFT+S⇔D}$。e.g.若结果为假分数，按下$\color{olive}{SHIFT+S⇔D}$，会使其变为带分数，反之亦然；若结果为分数，按下S⇔D会使其变为小数，反之亦然。

#### 答案

<table><tr><td bgcolor=orange>非较常用</td></tr></table>

​		ANS。记录了上一个表达式的结果。

#### 选项

<table><tr><td bgcolor=orange>较常用</td></tr></table>

​		OPTN。在默认的计算模式下，输入角度的单位默认为设置中的单位，而OPTN中可输入角度单位（°、<sup>r</sup>、<sup>g</sup>），将输入角度的单位设置为输入的单位。在其他模式下会有更多不同功能，在后面模式简介中介绍，此处按下不表。

​		e.g.若设置中的角度单位为度，输入1，按OPTN进入选项，按2进入角度单位子菜单，再按1输入°，按=，则输出为1；若在角度单位子菜单中选择按2输入<sup>r</sup>，则按下=后输出约为57.3（1rad≈57.3°）。

#### 直角坐标与极坐标互化

<table><tr><td bgcolor=orange>不太常用</td></tr></table>

​		$\color{olive}{SHIFT++（Pol）}$与$\color{olive}{SHIFT+-（Rec）}$。e.g.以直角坐标化为极坐标为例，输入Pol，再输入x、y坐标，两者之间以逗号$\color{olive}{SHIFT+）（.）}$隔开，则输出对应的r和θ。

#### 单位换算

<table><tr><td bgcolor=orange>不太常用</td></tr></table>

​		$\color{olive}{SHIFT+8单位换算）}$。一般仅用于压力和速度的换算。e.g.输入待换算的数据，按下$\color{olive}{SHIFT+8单位换算）}$，找到所需的换算式，按下对应的数字，则会输入该换算式，再按=，则会输出换算结果。

#### 质因数分解

<table><tr><td bgcolor=orange>不太常用</td></tr></table>

​		$\color{olive}{SHIFT+°'"（FACT）}$。e.g.输入10位及以内的整数，按下=，再按$\color{olive}{SHIFT+°'"（FACT）}$，则会输出分解结果。注意，计算器无法分解过大的整数（7位及以上），此类整数会用括号标注。

### 3. 模式简介

​		此处仅介绍常用模式及其功能，大部分功能都集成在OPTN选项下，可以在相应模式下按OPTN查看。菜单中可以切换模式。

#### 计算

<table><tr><td bgcolor=orange>最常用</td></tr></table>

默认模式，无特殊功能。

#### 复数

<table><tr><td bgcolor=orange>很常用</td></tr></table>

​		可计算辐角、共轭，提取实部、虚部，进行直角坐标与极坐标转换。在复数模式下，按下ENG会输入i，按下$\color{olive}{SHIFT+ENG（∠）}$会输入∠。

#### 矩阵

<table><tr><td bgcolor=orange>很常用</td></tr></table>

​		可定义、编辑最大4x4的矩阵，计算矩阵加法、乘法、行列式、转置，**不能求矩阵的秩和逆**。定义、编辑矩阵时，需要在相应位置输入各元素的值，输入完成之后按=结束对该元素值的编辑，所有元素编辑完成之后，可以直接按AC退出编辑、进入计算，也可以按OPTN选择继续定义、编辑其他矩阵，或者进入计算。

#### 向量

<table><tr><td bgcolor=orange>较常用</td></tr></table>

​		可定义、编辑最大三维向量，计算向量加法、乘法、内积、夹角。定义、编辑向量时，需要在相应位置输入各元素的值，输入完成之后按=结束对该元素值的编辑，所有元素编辑完成之后，可以直接按AC退出编辑、进入计算，也可以按OPTN选择继续定义、编辑其他向量，或者进入计算。

#### 方程

<table><tr><td bgcolor=orange>很常用</td></tr></table>

​		可求解四元及以下的一次线性方程组、四次及以下的一元线性方程。对于二次方程，还可以求解其最值大小和最值点。

#### 不等式

<table><tr><td bgcolor=orange>较常用</td></tr></table>

可求解四次及以下的一元不等式。

#### 统计

<table><tr><td bgcolor=orange>较常用</td></tr></table>

​		可计算期望、方差、标准差等统计数据，还可以用最小二乘法，根据指定形式函数进行拟合。

#### 基数

<table><tr><td bgcolor=orange>不常用</td></tr></table>

​		用于2、8、10、16进制之间的转换。

### 4.设置简介

​		$\color{olive}{SHIFT+菜单（设置）}$即可进入设置，设置一般默认即可，也可以按需调整。$\color{olive}{SHIFT+9（复位）}$可将所有设置数据重置为默认值。以下介绍顺序按照个人认为的重要性依次排列。

#### 角度单位

<table><tr><td bgcolor=orange>经常需要调整</td></tr></table>

​		可将输出默认角度单位设置为角度、弧度或者百分度，对应提示符分别为D、R、G，默认为角度D，一般只用前两个。

#### 复数

<table><tr><td bgcolor=orange>偶尔需要调整</td></tr></table>

​		可将输出复数结果的默认格式设置为a+bi或者ρ∠θ，对应提示符分别为i与∠，默认为a+bi。

#### 分数结果

<table><tr><td bgcolor=orange>一般无需调整</td></tr></table>

​		可将输出分数结果的默认格式设置为带分数或者假分数，默认为假分数。

#### 方程/函数

<table><tr><td bgcolor=orange>一般无需调整</td></tr></table>

​		可打开/关闭高次方程复数结果的输出，默认为开。

#### 输入/输出

<table><tr><td bgcolor=orange>一般无需调整</td></tr></table>

​		可设置输入/输出默认格式，默认为数学输入/数学输出，一般默认即可。

### 5.常用技巧

​		此处为本人一些小小的心得体会，欢迎补充。

#### 解单变量方程

​		$\color{red}{ALPHA+CALC（=）}$输入等号，等式两侧输入单变量表达式，$\color{olive}{SHIFT+CALC（SOLVE）}$输入变量迭代初值后求解距离初值最近的解。若解距离初值过远可能显示无解，求解过程可通过AC打断。可用于求解非线性方程、高次方程。

​		e.g.输入ln(x)，$\color{red}{ALPHA+CALC（=）}$输入等号，输入1，按下$\color{olive}{SHIFT+CALC（SOLVE）}$后输入0（即变量迭代初值），按下=即可求解，解得x=0.

#### 含参表达式求解

​		输入含参数的表达式，按下CALC后可依次输入各参数的值，最后得到计算结果。可使用此技巧快速求得单变量方程的数值解，在部分情况下（如自控理论B的频率特性校正计算）有奇效，具体操作如下：先自己化简等式，使等式一侧只含常量，另一侧为含参表达式，然后输入含参表达式，通过前述CALC功能求出参量取不同值时的结果，结果与常量足够接近时，参量的值即可视为近似解。若能熟练掌握该技巧，求近似数值解的速度可以比前述solve功能快。

​		e.g.若已知90-arctan（0.5x）+arctan（0.1x）-arctan（0.01x）-arctan（0.005x）=0，要求解x。则步骤如下：输入90-arctan（0.5x）+arctan（0.1x）-arctan（0.01x）-arctan（0.005x），按下CALC后输入0（即变量x的值），按下=后即可求得x=0时表达式的值。重复前述过程，可以求出参量取不同值时表达式的结果，当结果与0较为接近时，此时x的值即可作为近似解。

### 一些链接

如果想更全面地了解991的基础功能，可以参考卡西欧官方提供的[说明书](https://support.casio.com/cn/manual/manualresult.php?cid=004009101&keyword=)和一些[教程](https://www.casio.com.cn/support/calculators/content/download/shishengziliao/)。

如果想了解各路大神在991上整出来的花活，可以参考[fx-991cnx计算器:利用ROP漏洞执行任意代码 - 知乎](https://zhuanlan.zhihu.com/p/618704031)。
