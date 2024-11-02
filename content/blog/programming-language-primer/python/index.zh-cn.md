---
title: Python 语言特性杂谈
date: 2024-01-28
description: Python 这样的语言对比之前的 C 来说，非常的高级
authors:
  - name: 寅默
    link: https://github.com/YinMo19
    image: https://github.com/YinMo19.png
excludeSearch: false
math: true
---

Python 这样的语言对比之前的 C 来说，非常的高级。这样的高级很多时候直接体现在逻辑的不一样——我们不会像 C 语言那样直接考虑计算机的底层逻辑，甚至有`memcpy`这样直接对内存做拷贝的函数。很多时候例如在 C 语言中我们对变量做自增`obj++`，但是这样的写法在 Python 中是行不通的。因为 Python 不会去考虑这样的写法是否会更符合汇编语言，或者说计算机底层的直接的实现如何。又比如说，Python 中没有宏这样的概念，所以也不需要`do{} while(0)`语句来实现一些功能。若我们需要在循环之后才判断，我们在 Python 中并没有`do{} while()`这样的循环可以选择，然而我们可以在 while 中写一个 if 语句进行判断来作为循环后判断的代替。例如我们想要制作一个阶乘计算器，而这个计算器的终止条件是输入一个负数，我们在 C 语言中可以这样做。

```C
#include <stdio.h>

int main(void) {
    int input = 0, result = 1;
    do {
        scanf("%d", &input);
        result = 1;
        for (int i = 1; i <= input; i++) {
            result *= i;
        }
        printf("%d\n",result);
    } while (input >= 0);
    return 0;
}  
```

但如果是 python，我们则是

```python
while True :
    my_input = int(input("input n:"))
    result = 1
    if my_input < 0 :
        break
    for i in range (1,my_input+1):
        result *= i
    print("n!=",result)
```

这样的高级性很多时候让 Python 的使用更多的是依靠其丰富的库。很多时候你能用 Python 来做什么不是 Python 能做什么，而是有没有这个功能的库以及你对这方面知识了解多少。这样的使用体验很类似于在 C 语言中使用`qsort`来进行排序——我不需要知道具体是怎么实现排序这个功能的，我只需要提供排序的依据和需要排序的内容就可以了。

但是无论怎么说，Python 的学习依然和之前的 C 一样，还是需要多读代码，多写代码才能提高对语言的理解。学习路径大概便是这样，我们将第一章的部分题目用 Python 重新实现，通过 C 和 Python 的关联和对比，我们或许可以更好的学习 Python。至于 Django，由于具体是网站的后端，所以逻辑上不太相似，我们放在下一章。可以说我学习 Python 的目的是为了学习 Django，所以在本体的语言学习上会比较粗浅——但是我只需要能够在出现问题的时候能够知道在哪里获得答案，这就足够了，不是么？

## 配置每个项目需要的环境

如果我们编写大型项目可能就会出现某些问题，例如包冲突。解决包冲突的一种方法就是使用虚拟环境，在每一个 project 里面都配一次环境。输入

```
python -m venv venv
source ./venv/bin/activate
```

来激活虚拟环境，并选择 python 的解释器为 venv，即我们刚刚设置的虚拟环境，然后可以进行环境的配置，例如

```
pip install django 
pip install mysqlclient 
```

至于关闭虚拟环境只需要输入如下。

```
deactivate
```

## python 语言的特性

python 语言是动态的，其自由变量的名称解析发生于运行时而不是编译时。例如，

```python
i = 10
def f():
    print(i)
i = 42
f(12)
```

这和 C 语言中的

```C
#include <stdio.h>

int a = 10;
int func(void) { return a; }

int main(void) {
    extern int a;
    a = 20;
    printf("%d", func());
    return 0;
}
```

不是同一个意思，python 把值和标识符上面的，而我们如果调用其 id 就会发现两次的 i 就不是同一个东西了，但是函数调用的依然是后面的那个值，这说明：python 是动态的解析函数内的标识符，这是一件比较独特的事情。

## 类与面向对象编程

python 语言最重要的特性就是面向对象编程。例如之前学习的 C 语言，我们的表达式类似于 1+1，我们认为这是一种运算——但是在 python 中我们则是会认为这是一种方法，一种类下的方法。

加法对应着`__add__`方法，也就是说实际上

```python
1+1 #与下面的
a = 1
a.__add__(1)
```

是等价的。python 的语法糖是说，对于不需要新增语言特性而可以简化写法的一些特定语法。例如加法就是一个语法糖。那么什么是方法什么是类？

实际上是这样，我们可以新建一个类，类似于如下代码：

```python
class MyClass:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def SomeFuc(self):
        pass
```

这里我们进行一些简单的解释。首先我们定义了一个类，这个类的名字叫做`MyClass`，这个类下面可以定义一些方法，其中不可或缺的就是初始化方法。初始化方法固定写法就是前后加上两条下划线，而且第一个“传入”的元素是其本身。什么本身？就是这个类的实例本身。这里需要简单说明一下，我们如果不是直接对这个类进行操作，就需要将类实例化。也就是对特定某个对象进行操作，例如之前我们说的 1+1 中的前面一个 1 就是一个实例，我们对其使用了其名下（python 自带的）方法（也就是类中定义的函数）。需要注意的是初始化是我们创立实例的时候运行的。

其后我们需要注意的是（尤其是初学者很容易一头雾水的），我们初始化中的`self.a = a`实际上做的操作是，新建了一个实例名下的特性 a，并赋值为初始化的时候传入的那个值 a。所以我们在实例化的时候就要传入初始化需要的值。

```python
test = MyClass(3,5)
print(test.b)
#output:5
```

所以所谓的方法就是实例对应的类名下的函数。而且我们可以随意创建其名下的特性。

## 迭代器与 for 循环

首先定义`iterable,iterator`对象，即迭代器。迭代器是，凡是可以动态产生“下一个”对象的东西。

自己实现`range`如下

```python
class MyRange:
    def __init__(self,beg,end):
        self.beg = beg
        self.end = end 
    def __iter__(self):
        self.cur = self.beg 
        return self 
    def __next__(self):
        if self.cur == self.end:
            raise StopIteration
        r = self.cur 
        self.cur += 1
        return r
```

例如，在`for`第一次调用`range`的时候，我们会自动调用一次的`__iter__`，以后每一次在`for`中调用的是`__next__`。`for`循环的具体实现方式在下一节，而这里我们写一个偶数迭代器如下。

```python
class EvenIter:
    def __init__(self, n) -> None:
        self.cnt = 0
        self.num = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.cnt < self.num:
            tmp = self.cnt
            self.cnt += 2
            return tmp
        else:
            raise StopIteration


for i in EvenIter(7):
    print(f"Loop: {i}")
```

迭代器的一个好处是，不需要占用整个列表的内存，而是每次“加载”下一次的数据。

## 实现我们自己的`enumerate`

第一个方法是最不好理解的，但是相比第二种方法，他可以复用。首先注意第 15 行，我们在第一次返回`MyEnum`的时候调用了`self.iterable.__iter__`，这里实际上进行了两次操作，即初始化和返回值 (如果使用调试就会发现这里进入了两次)

```python
class MyEnumIterator:
    def __init__(self, iterator) -> None:
        self.cur = -1
        self.iterator = iterator
    
    def __next__(self):
        self.cur += 1
        return self.cur, self.iterator.__next__()

class MyEnum:
    def __init__(self, iterable):
        self.iterable = iterable
    
    def __iter__(self):
        return MyEnumIterator(self.iterable.__iter__())

if __name__ == '__main__':
    for i, e in MyEnum([1, 2, 3, 4]):
        print(i, e)
```

```python
class MyEnum2:
    def __init__(self, iterable):
        self.iterable = iterable
    
    def __iter__(self):
        self.cur = -1
        self.iterator = self.iterable.__iter__()
        return self

    def __next__(self):
        self.cur += 1
        assert self.iterator is not None
        return self.cur, self.iterator.__next__()
```

显然接下来的第三个是最好理解的，利用`yield`将两个参数传回。

```python
def MyEnum3(iterable):
    cur = 0
    for elm in iterable:
        yield cur, elm
        cur += 1
```

## `yield`的“世界暂停”

在`for`循环中，迭代器本身可以利用`yield`来做。我们可以实现迭代器如下：

```python
def MyRange2(beg,end):
    cur = beg
    while cur != end:
        yield cur 
        cur += 1
    return
```

`yield`是一个语法糖。他在使用的时候会返回他后面的东西，并且“短暂的”停止`def`定义内的函数内容，至例如，`for`循环去重新调用迭代器的`__next__`方法。比如我们首先重写一个`mymap`如下。

```python
class MyMap1:
    def __init__(self,f,it):
        self.f = f
        self.it = it
    def __iter__(self):
        self.elm = None
    def __next__(self):
        self.elm = self.f(self.it.__next__())
        return self.elm
```

需要注意的是这里的两个`__next__`不是同一个东西。我们自己定义的`__next__`是对于我们的`mymap`使用的，而在`__next__`里面的

```python
    self.elm = self.f(self.it.__next__())
```

本身是对于可迭代对象，例如列表，元组的`__next__`方法。

```python
def MyMap(f,it):
    for elm in it:
        yield f(elm)
```

这里可以认为，`yield`是上面写法（也就是用类写的`yield`对应部分）的相同表述。例如我们写一下的测试代码

```python
it = MyMap(lambda x: x+1, [1, 2, 3, 4, 5])
print("before loop")
try:
    while True:
        i = it.__next__()
        print(f"Loop: {i}")
except StopIteration:
    pass
```

会输出

```python
before loop
Do: 1
Loop: 2
Do: 2
Loop: 3
Do: 3
Loop: 4
Do: 4
Loop: 5
Do: 5
Loop: 6
```

也就是，这里的看似函数的写法实际上并不是函数，而是一个语法糖，所以我们实际上在第一行调用的时候并不会输出`Do :1`，而是先输出`before loop`。并且我们这里的`__next__`方法会被自动认为是这个我们改写的`MyMap`。

那么什么是“世界暂停"？这里的暂停实际上就是，我们遇到一个`yield`之后就会像`return`一样返回，一直到后面再遇到`__next__`方法，就会从上一次`yield`的地方继续往下运行，这又体现出迭代器省内存的优势。

另外，`for`循环的实现原理如下

```python
it = after_in.__iter__()
try:
    while True:
        i = it.__next__()
        pass
except StopIteration:
    pass
```

最后还有一个`yield-from`方法，实际上这依然是一个语法糖。例如下面的

```python
def flatten(it):
    for elm_it in it:
        for elm in elm_it:
            yield elm
```

可以将输入的列表套列表（元组套字典等）展平为一个列表（元组），而这可以等价于

```python
def flatten(it):
    for elm_it in it:
        yield from elm_it
```

另外我们需要注意的是，我们使用了`yield`实际上就不是一个函数，而是一个类，甚至是一个迭代器——他已经自动帮我们重写了里面的迭代器方法。所以我们可以例如这样

```python
it = list(flatten([[1,2,3],[2,3,4],[3,4,5]]))
print(it)#output:[1, 2, 3, 2, 3, 4, 3, 4, 5]
```

这是因为`list`接受的东西是一个迭代器。例如可以写`list(range(1,7))`。我们还可以写生成器表达式如下：

```python
[10*i + j for i in range(1,5) for j in range(1,5) if j%2 == 0 ]
```

## 关闭资源的省心方法

如果我们清理文件需要很多次的时候我们可以使用`with)语句。我们希望就是在某一块区域内如果我们需要离开，我们都必须在最后关掉某个资源——不管是用什么方法退出的情况，我们都需要释放资源。(这是一个语法糖。`

```python
with open("11.txt","w") as f:
    f.write("111")
```

具体到`with`语句中就是，在其后的缩进块中退出就会自动关闭其打开的资源。

## python 的模块与包

python 的一个包必须含有一个`__init__.py`的文件，而且是每一个文件夹中都需要有一个。例如我们可以在这个文件夹中的文件内定义的函数`import`到同文件夹中的`__init__.py`，然后用`__all__`，就可以对外直接调用这些函数。例如我们如下的目录路径

```
.
├── addtools
│   ├── aaa.py
│   ├── bbb.py
│   ├── __init__.py
│   └── __pycache__
│       ├── aaa.cpython-311.pyc
│       ├── bbb.cpython-311.pyc
│       └── __init__.cpython-311.pyc
└── main.py
```

我们在`addtools`的`__init__.py`中写入

```python
from .aaa import add1 
from .bbb import add2 

__all__ =  ["add1","add2"]
```

这样我们在`main.py`就可以直接写

```python
from addtools import add1,add2 


print(add1(1))
print(add2(1))
```

即相当于直接对外界暴露我们在一个包内的文件中自己定义的函数。

## 类型标注

类型标注的基本语法类似如下

```python
a:int = 11
b:bool = True
c:float = 1.1 if a else 1.3 
d:None = None
```

```python
list_int:list[int] = [1,1,1,1]
list_int:list[str] = [*'str']
tuple_a:tuple[int,int,int] = (1,1,1)
```

所谓`Callable`是值这个函数是可调用对象。

```python
def addone(x:int)->int:
    return x+1


addone_c:Callable[[int,int],int]
```

如果有默认值的参数，那么写法和最开始的写法是一样的。

```python
def addone(x:int，delta:int = 1)->int:
    return x+1
```

另外函数传入的参数列表中如果默认值是一个可变对象会出现：调用函数对默认值进行修改的风险。所以如果需要，那么需要这样写

```python
def bindecrease(xy:list[int],delta:list[int] | None = None):
    if delta is None:
        delta = [1,1]
    return [xy[0]+delta[0],xy[1],delta[1]]
```

其中这里对`__or__`方法进行了重载，这是一个语法糖。

```python
delta:list[int] | None = None
```

```python
@classmethod 
@staticmethod
```

分别用于不对外开放的方法和逻辑上隶属于这个类的方法。

```python
from typing import overload, assert_never


class test_overload():
    @overload
    def __init__(self, date: int) -> None:
        pass

    @overload
    def __init__(self, date: str) -> None:
        pass
    
    def __init__(self,date :int | str) -> None:
        match date:
            case int():
                pass
            case str():
                pass  
            case _ as unreachable:
                assert_never(unreachable)
```

重载方法用的语法糖（装饰器

## 斐波那契数列

在 C 语言中，我们利用在函数中调用相同函数的特性来计算斐波那契数列，而我们在 python 中自然也可以这么做——但是 Python 语言的特性可以大大简化这样的过程，我们只需要在主函数中使用类似于`a,b = b,a+b`的语句就可以进行同时的赋值。这样的语句会先进行右边部分的计算，然后再一一对应的赋值给左边。所以 python 语言的值交换是非常简单的。

```python
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b
```

这样就是直接利用递推式输出斐波那契数列的不超过 10 的前几项。

## 最大公约数

Python 语言非常简洁——而且非常规范。我们需要注意，例如顶级定义之间空两行，方法定义之间空一行的要求。Python 与 C 不同，Python 不太强调数值的类型，所以函数定义的时候并不是像 C 那样先指明函数的返回类型，甚至在 Python 中不写`return` 表示无返回值。另外 Python 也有自己的三元运算符，例如本次所写的

```python
def gcd(a, b):
    return gcd(b, a % b)if b else a


a, b = (input("Input numbers a and b:").split())
print(f"Gcd(a,b) = {gcd(int(a),int(b))}")
```

Python 的三元运算符判断的语句在中间而非两边，并且使用了`if else`来连接，这似乎非常的符合英语的语法，也体现了 Python 语言的高级性。

## 念整数

题目与上一章的一样，我们用 Python 实现如下

```python
long_int = input("please input a long int:")
int_list = ["ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu"]
for i in long_int:
    if i == "-":
        print("fu", end=" ")
        continue
    print(int_list[int(i)], end=" ")
```

这里的思路恐怕和 C 就不太一样，我们不真的把整数看成整数，而是看成字符串再分割成一个个字符做“强转”，并且我们利用了 python 的`for`循环的特性，可以对列表、元组内的元素遍历——那么字符串我们可以视为一种特殊的元组，还有什么比这更巧的事么？

## 矩阵的转置

在 python 实现转置我们可以使用列表推导式来处理。例如

```python
def transpose_list(list_of_lists):
    return [
        list(row)
        for row in zip(*list_of_lists)
    ]
    
print(transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
```

这里的实现方式非常有趣，以至于一开始还不太好理解。我们在函数中`return`的是一个列表推导式（换行了）。列条推导式的函数部分（也就是平常`for`循环的缩进部分）是产生一个列表，这是因为后面出现的那个，没有见过的东西——`zip`的需要。`zip()` 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

这就是`zip`和`map`的相同和不同之处了。后者接受一个函数，将其后传入的可迭代对象按顺序一一取出元素放入函数中，将结果作为新的列表的元素。而前者则是简单的将传入的可迭代对象按顺序一一取出之后列为一个个元组。需要注意的是，为了节省内存，python3 的特性是，需要手动在外面套一层例如，`list`才能就将其转换为元组的列表。另外如果在`zip(*obj)`实际上相当于解包。

就本题而言，传入的二维列表在`zip`内被转化为三个一维列表 (仅仅只看我们的例子)，而这三个一维列表被`zip`接受转化为三个对应的元组。现在我们的列表推导式从这个 zip 中接受的是一个个元组（因为此时可迭代对象变成了一个个元组），并转换为了一个个列表。

所以这实际上用于做矩阵的转置是有一点“作弊”了。这个内置函数的作用刚刚好就是用于做这件事的。另外我们考虑用`map`；来实现`zip`的效果。

```python
map(lambda *args:args,*list_of_lists)
```

实际上这里我们利用了匿名函数参数不定时返回元组的特性。

## 汉诺塔

利用递归将汉诺塔的方法简化为：

- 先将前 n-1 层挪到第二根柱子上
- 将第 n 层挪到第三根柱子上
- 将前 n-1 层挪到第三根柱子上
  将柱子抽象出来为某个元素，这样我们就可以完成递归——其中函数就是将从上往下数 n-1 层的挪动方法。

```python
def hanoi(n,x,y,z):
    if n == 1:
        print(f"{x} --> {z}")
    else:
        hanoi(n-1,x,z,y)
        print(f"{x} --> {z}")
        hanoi(n-1,y,x,z)

n = input("请输入汉诺塔的层数：")
hanoi(int(n),'X','Y','Z')
```

例如输出

```
请输入汉诺塔的层数：4
X --> Y
X --> Z
Y --> Z
X --> Y
Z --> X
Z --> Y
X --> Y
X --> Z
Y --> Z
Y --> X
Z --> X
Y --> Z
X --> Y
X --> Z
Y --> Z
```

我们人类有时候很难去想象一些方法，尤其是递归方法。例如这个问题，如果多层调用同一个函数我们就很难想象其进程。甚至于，如果真的直接处理四层汉诺塔，我们会觉得上面输出的方法很巧妙——然而实际上这个答案不过是由代码生成的，而且代码还很简单（甚至逻辑很简单）。

## 迷宫问题 (BFS 深度搜索算法)

我们用*来代表墙壁，而空格就是路径。另外我们的出发点和出口分别用字母 S(start) , T(terminal) 表示。例如迷宫

```
S*   ** 
 * * ** 
 * * ** 
   *  T
*******
```

找到最短路径并输出。其中提前输入行数。

```python
def find_start(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "S":
                return [i, j]
    return [-1, -1]


def find_next(lis, vlis, pos, step):
    global min
    if lis[pos[0]][pos[1]] == 'T' and step < min:
        min = step
    for nps in dirs:
        try:
            if pos[0]+nps[0] >= 0 and pos[1]+nps[1] >= 0:
                fps = pos[0]+nps[0], pos[1]+nps[1]
                if ((lis[fps[0]][fps[1]] == ' ' or lis[fps[0]][fps[1]] == 'T')
                        and vlis[fps[0]][fps[1]] == 0):
                    vlis[fps[0]][fps[1]] = 1
                    find_next(lis, vlis, fps, step+1)
                    vlis[fps[0]][fps[1]] = 0
        except IndexError:
            continue


row = input("请输入行数：")
vlis, lis = [], []
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
min = 114514

for i in range(int(row)):
    lis.append([])
    lis[i] = input()

vlis = [[0*i for i in range(len(lis[rows]))]
        for rows in range(len(lis))]

pos = find_start(lis)
vlis[pos[0]][pos[1]] = 1
find_next(lis, vlis, pos, 0)
print("最短路径为", min)
```

其中需要注意的是，python 对列表的索引值是可以是负的（也就是对应的反方向查找）！所以我们需要人为判断为正。至于列表越界，利用 python 自带的机制即可。这是很经典的 DFS 算法，实际上利用 C 和 Python 实现起来难度相近。

```
请输入行数:9
**   **   *
 * * ** * *
 *S* ** * *
   *    ***
******* *T*
*       * *
  ******* *
*         *
***********
最短路径为 31
```

另外修改过的代码如下

```python
# 全局的东西就放到最前边全局去，并且大写
GMIN = None
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 重命名，map 是 python builtin 的东西，最好不要重名
def find_start(maze):
            if cell == 'S':
                # 尽量使用不可变的元组类型做这种 "把几个值打包放一起的操作"
                return (i, j)

    # 如果需要一个和其他值意义都不一样的值，
    # 那就让它彻底表现得和正常情况不一样
    return None


# 重命名 lis -> maze, python 是动态类型语言，对同一个概念维持同一个命名很重要
# 重命名 vlis -> visited, 不要使用奇奇怪怪的缩写
def find_next(maze, visited, pos, step):
    # 直接使用解构赋值给予 pos 中的两个值一个有意义的名字
    row, col = pos

    # 重命名，min 是 python builtin
    global GMIN
    assert GMIN is not None
    if maze[row][col] == 'T' and step < GMIN:
        GMIN = step

    # 具有意义的一段代码可以抽出来写小函数，更加具有可读性
    def in_range(row, col):
        return 0 <= row < len(maze) and 0 <= col < len(maze[new_row])

    for next_row, next_col in DIRS:
        new_row, new_col = row + next_row, col + next_col
        # 偏好尽早退出而非嵌套
        if not in_range(new_row, new_col):
            # 没事不要用 try except IndexError 的样子来判断是否超范围，
            # 这很少见且没有直接体现你的意图
            continue

        # visited 里放的类型从 0/1 int 转成 bool, 因为你本质上就是拿它当 bool 在用
        # 使用 in 运算符可以替代多次重复写 maze[new_row][new_col]
        if maze[new_row][new_col] in (' ', 'T') and not visited[new_row][new_col]:
            visited[new_row][new_col] = True
            find_next(maze, visited, (new_row, new_col), step + 1)
            visited[new_row][new_col] = False


# 如果一个 python 脚本是期望直接运行的，那么最好像下边这样写
# 包在下边这个 if 内的代码只有在直接 python <文件> 的时候才会执行，
# 在它被 import 的时候则不会。可以认为这是约定俗成的 "main" 函数
if __name__ == '__main__':
    # 在输入处直接做数据处理 (转成 int), 而不是留到后边做
    row_cnt = int(input("请输入行数："))
    GMIN = row_cnt ** 2

    # 让第一次绑定尽量贴着变量的构建，它们逻辑上是一块的："构建出这个对象"
    # 尽可能使用表意的写法，直接描述对象应该是什么，而不是描述要如何构建这个对象
    maze = [input() for _ in range(row_cnt)]
    visited = [[False for _ in row] for row in maze]

    if (start_pos := find_start(maze)) is None:
        raise RuntimeError('Start pos not found')
    start_row, start_col = start_pos

    visited[start_row][start_col] = True
    find_next(maze, visited, start_pos, 0)

    print("最短路径为", GMIN)

    # 使用合理的空行，按逻辑分块你的程序，以及文件最后一个字符应该是回车
```

## 动态规划——寻找最佳子序列

输入一串用空格隔开的数字，找出其最大子序列的序列长度。动态规划的想法是，制造一个数组，这个数组的内容是{\bf 以数组下标对应本数组的数字为子序列最后一个元素的最优解的序列长度}，其递推关系为
$$
    \mathrm{dp}[j]
    =
    \begin{cases}
        1 &,\mathrm{list}[i]<\mathrm{list}[j] ,0\leq i <j\\[2ex]
        \max\{ \mathrm{dp}[i]\} +1&,\mathrm{list}[i]<list[j] ,0\leq i <j
    \end{cases}
$$

```python
def find_dp(list_A: list[int]) -> list[int]:#类型标注，类似于 C 的 int *list_A
    dp = [1 for _ in range(len(list_A))]#创建一个 dp 数组
    for j in range(len(list_A)):
        for i in range(j):
            if list_A[i] < list_A[j]:
                dp[j] = max(dp[i] + 1, dp[j])#算法本身，利用 python 写要直接表达意思
    return dp


if __name__ == '__main__':
    list_A = list(map(int, input().split()))
    dp = find_dp(list_A)
    print(max(dp))

```
