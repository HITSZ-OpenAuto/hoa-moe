---
title: C 语言刷题笔记
date: 2024-01-27
description: 对于一个初学者，留着本来的代码参考是一件很有意思的事情。我留下了第一次遇到这个题目的想法，这也体现了我对某个题目的想法的一步步进步
authors:
  - name: 寅默
    link: https://github.com/YinMo19
    image: https://github.com/YinMo19.png
excludeSearch: false
math: true
---

本文实际上是用 LaTeX 进行写作，写完之后受 OpenAuto 开发者的邀请用 Markdown 进行重写。然而重写是不可能重写的，只能用 python 自己写一个转换程序这样子。写程序总会（或者说很容易）出现 bug，虽然转换之后已再三检验，但错误在所难免。如若发现错误，欢迎和开发者（或笔者）进行沟通（QQ：2672690715）。

由于本书是个人学习笔记，所以会随着笔者的学习不断的更新，有机会可以将更多内容投放至此。写的并不是很好，具体说明详见第二版前言、第一版前言。祝编程愉快。

笔者在初学编程语言的时候犯下了许多错误，其中很大的一项是随意猜测代码本意。虽然很快的之后就发现了这样的错误，但是依然给我敲响了警钟。学习编程很重要的是能够理解代码背后的含义，算法思维也是很重要的。如果看到第二章的内容比第一章要简洁很多，虽然可能是因为 Python 语言本身就简洁，但是更多的时候是学完 C 语言之后的想法更好了，自然也写的更好了。如果让我重写第一章的内容，我或许会写的少很多——但是我没有这么做。

对于一个初学者，留着本来的代码参考是一件很有意思的事情。我留下了第一次遇到这个题目的想法，这也体现了我对某个题目的想法的一步步进步。例如念整数那个题目，我最开始考虑利用`switch-case`语句来对应一种种情况，后来才知道，利用数组可以很便捷的实现这样的功能，但最开始我利用数字去判断这样的思路难道就有什么问题么？再进一步思考，我最开始就把输入的这个数字真的当成数字有必要么？作为一个个字符，处理起来是否会更轻松呢？如果有这样的想法的一步步进步，那么这些笔记就才值得一看了。否则列一个提纲，直接去 CSDN 上面搜索，我相信每道题都会有答案的。

<p align="right">寅默<br>2023 年秋</p>

# C 语言例题与分析

## 九九乘法表

输出九九乘法表，只需要写两个简单的循环。注意由于间距不定，我们采用输出制表符$\backslash{\rm t}$保证相同间距。

```C
#include <stdio.h>

int main(void) {
    int i, j;
    for (i = 1; i <= 9; i++) {
        for (j = 1; j <= i; j++) {
            printf("%d*%d=%d\t", i, j, i * j);
            if (i == j) {
                printf("\n");
            }
        }
    }
    return 0;
}
```

这样就可以输出如下

```
1*1=1
2*1=2   2*2=4
3*1=3   3*2=6   3*3=9
4*1=4   4*2=8   4*3=12  4*4=16
5*1=5   5*2=10  5*3=15  5*4=20  5*5=25
6*1=6   6*2=12  6*3=18  6*4=24  6*5=30  6*6=36
7*1=7   7*2=14  7*3=21  7*4=28  7*5=35  7*6=42  7*7=49
8*1=8   8*2=16  8*3=24  8*4=32  8*5=40  8*6=48  8*7=56  8*8=64
9*1=9   9*2=18  9*3=27  9*4=36  9*5=45  9*6=54  9*7=63  9*8=72  9*9=81
```

不采用制表符，我们可以采取指定输出整数的位数来实现 (注意我们采用的方法是向右补空格，所以是$\%$-nd，其中 n 代表你想要输出的宽度)：

```C
    printf("%d*%d=%-4d",i,j,i*j);
```

另外一种乘法表是写右上角的乘法表，这样的实现也是简单的补制表符即可。我们就不加演示。

## 最大公因数的实现

    采用辗转相除法，并将其内置为函数。本次写法为前导式。

```C
#include <stdio.h>

int gcd(int a,
        int b); //前导式函数引语，指明最大公因数函数的函数的输入输出格式。

int main(void) {
    int a = 0, b = 0;
    scanf("%d %d", &a, &b);
    printf("%d\n", gcd(a, b));
    return 0;
}

int gcd(int a, int b) {
    int d = 1, cnt = 1;
    if (a <= b) {
        d = a, a = b, b = d;
    } //判断两数大小，保持大的在前。
    for (cnt = 1; b > 0; cnt++) {
        d = b, b = a % b, a = d;
    }
    return a;
}
```

这里有一个易错点：在 for 循环语句中我们的判断条件是可以继续执行的条件而不是结束条件，所以 gcd 函数中的 for 条件应该是$b>0$，而不是等于 0.

这样的代码在实现需要的功能已经是没有问题了，那么如果我们还需要多次输入以及美化这个函数，我们可以进行如下修改。

```C
#include <stdio.h>

int gcd(int a, int b);

int main(void) {
    int  a = 0, b = 0, n = 0, judge = 1;
    char K = '1';
    for (n = 0; judge; n++) {
        printf("输入两个需要得出最大公因数的正整数（两个数中间用空格隔开）：");
        scanf("%d %d", &a, &b);
        printf("%d\n", gcd(a, b));
        printf("请问您还需要判断下一组数据吗？回答Y或者N：");
        scanf(" %c", &K);
        judge = K == 'Y' ? 1 : 0;
    }
    return 0;
}

int gcd(int a, int b) {
    int d = 1, cnt = 1;
    if (a <= b) {
        d = a, a = b, b = d;
    }
    for (cnt = 1; b > 0; cnt++) {
        d = b, b = a % b, a = d;
    }
    return a;
}
```

请注意这里的易错点：我们输入两个数后按了回车，这个回车键是会被 scanf 扫描进 char 的，因为 char 规定回车键也是字符的一种。所以我们在 scanf 中提前插入空格来保证这个回车不会产生影响。

上述程序中我们利用了 for 循环的特性来写这样一个判断语句。如果用户输入 Y，我们认定 judge 的值为 1，即条件为真，因此输入 Y 意味着我们可以进行下一轮测试。此外我们还可以利用 if，并且直接省略 for 中的判断语句（但是分号不能丢），采用 continue 和 break 来判断。

```C
for (n = 0;; n++) { //直接将其替换上面的代码对应行即可。
    printf("输入两个需要得出最小公因数的正整数（两个数中间用空格隔开）：");
    scanf("%d %d", &a, &b);
    printf("%d\n", gcd(a, b));
    printf("请问您还需要判断下一组数据吗？回答Y或者N：");
    scanf(" %c", &K);
    if (K == 'Y')
        continue;
    else
        break;
}
```

break 和 continue 起到了 for 语句第二条的作用，实质上这样写便和 while 语句没有区别了。最后我们甚至可以不使用循环语句，仅仅利用 goto。因此我们省去了几个不需要的变量。

```C
int main(void) {
    int  a = 0, b = 0, c = 0;
    char K = '1';
A:
    printf("输入两个需要得出最小公因数的正整数（两个数中间用空格隔开）：");
    scanf("%d %d", &a, &b);
    printf("%d\n", gcd(a, b));
    printf("请问您还需要判断下一组数据吗？回答Y或者N：");
    scanf(" %c", &K);
    if (K == 'Y')
        goto A;
    else
        goto B;
B:
    return 0;
}
```

下一步我们考虑对 gcd 函数的进一步简化。我们有没有必要先判断 ab 的大小进行交换呢？不如这样考虑，如果 ab 不进行交换会发生什么？a 获得了 b 的值，b 获得了 a$\%$b的值。注意，由于 b 比 a 大，所以实际上 a$\%$b还是 a！这样我们就做了一次交换。所以代码中对 ab 的大小判断实际上是可以删掉的。

```C
int gcd(int a, int b) {
    int d = 1, cnt;
    for (cnt = 1; b > 0; cnt++) {
        d = b, b = a % b, a = d;
    }
    return a;
}
```

我们在函数中写了一个自降的循环，这是可以的。但是我们实际上在函数的调用中天然就可以写出循环，也就是函数自循环。例如我们在函数的返回值中继续调用 gcd，那么它便又返回 gcd 函数中了。所以我们利用三目运算符和函数自降简化如下：

```C
 int gcd(int a, int b) {
  return b ? gcd(b, a % b): a; /*b是0吗？不是的话(请注意只写一个b表示布尔运算，即非0为真，0为假)就返回gcd(b,a%b)，是就返回a(程序结束)*/
 }
```

另外我们换一种自循环的递降算法也一样可以大大简洁代码

```C
#include<stdio.h>

int gcd(int a,int b){
 return a>b?gcd(a-b,b):a<b?gcd(a,b-a):a;/*若a>b则返回gcd(a-b,b),若a<b则返回gcd(a,b-a),若都不然(即两数相等)返回a,程序结束*/}

int main(){
 int a=0,b=0;
 scanf("%d %d",&a,&b);
 printf("%d",gcd(a,b));
 return 0;
 }
```

最后给出效率最低的方式：穷举法。我们从较小的数开始向下穷举，直到发现第一个可以被两数同时整除的数字。

```C
#include<stdio.h>

int gcd(int a,int b){
 int c;
 for(c= a>b?b:a;a%c!=0||b%c!=0;c--);
 return c;
}

int main(void) {
 int a,b;
 scanf("%d %d",&a,&b);
 printf("%d",gcd(a,b));
 return 0;
}
```

## 素数和

**问题：**我们认为 2 是第一个素数，3 是第二个素数，5 是第三个素数，依次类推。
现在，给定两个整数 n 和 m，$0<n\leq m<200$，你的程序要计算第 n 个素数到第 m 个素数之间所有的素数的和，包括第 n 个素数和第 m 个素数。

```C
#include <stdio.h>

int main(void) {
    int n = 0, m = 0, cnt = 0, zs = 0, i = 0, judge = 0, sum = 0;
    scanf("%d %d", &n, &m);
    for (i = 2; cnt <= m - 1; i++) {
        zs = 1;
        for (judge = 2; judge < i; judge++) {
            if (i % judge == 0) { //判断是否是素数
                zs = 0;
            }
        }
        cnt = zs ? cnt + 1 : cnt; //是素数则计数器自增
        sum+=(zs && (cnt >= n))*i; //若是素数且在所需要的区间内算入总和
    }
    printf("%d", sum);
    return 0;
}
```

分为几个步骤：判断是否是素数，是素数则计数器自增，若是素数且在所需要的区间内算入总和。其中判断素数可以写为一个函数，虽然在本题中的意义并不大。

```C
int zspd(int i) {
    int judge = 1, zs = 1;
    for (judge = 2; judge < i; judge++) {
        if (i % judge == 0) {
            zs = 0;
        }
    }
    return zs;
}
```

    此时原代码只需要去掉main中不需要的变量，并将原本判断素数的循环改为zs=zspd(i);即可。

## 念整数

**问题：**你的程序要读入一个整数，范围是[-100000,100000]。然后，用汉语拼音将这个整数的每一位输出出来。如输入 1234，则输出：yi er san si。注意，每个字的拼音之间有一个空格，但是最后的字后面没有空格。当遇到负数时，在输出的开头加上“fu”，如 -2341 输出为：fu er san si yi。

```C
#include <math.h>
#include <stdio.h>

int main(void) {
    int m = 0, i = 0, judge = 0, cnt = 0, t = 0, bite = 0, j = 0;
    scanf("%d", &m);
    if (m < 0) { //判断有没有没负号，若有则加上fu，并修正为正。
        m = -m;
        printf("fu");
    }
    t = m;
    for (cnt = 1; m > 0; cnt++) { //判断这个整数的位数
        if (m / 10 != 0)
            m = m / 10;
        else
            break;
    }
    for (j = 0; t > 0; j++) { //逐个输出每一位数对应的拼音
        bite = t / (pow(10, cnt - 1 - j));
        switch (bite) {
        case 1:
            printf(" yi");
            break;
        case 2:
            printf(" er");
            break;
        case 3:
            printf(" san");
            break;
        case 4:
            printf(" si");
            break;
        case 5:
            printf(" wu");
            break;
        case 6:
            printf(" liu");
            break;
        case 7:
            printf(" qi");
            break;
        case 8:
            printf(" ba");
            break;
        case 9:
            printf(" jiu");
            break;
        case 0:
            printf(" ling");
            break;
        }
        t = t - bite * pow(10, cnt - 1 - j);
    }
    return 0;
}
```

这是一段偏蠢的代码，但是它是很好理解的。我们可以对几处重复的写法进行修正。第一处是一出 for 循环。

```C
for (cnt = 1; m > 0; cnt++) { //判断这个整数的位数
    if (m / 10 != 0)
        m = m / 10;
    else
        break;
}
```

for 循环本身具有判断条件，所以我们根本不需要再利用 if 和 else 来判断是否跳出。不过需要注意的是直接修改可能会出现计数器的错误，因为 for 循环在第二次以上的检验会先对第三条语句进行运算，但是本例中 if 语句是先判断后运算，恰巧一样，故仅修改如下。

```C
for (cnt = 1; m / 10 != 0; cnt++) { //判断这个整数的位数
    m = m / 10;
}
```

到这似乎是一个正确的结果了？但是我们注意到一个小问题。如果我们输入一个正数，那么就会在最开始出现一个多余的空格。仔细思考我们确实是这样的。

修改的蠢办法依然是有的，例如我们将第一位的输出单独再改一次。但是这样做显然过于麻烦，而且代码长度便大大增长了，虽然各位都是 CV 程序员（雾）...注意到 for 循环中自带了一个计数器，我们只需要当第一位的时候不输出空格即可。所以我们修改第三段代码如下：

```C
for (j = 0; t > 0; j++) {
    if (j != 0) {
        printf(" ");
    }
    bite = t / (pow(10, cnt - 1 - j));
    switch (bite) {
    case 1:
        printf("yi");
        break;
    case 2:
        printf("er");
        break;
    case 3:
        printf("san");
        break;
    case 4:
        printf("si");
        break;
    case 5:
        printf("wu");
        break;
    case 6:
        printf("liu");
        break;
    case 7:
        printf("qi");
        break;
    case 8:
        printf("ba");
        break;
    case 9:
        printf("jiu");
        break;
    case 0:
        printf("ling");
        break;
    }
    t = t - bite * pow(10, cnt - 1 - j);
}
```

如果我们输入 1234，确实得到了正确结果，但是若是 -1234 我们便会发现 fuyi 之间没有空格。所以我们还需要再对前面第一部分进行修正：

```C
if(m<0){
     m=-m;
     printf("fu ");
}
```

这里有个问题，那么多的 switch-case 能不能用什么方法简化一下呢？可以的，我们将字符串直接存在数组里面就可以了。

```C
char *zs[10] = {"ling", "yi",  "er", "san", "si",
                "wu",   "liu", "qi", "ba",  "jiu"}; //导言区

for (j = 0; t > 0; j++) { //输出整数每一位的部分
    if (j != 0) {
        printf(" ");
    }
    bite = t / (pow(10, cnt - 1 - j));
    printf("%s", zs[bite]);
    t = t - bite * pow(10, cnt - 1 - j);
}
```

这样就从 switch 跳到特定的某一行变成直接从数组里调取某个元素。显然后者实现简单多了。更改结束后的全代码如下。

```C
#include <math.h>
#include <stdio.h>

int main(void) {
    long  m = 0, i = 0, judge = 0, cnt = 0, t = 0, bite = 0, j = 0;
    char *zs[10] = {"ling", "yi",  "er", "san", "si",
                    "wu",   "liu", "qi", "ba",  "jiu"};
    scanf("%ld", &m);
    if (m < 0) {
        m = -m;
        printf("fu ");
    }
    t = m;
    for (cnt = 1; m / 10 != 0; cnt++) { //判断这个整数的位数
        m = m / 10;
    }
    for (j = 0; t > 0; j++) {
        if (j != 0) {
            printf(" ");
        }
        bite = t / (pow(10, cnt - 1 - j));
        printf("%s", zs[bite]);
        t = t - bite * pow(10, cnt - 1 - j);
    }
    return 0;
}
```

在测试的时候又发现了个问题，如果数字太大就直接程序就错误了！那么又怎么办呢？如果我们的输入直接存到一个数组里面，不但解决了数字过大的问题，连最开始的位判断都能省去了。

```C
#include<stdio.h>

int main()
{
 int i=0,shuru[50]={0};//初始化输入的数据
 char m=0,*zs[10]={"ling","yi","er","san","si","wu","liu","qi","ba","jiu"} ;
 while(i<50){//检测每次输入是否是回车，是即停止，否则继续存入下一个数字
  shuru[i]=getchar();
  if(shuru[i]=='\n'){
   break;
  }
  i++;
 }
 for(int k=0;k<50&&shuru[k]!=10;k++){/*如果遇到回车(ASCII码是10)和输入超出50个任一即退出*/
  if(k==0&&shuru[0]==45){
   printf("fu ");
   continue;//判断首位是否是负号(ASCII码是45)
  }
  printf("%s ",zs[shuru[k]-48]);//否则按位输出
 }

 return 0;
}
```

我们测试程序如下：

```
-1726268272817272823826917391753
fu yi qi er liu er liu ba er qi er ba yi qi er qi er ba er san ba er liu jiu yi qi san jiu yi qi wu san
```

我们发现在每次输出后自然而然的加上了空格。其实这件事并不是很重要，如果我们真的不想让最后一位多输出一个空格，我们就只需要把是否输出空格变成一个条件判断即可。

## 玩猜数字游戏 (7.11)

人与电脑一起报数，从 1 开始，只能报一个或者两个，谁报 30 谁赢。其中由于存在后手必胜策略，电脑的出方式为剩下个数余 3 为 2 则报两个，余 1 报一个，整除则随便报一个或者两个。我们先来看看一个简单的例子。如果我报数 1，电脑则是 2，3，我报 4，5，电脑则报 6.这样显然电脑最后会报 30。若电脑先手，则随便一个或者两个。一旦我出现了纰漏（指报不到三的倍数），接下来则电脑由前面的策略必胜。我们来考虑这样一个代码。首先是随机出一个先手。

```C
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main() {
 srand(time(NULL));
 char *a[2]= {"电脑","您"};//定义一个字符数组
 int role=rand()&1,cnt=0;/*role是一个随机的数字0或者1，&表示按位与，对1按位于即舍弃二进制前面所有的内容，保留最后一位。*/
 printf("本次游戏的先手为：%s\n",a[role]);
 return 0;
}
```

接下来考虑游戏过程。我们考虑对角色 role 的值在每一次游戏过后都变化一次。但是我们还需要在函数中返回游戏进行到哪一步。除了使用指针来改变 role 的值以外，我们可以在循环中每执行一次用按位或来使 role 在 01 之间变换。所以我们写了一个游戏进行的循环。

```C
int (*play_func[2])(int) = { play_computer, play_human };

int main() {
 srand(time(NULL));
 char *a[2]= {"电脑","您"};
 int role=rand()&1,cnt=0;
 printf("本次游戏的先手为：%s\n",a[role]);
 for(role; 1; role^=1) {//每次通过按位或来对role实行01变换
  if((cnt=play_func[role](cnt))==30) {//每次对cnt赋值后调用特定函数
   printf("%s胜出。",a[role]);//结束时通过最后的角色来判断谁胜出
   break;
  }
 }
 return 0;
}
```

这里我们使用了函数指针。也就是我们设置了一个函数的数组，使用起来和数组相似。在这里这个数组的元素是一个个函数，我们在调用数组就是一个判断并使用特定函数的过程。这里我们在巧妙运用 if 的特性。每次程序进入 for 循环之后执行 if 判断，即使我们 if 的条件为假，没有进入 if 内的语句，我们依然会执行 if 条件的语句。这样我们在 if 中写入的语句会一次次被执行。我们这个程序依靠计数器 cnt 来完成，所以我们函数的输入和输出都是 cnt。

```C
int play_computer(int cnt) {
 int r=rand()%2;//通过取余来实现01随机数选取
 if((30-cnt)%3==2) printf("电脑:%d,%d\n",cnt+1,cnt+2);
 else if((30-cnt)%3==1) printf("电脑:%d\n",cnt+1);//基础判断
 else if((30-cnt)%3==0&&r) printf("电脑:%d,%d\n",cnt+1,cnt+2);
 else printf("电脑:%d\n",cnt+1);//如果刚好cnt已经是3的倍数，随机加1或2
 return (30-cnt)%3==2?cnt+2:(30-cnt)%3==1?cnt+1:cnt+1+r;/*根据上面的输出来返回cnt的值。两次三目运算符分别判断是不是模3余2，模3余1，(剩下情况)整除*/
}

int play_human(int cnt) {
 int human_input;
 printf("请您输入：");
 do {
  scanf("%d",&human_input);
  cnt++;
 } while(getchar()!='\n');/*例如我们输入3 2(回车),那么首先读入一个数字，while执行判断：空格不是回车，继续读入数字，然后输入2和回车，那么结束循环，离开。在这个过程中我们输入了多少个数字，那么计数器就增加了多少。*/
 return cnt;
}
```

这样就实现了整个过程。完整代码如下。

```C
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int play_computer(int cnt) {
 int r=rand()&1;
 if((30-cnt)%3==2) printf("电脑:%d,%d\n",cnt+1,cnt+2);
 else if((30-cnt)%3==1) printf("电脑:%d\n",cnt+1);
 else if((30-cnt)%3==0&&r) printf("电脑:%d,%d\n",cnt+1,cnt+2);
 else printf("电脑:%d\n",cnt+1);
 return (30-cnt)%3==2?cnt+2:(30-cnt)%3==1?cnt+1:cnt+1+r;
}

int play_human(int cnt) {
 int human_input;
 printf("请您输入：");
 do {
  scanf("%d",&human_input);
  cnt++;
 } while(getchar()!='\n');
 return cnt;
}

int (*play_func[2])(int) = { play_computer, play_human };

int main() {
 srand(time(NULL));
 char *a[2]= {"电脑","您"};
 int role=rand()&1,cnt=0;
 printf("本次游戏的先手为：%s\n",a[role]);
 for(role; 1; role^=1) {
  if((cnt=play_func[role](cnt))==30) {
   printf("%s胜出。",a[role]);
   break;
  }
 }
 return 0;
}
```

运行结果如下。由于 while 执行判断的方式是判断是否是回车，所以我们输入的时候可以用任何方式输出两个数字（如果你需要的话）的间隔。

```
本次游戏的先手为：电脑
电脑:1,2
请您输入：3
电脑:4
请您输入：5 6
电脑:7
请您输入：8,9
电脑:10
请您输入：11 12
电脑:13,14
请您输入：15
电脑:16
请您输入：17 18
电脑:19
请您输入：20.21
电脑:22,23
请您输入：24
电脑:25,26
请您输入：27
电脑:28,29
请您输入：30
您胜出。
```

## 利用数组求长阶乘 (8.17)

本题需求是求 1 到 40 的阶乘。由于没有任何类型支持超长整数输出，我们需要利用数组来完成这样一个任务。

本代码的关键是如何实现数组储存长整型。我们考虑两个数相乘（一个很长的数和一个两位数相乘）的时候，我们直接将这个长整型的每一位都和这个两位数相乘，这样我们便可以得到一个每一位都确定的数。例如（请注意这里的第一行和第三行的数字是反序的，也就是前面的是低位，后面的是高位）

```C
  1  3  7  6  5  8
*  34
== 34 102 238 204 170 272
```

接下来我们才考虑进位，例如个位上的 34 我们就保留 4，把 3 进位到十位。而十位加上 3 之后得到的 105，我们将 1 进位到千位，百位进位了 0.经过从低到高的进位之后我们就得到了一个数字序列，这个数字序列的反序就是我们的结果。我们将这些数字储存在数组之中，这样便完成了乘法。具体实现即

```C
void jc(int a[100],int c);//导言区

void jc(int a[100],int c)
{
 for(int m=0;m<=99;m++){
   a[m]=0;
  }
  a[0]=1;
 for(int k=1;k<=c;k++){//阶乘的每一次乘法
  for(int i=0;i<100;i++){//乘法本身
   a[i]=k*a[i];
  }//每一位乘上对应的数字
  for(int j=0;j<98;j++){
   a[j+2]+=a[j]/100;
   a[j+1]+=(a[j]%100-a[j]%10)/10;
   a[j]=a[j]%10;
  }//进位的实现
 }
}
```

这里需要注意的是由于我们写成函数，也就是每次都需要用同一个数组进行运算，所以在循环之前需要初始化。在数组乘法实现之后，我们需要将其输出。我们专门写了一个函数实现它的输出。我们注意到由于 00000234000 实际上等价于 234000，也就是在**遇到第一个非 0 数字之前的任何 0 都是无效的**,所以我们先利用一个循环判断跳出的时机，并在跳出后反序输出每一位数字。为了工整美观，这个函数最后还需要输出一个换行。

```C
void print(int a[100]);//导言区

void print(int a[100])
{
 int k=0;
 for(k=99;k>=0;k--){//从最高位开始反序判断
  if(a[k]!=0){
   break;//如果遇到了第一个非零数即跳出，此时的k就是数组中所储存的数字的最高位
  }
  else;
 }
 for(int u=k;u>=0;u--){//反序输出每一位数字
  printf("%d",a[u]);
 }
 printf("\n");
}
```

下面是完整代码。

```C
#include <stdio.h>

void jc(int a[100], int c);
void print(int a[100]);

int main(void) {
    int a[100] = {1}, c = 1;
    for (c = 1; c <= 40; c++) { // 40并不是一个magic
                                // number，这是题干要求的内容。
        jc(a, c);           //调用了没有返回值的函数jc（阶乘）
        printf("%2d!=", c); // 2d表示占格两个，用于对齐
        print(a);           //输出数组a对应的数值
    }
    return 0;
}

void jc(int a[100], int c) {
    for (int m = 0; m <= 99; m++) {
        a[m] = 0;
    }
    a[0] = 1;
    for (int k = 1; k <= c; k++) {      //阶乘的每一次乘法
        for (int i = 0; i < 100; i++) { //乘法本身
            a[i] = k * a[i];
        } //每一位乘上对应的数字
        for (int j = 0; j < 98; j++) {
            a[j + 2] += a[j] / 100;
            a[j + 1] += (a[j] % 100 - a[j] % 10) / 10;
            a[j] = a[j] % 10;
        } //进位的实现
    }
}

void print(int a[100]) {
    int k = 0;
    for (k = 99; k >= 0; k--) { //从最高位开始反序判断
        if (a[k] != 0) {
            break;
            //如果遇到了第一个非零数即跳出，此时的k就是数组中所储存的数字的最高位
        } else
            ;
    }
    for (int u = k; u >= 0; u--) { //反序输出每一位数字
        printf("%d", a[u]);
    }
    printf("\n");
}
```

运行结果如下

```C
 1!=1
 2!=2
 3!=6
 4!=24
 5!=120
 6!=720
 7!=5040
 8!=40320
 9!=362880
10!=3628800
11!=39916800
12!=479001600
13!=6227020800
14!=87178291200
15!=1307674368000
16!=20922789888000
17!=355687428096000
18!=6402373705728000
19!=121645100408832000
20!=2432902008176640000
21!=51090942171709440000
22!=1124000727777607680000
23!=25852016738884976640000
24!=620448401733239439360000
25!=15511210043330985984000000
26!=403291461126605635584000000
27!=10888869450418352160768000000
28!=304888344611713860501504000000
29!=8841761993739701954543616000000
30!=265252859812191058636308480000000
31!=8222838654177922817725562880000000
32!=263130836933693530167218012160000000
33!=8683317618811886495518194401280000000
34!=295232799039604140847618609643520000000
35!=10333147966386144929666651337523200000000
36!=371993326789901217467999448150835200000000
37!=13763753091226345046315979581580902400000000
38!=523022617466601111760007224100074291200000000
39!=20397882081197443358640281739902897356800000000
40!=815915283247897734345611269596115894272000000000
```

接下来我们考虑对代码的改进。第一处是进位。我们考虑直接将每一个位的百位进到那个位前面两个位，这其实是没有必要的。例如我们将 132 的 1 向前进 2 位。3 向前进 1 位，实质上只需要将 13 进位到前一位即可。因为我们实质上的操作是只保留了最后一位 2，那么每一次这样操作之后也只会留下个位数，所以并没有关系。所以改进进位算法如下。

```C
for(int j=0;j<90;j++){
  a[j+1]+=a[j]/10;
  a[j]=a[j]%10;
 }//进位的实现
```

另外输出的时候我们采用循环判断的方式需要两个循环语句，我们也可以使用 if 判断语句来实现。怎样使用 if 语句来实现只要出现第一非零数字就开始持续不断的输出呢？我们注意到只要让某个计数器改变即可，所以改进如下。

```C
void print(int a[100])
 {
  int k=0,judge=0;
  for(k=99;k>=0;k--){//从最高位开始反序判断
   if(a[k]!=0){
    judge=1;
   }
   else;/*如果还没遇到非0数字，那么if语句不会执行，后面的输出也不会执行；一旦遇到非0数字，那么接下来即使遇到0，judge也不会改变，依然会输出*/
   if(judge){
    printf("%d",a[k]);
   }
  }
  printf("\n");
 }
```

增加效率的方式是使用压位。我们在上面数组每一位实际上最后只储存了一个不大于 9 的数，这对于一个数组实际上是很浪费的。作为 int 型的数组，我们能在每一位存的数实际上可以远大于 9(实际上 int 储存的最大值是 2147483647，因此我们一般压位的时候储存 4 位（保证效率的时候乘低精度的时候也不容易在最高位溢出）。)。所以如果我们考虑数组中的一个单元储存 2 位，甚至 3 位 4 位，我们就能实现所谓的**压位高精**。例如，我们本来将数字如下储存

```C
  1 2 3 4 5 6 7 8 9 8 7
a[x]1 2 3 4 5 6 7 8 9 8 7
b[x]0123 4567  8987
```

从本来需要存储数组的 11 个元素变为 3 个，这是一个较大的简化。压位的运算和之前完全一样，进位规则也几乎没有区别，只不过我们需要在输出时进行一次判断两次不同的输出。首先判断第一次出现的非 0 数组元素，输出这个元素，剩下的反序输出的同时需要**将首位 0 也输出**。这看起来有点奇怪，但是你一定不会想让

```
 0000 0000 0100 0100 1234
```

的数组输出是

```
        100   100 1234
```

吧？所以我们在判断输出的时候除了第一个直接输出，其余需要

```C
 printf("%.4d",a[u]);
```

来保证即使不足 4 位，也将前导 0 补齐。

## 冒泡法排序 (8.16)

利用冒泡法做数组内数字的大小排序。

我们先设置一个数组，并写两个函数来控制这个数组的输入和输出。

```C
#include<stdio.h>

void print(int *score) {
 while(*score!=-1) printf("%d ",*score++);/*当score不是-1的时候，我们让指针向后移位的同时输出这个指针对应的数组的量*/
}

void read(int *score) {
 do scanf("%d",score);//读入数组元素
 while(*score++!=-1);//判断指针score对应元素的是否是-1的同时指针向后移位
}

int main(void) {
 int score[40]= {0,};//40是题目指定的数组最大长度，其中我们以不被算入的-1作为结束
 read(score);
 print(score);
 return 0;
}
```

接下来考虑冒泡法排序。冒泡法的原理是通过每次比较前后两个数字的大小来实现整个排序过程。所以我们循环的结束条件应该是检验数组内的数字是否已经排列整齐。如果我们每次循环都做这样的检验，未免显得过于麻烦。所以我们换种方式考虑：设置一个计数器，每次进行交换的时候让计数器 +1(当然每次循环都需要初始化为 0)，若循环到最后一次的时候已经不再需要做交换，那么计数器就是 0，也即说明我们的交换已经做完了，可以离开循环了。

```C
void mpf(int *score) {//以指针形式传入数组
 int all=-1,temp=0;
 while(score[++all]!=-1) ;//all自增同时检验是否all是否到达-1的位置
 for(int cnt=1; cnt>0;) {/*判断结束的条件是该次循环已经没有再对数组做修改，即操作次数(cnt)为0*/
  cnt=0;//cnt最为每次循环的计数器，循环每次初始化为0
  for(int test=0; test<all-1; test++) {//test最大只能到all-2
   if(score[test]>score[test+1]) {
    temp=score[test];
    score[test]=score[test+1];
    score[test+1]=temp;
    cnt++;
   }//在需要的时候进行交换，并且记录操作次数
  }
 }
}

//...read(score);//main函数内
mpf(score);
//print(score);...
```

这样程序就完成了。完整代码：

```C
#include<stdio.h>

void mpf(int *score) {
 int all=-1,temp=0;
 while(score[++all]!=-1) ;
 for(int cnt=1; cnt>0;) {
  cnt=0;
  for(int test=0; test<all-1; test++) {
   if(score[test]>score[test+1]) {
    temp=score[test];
    score[test]=score[test+1];
    score[test+1]=temp;
    cnt++;
   }
  }
 }
}

void print(int *score) {
 while(*score!=-1) printf("%d ",*score++);
}

void read(int *score) {
 do scanf("%d",score);
 while(*score++!=-1);
}

int main(void) {
 int score[40]= {0,};
 read(score);
 mpf(score);
 print(score);
 return 0;
}
```

测试：

```C
1 3 2 4 5 9 7 6 26 13 29 333 22 52 42 88 -1//输入
1 2 3 4 5 6 7 9 13 22 26 29 42 52 88 333//输出
```

## 插入数据 (8.15)

题目要求为在一个已经顺序排列的数组中插入一个数据。输入输出的基本架构和上题完全一样。只需要更换一个函数。

```C
void insert(int *score,int x) {
 int all=-1;
 while(score[++all]!=-1) ;//记录所输入的数组长度
 for(int test=0; test<=all; test++) {
  if(x<score[test]||test==all) {//判断x位置
   for(int i=all;i>=test;i--) score[i+1]=score[i];//从高位向左赋值
   score[test]=x;//插入数字
   break;//结束循环
  }
 }
}

//main函数内插入
int x;
scanf("%d",&x);
insert(score,x);
```

完整代码如下

```C
#include<stdio.h>

void insert(int *score,int x) {
 int all=-1;
 while(score[++all]!=-1) ;
 for(int test=0; test<=all; test++) {
  if(x<score[test]||test==all) {
   for(int i=all;i>=test;i--) score[i+1]=score[i];
   score[test]=x;
   break;
  }
 }
}

void print(int *score) {
 while(*score!=-1) printf("%d ",*score++);
}

void read(int *score) {
 do scanf("%d",score);
 while(*score++!=-1);
}

int main(void) {
 int x;
 int score[40]= {0,};
 read(score);
 scanf("%d",&x);
 insert(score,x);
 print(score);
 return 0;
}
```

测试如下：

```C
1 4 6 7 9 10 15 22 55 77 247 -1//数组的输入
34//x的输入
1 4 6 7 9 10 15 22 34 55 77 247//输出
```

## 斐波那契数列

简单实现斐波那契数列是很简单的。

```C
#include<stdio.h>

long fbnq(long init){
 return init==1?1:init==2?1:fbnq(init-1)+fbnq(init-2);//初始两个1，接下来是一个递推
}

int main(void){
 for(long i=1;i<=45;i++) printf("fbnq(%d)=%d\n",i,fbnq(i));
 return 0;
}
```

但是我们运行就会发现时常非常长，该代码效率极低。为什么？我们做递归的时候，例如我们计算 fbnq(40)，我们把前 39 个斐波那契数全又算了一遍。这是一件非常不合理的事情。在计算第 45 个就已经很吃力了，所以我们仅仅欣赏代码的简洁性。不妨来计算一下这个代码的时间复杂度。

我们将调用一次函数作为所谓的一次运算。例如我们输入 fbnq(n)，那么下一步运算就是需要计算 fbnq(n-1)+fbnq(n-2)。注意！这里我们的 fbnq(n-1) 依然是一个独立的整体，是需要重新计算的。我们认定计算次数为${\rm Cnt}(n)$，那么就得到递推关系

$$
{\rm Cnt}(n)={\rm Cnt}(n-1)+{\rm Cnt}(n-2)
$$

我们还知道 n 为 1 或者 2 的时候我们只需要调用一次函数，所以实际上计算次数和斐波那契数的结果是一样的！如果不进行直接数学运算的话，可以看看待会输出的结果，让计算机进行这么多运算来得到结果显然是愚蠢的做法。如果我们知道斐波那契数列的通项公式的话，那么运算的时间复杂度就是$O\left(\exp\left(n\right)\right)$。我们刚才说运算到 45 已经很吃力了，我们根据 fbnq(45)=1134903170，在运算这个结果的时候我们反复调用了这个函数 11 3490 3170 次！

我们利用数组改进如下。

```C
#include<stdio.h>
#define len 700
#define ws 200

int main(void) {
 int a[len][ws]= {{1,},{1,}};//初始化两个1

 for(int cnt=2; cnt<len; cnt++) {
  for(int init=0; init<ws; init++) {
   a[cnt][init]=a[cnt-1][init]+a[cnt-2][init];//对每一位递推
  }
  for(int jw=0; jw<ws-1; jw++) {
   a[cnt][jw+1]+=a[cnt][jw]/10;
   a[cnt][jw]%=10;
  }//实现进位
 }

 for(int cnt=0; cnt<len; cnt++) {
  printf("fbnq(%d)=",cnt+1);//输出
  for(int init=ws-1,codeblock=0;init>=0;init--) {
   if(a[cnt][init]!=0||codeblock==1){//遇到第一个非0数开始持续输出至首位
    printf("%d",a[cnt][init]);
    codeblock=1;
   }
  }
  printf("\n");
 }
 return 0;
}
```

这样我们实现了高精度运算。并且利用数组储存我们每一个结果，这样我们进行递推的时候就只需要调用之前的运算结果，这样就极大的简化了我们的运算。我们选取部分输出如下：

```C
fbnq(290)=1806885656323799249738933639586633513160792578781310139745345
fbnq(291)=2923602405716568564338475449381171413803636207598822186175234
fbnq(292)=4730488062040367814077409088967804926964428786380132325920579
fbnq(293)=7654090467756936378415884538348976340768064993978954512095813
fbnq(294)=12384578529797304192493293627316781267732493780359086838016392
fbnq(295)=20038668997554240570909178165665757608500558774338041350112205
fbnq(296)=32423247527351544763402471792982538876233052554697128188128597
fbnq(297)=52461916524905785334311649958648296484733611329035169538240802
fbnq(298)=84885164052257330097714121751630835360966663883732297726369399
fbnq(299)=137347080577163115432025771710279131845700275212767467264610201
fbnq(300)=222232244629420445529739893461909967206666939096499764990979600
\\290~300之间的结果
fbnq(700)=87470814955752846203978413017571327342367240967697381074230432592527501911
     290377655628227150878427331693193369109193672330777527943718169105124275
```

书接上文，让电脑执行这个数量的运行次数显然不合理。那么利用数组进行运算，由于我们已经将数字存下来了，(在这里我们对位执行操作不计算入运行次数，因为我们如果使用 int 之类的类型来计算，计算机内部也会执行位运算) 所以每计算一个斐波那契数都只需要运行一次。该程序运行起来已经非常迅速。至于再次优化，那么又是压位高精，或者更高级的有关数论的优化算法。例如高精乘法可以从$O(n^2)$利用 FFT 优化到$O(n \log n)$，这又是很大的进步。(对数增长的速度远远低于幂函数，我们有以下结论：对于$\forall \alpha>0$,

$$
 \lim_{x\rightarrow+\infty}\frac{\log x}{x^\alpha}=0
$$

}

## 利用黎曼和求积分 (9.6)

简单来说即利用梯形法求函数和数轴围成的面积。根据定积分的定义有

$$
 \int_a^b f(x){\rm d}x=\lim_{N\rightarrow\infty}\frac{b-a}{N}\sum_{k=1}^{N}f\left(\xi_k\right),\xi_k\in\left(\frac{b-a}{N}(k-1),\frac{b-a}{N}k\right)
$$

,由于$\xi_k$的选取是任意的，我们直接选取单边，于是积分公式即

$$
 \int_a^b f(x){\rm d}x=\lim_{N\rightarrow\infty}\frac{b-a}{N}\sum_{k=1}^{N}f\left(\frac{b-a}{N}k\right)
$$

根据上述公式实现代码如下。

```C
#include <stdio.h>
#define N 100000//细分多少份

float Integrate(float(*f)(float),float a,float b) {
 float c=0;
 for (int i=1; i<=N; i++) c+=f(i*(b-a)/N);//求和部分
 return c*(b-a)/N;
}

float function1(float x) {//题目要求的两个待积分函数
 return 1+x*x;
}

float function2(float x) {
 return x/(1+x*x);
}

float (*f[2])(float)= {function1,function2};//函数指针的数组

int main(void) {
 printf("%f,%f",Integrate(f[0],0.0,1.0),Integrate(f[1],0.0,3.0));
 return 0;
}
```

输出为

```
1.333351,1.151306
```

我们可以直接计算两个积分为

$$
 \int_0^1 1+x^2 {\rm d}x=\frac{4}{3},\int_0^3\frac{x}{1+x^2}{\rm d}x=\frac{1}{2}\ln 10
$$

可见结果精度还是比较高的。

## 方针转置 (11.4)

```C
#include <stdio.h>

void Swap(int *a, int *b) {//按位异或的方式来进行交换
 *a=*a^*b;
 *b=*a^*b;
 *a=*a^*b;
}

#define N 10

void transpose_1(int a[][N], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            Swap(&(a[i][j]), &(a[j][i]));
        }
    }
}

void transpose_2(int (*a)[N], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            Swap(&(a[i][j]), &(a[j][i]));
        }
    }
}

void transpose_3(int *a, int n) {//输入时是指针*a,也就是a[0],即a[0][0]的地址
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            Swap(a + N*i + j, a + N*j + i);/* a在这里实际上是a[0][0]的地址，即我们直                      接对地址进行操作*/
        }
    }
}

void input(int a[][N], int n) {//输入
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &(a[i][j]));
        }
    }
}

void output(int a[][N], int n) {//输出
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%3d", a[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int a[10][10], n;

    scanf("%d", &n);
    input(a, n);

    transpose_1(a, n);
    output(a, n);

    transpose_2(a, n);
    output(a, n);

    transpose_3(*a, n);
    output(a, n);

    return 0;
}
```

## 非对称矩阵转置 (11.5)

实现矩阵转置。下面的代码使用了一维数组当作二维数组进行动态内存分配。

```C
#include<stdio.h>
#include<stdlib.h>//使用calloc和free函数需要调用

void Transpose(int *a,int *at,int m,int n) {//该转置即将a的内容写入at
 for(int cnt=0; cnt<m; cnt++) {
  for(int cntt=0; cntt<n; cntt++) {
   at[cntt*m+cnt]=a[cnt*n+cntt];
  }
 }
}

void read(int *a,int m,int n) {//读入a
 for(int cnt=0; cnt<m; cnt++) {
  for(int cntt=0; cntt<n; cntt++) {
   scanf("%d",&a[cnt*n+cntt]);
  }
 }
}

void print(int *at,int m,int n) {//打印at
 for(int cntt=0; cntt<n; cntt++) {
  for(int cnt=0; cnt<m; cnt++) {
   printf("%d ",at[cntt*m+cnt]);
  }
  printf("\n");
 }
}

int main(void) {
 int m,n,*a=NULL,*at=NULL;
 scanf("%d %d",&m,&n);
 a=calloc(m*n,sizeof(int));
 at=calloc(n*m,sizeof(int));//动态内存分配
 read(a,m,n);
 Transpose(a,at,m,n);
 print(at,m,n);
 free(a);
 free(at);//释放内存
 return 0;
}
```

输出如下 (Example)

```C
3 5//矩阵大小
2 3 4 5 6
6 5 4 3 2
3 3 7 8 1//初始矩阵
2 6 3
3 5 3
4 4 7
5 3 8
6 2 1//转置后的矩阵
```

若仿造上一题的做法，那么代码可以是

```C
#include <stdio.h>

void Swap(int *a, int *b) {
    int const t = *a;
    *a = *b;
    *b = t;
}

#define N 10
#define M 10

void transpose_1(int a[][N], int at[][M], int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            at[j][i] = a[i][j];
        }
    }
}

void transpose_2(int (*a)[N], int (*at)[M], int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            at[j][i] = a[i][j];
        }
    }
}

void transpose_3(int *a, int *at, int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            *(at + j*M + i) = *(a + i*N + j);/*与上一题不同的是这题直接对赋值，所以我们考虑指针*/
        }
    }
}

void input(int a[][N], int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &(a[i][j]));
        }
    }
}

void output(int a[][M], int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("%3d", a[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

int main() {
    int a[M][N], at[M][N], m, n;

    scanf("%d %d", &m, &n);
    input(a, m, n);

    transpose_1(a, at, m, n);
    output(at, n, m);

    transpose_2(a, at, m, n);
    output(at, n, m);

    transpose_3(*a, *at, m, n);
    output(at, n, m);

    return 0;
}
```

## 单词改错

根据莱温斯坦距离，我们首先设计单词距离函数。这个函数需要传入两个单词，也就是两个 char 类型的指针，并返回两者的莱温斯坦距离，也就是一个整数。根据题目意思，设计如下。

```C
int levenshteinDistance(char *word1, char *word2) {
 int len1 = strlen(word1);
 int len2 = strlen(word2);//得到两个单词的长度

 int matrix[len1 + 1][len2 + 1];

 for (int i = 0; i <= len1; i++)
  matrix[i][0] = i;
 for (int j = 0; j <= len2; j++)
  matrix[0][j] = j;

 for (int i = 1; i <= len1; i++) {
  for (int j = 1; j <= len2; j++) {
   int cost = (word1[i - 1] != word2[j - 1]);//cost是0和1来判断
   matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + cost);
  }
 }

 return matrix[len1][len2];
}
```

而在这个函数中我们又需要一个最小值函数，利用三元运算符简单设计如下

```C
int min(int a, int b, int c) {
 return a<=b&&a<=c?a:b<=c?b:c;
}
```

现在可以来设计主函数。首先我们需要调用三个头文件，并定义两个常数

```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define WORD_LENGTH 16
#define WORD_COUNT 8
#define LINE_LENGTH 5000
```

接下来在主函数中，我们先读入 (输出) 文件，并定义为指针，并作一定的错误分析。

```C
int main() {
 FILE *inputFile = fopen("words.txt", "r");
 FILE *wordListFile = fopen("vocabulary.txt", "r");
 FILE *outputFile = fopen("output.txt", "w");

 if (inputFile == NULL || wordListFile == NULL || outputFile == NULL) {
  printf("Failed to open file.\n");
  exit(1);
 }
```

接下来读入单词表

```C
// Read vocabulary
 char wordList[LINE_LENGTH][WORD_LENGTH]= {0,};
 int wordCount = -1;
 while (fgets(wordList[++wordCount], WORD_COUNT*WORD_LENGTH+10, wordListFile) != NULL)
  wordList[wordCount][strlen(wordList[wordCount])-1]='\0';
```

这里需要注意，由于 fgets 函数会读入回车，所以我们要将这一行单词的最后一个非零元素改成 0。其中修改的是最后一个元素，所以我们使用 strlen 函数来得出最后一个字符的位置。
接下来从我们要修改的单词文档中读入单词，然后再修改。我们来考虑读入单词的形式。由于每一行单词的格式是**四位数字 单词 单词/单词/.../单词**所以我们需要给读入的一行断成几个部分来处理。考虑 strtok 函数。

```C
    char line[WORD_LENGTH*WORD_COUNT+10];
 while (fgets(line, WORD_LENGTH*WORD_COUNT+10, inputFile) != NULL) {
  int ordinal=(line[0]-48)*1000+(line[1]-48)*100+(line[2]-48)*10+(line[3]-48),first=1,a=0;
  fprintf(outputFile, "%04d ", ordinal);

  char *wordPtr = strtok(line+5, " ");

  while (wordPtr != NULL) {
   int bestDistance = WORD_LENGTH,cnt=0;
   char bestWord[WORD_LENGTH];
            if (wordPtr[strlen(wordPtr)-1]=='\n') wordPtr[strlen(wordPtr)-1]='\0';

   for (int i = 0; i <wordCount; i++) {
    int distance = levenshteinDistance(wordPtr, wordList[i]);
    if (distance < bestDistance) {
     bestDistance = distance;
     strcpy(bestWord, wordList[i]);
    }
   }

   fprintf(outputFile, "%s", bestWord);
   if (first==1) {
    wordPtr = strtok(NULL, " ");
    fprintf(outputFile, " ");
    wordPtr = strtok(wordPtr, "/");
   } else wordPtr = strtok(NULL, "/");
   if(wordPtr != NULL&&first==0) fprintf(outputFile, "/");
   first=0;
  }
  fprintf(outputFile, "\n");
 }
```

我们给出的 wordPtr 指针首先是从读入的一行的第五个元素开始向后段至遇到的第一个空格，而前面的四个数字以补零的方式以一个数值输出。往后通过定义的 first=1，通过 if 判断是否是循环的第一次，然后再考虑接下来的指针的位置。再 while 循环中的 for 循环通过比较每一个单词和词汇表中的莱温斯坦距离来推断哪一个但是是最贴近的单词，利用 strcpy 写入 bestWord 中。最后还需要在每一行的后面输出一个回车。

还需要注意，由于 fgets 得到的每一行最后有一个回车，所以需要通过 strlen 得到单词长度把回车换成 0。最后我们还需要 fclose 几个文件。

```C
    fclose(inputFile);
 fclose(wordListFile);
 fclose(outputFile);

 printf("Correction complete. Result saved to output.txt.\n");

 return 0;
```

于是整个程序就完成了。这个程序需要运行约 30 秒，效率不算高。所有代码如下。

```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define WORD_LENGTH 16
#define WORD_COUNT 8
#define LINE_LENGTH 5000

int min(int a, int b, int c) {
 return a<=b&&a<=c?a:b<=c?b:c;
}

int levenshteinDistance(char *word1, char *word2) {
 int len1 = strlen(word1);
 int len2 = strlen(word2);
 int matrix[len1 + 1][len2 + 1];

 for (int i = 0; i <= len1; i++)
  matrix[i][0] = i;
 for (int j = 0; j <= len2; j++)
  matrix[0][j] = j;

 for (int i = 1; i <= len1; i++) {
  for (int j = 1; j <= len2; j++) {
   int cost = (word1[i - 1] != word2[j - 1]);
   matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + cost);
  }
 }

 return matrix[len1][len2];
}

int main() {
 FILE *inputFile = fopen("words.txt", "r");
 FILE *wordListFile = fopen("vocabulary.txt", "r");
 FILE *outputFile = fopen("output.txt", "w");

 if (inputFile == NULL || wordListFile == NULL || outputFile == NULL) {
  printf("Failed to open file.\n");
  exit(1);
 }

 // Read vocabulary
 char wordList[LINE_LENGTH][WORD_LENGTH]= {0,};
 int wordCount = -1;
 while (fgets(wordList[++wordCount], WORD_COUNT*WORD_LENGTH+10, wordListFile) != NULL)
  wordList[wordCount][strlen(wordList[wordCount])-1]='\0';

 char line[WORD_LENGTH*WORD_COUNT+10];
 while (fgets(line, WORD_LENGTH*WORD_COUNT+10, inputFile) != NULL) {
  int ordinal=(line[0]-48)*1000+(line[1]-48)*100+(line[2]-48)*10+(line[3]-48),first=1,a=0;
  fprintf(outputFile, "%04d ", ordinal);

  char *wordPtr = strtok(line+5, " ");

  while (wordPtr != NULL) {
   int bestDistance = WORD_LENGTH,cnt=0;
   char bestWord[WORD_LENGTH];
            if (wordPtr[strlen(wordPtr)-1]=='\n') wordPtr[strlen(wordPtr)-1]='\0';

   for (int i = 0; i <wordCount; i++) {
    int distance = levenshteinDistance(wordPtr, wordList[i]);
    if (distance < bestDistance) {
     bestDistance = distance;
     strcpy(bestWord, wordList[i]);
    }
   }

   fprintf(outputFile, "%s", bestWord);
   if (first==1) {
    wordPtr = strtok(NULL, " ");
    fprintf(outputFile, " ");
    wordPtr = strtok(wordPtr, "/");
   } else wordPtr = strtok(NULL, "/");
   if(wordPtr != NULL&&first==0) fprintf(outputFile, "/");
   first=0;
  }
  fprintf(outputFile, "\n");
 }

 fclose(inputFile);
 fclose(wordListFile);
 fclose(outputFile);

 printf("Correction complete. Result saved to output.txt.\n");

 return 0;
}
```

词汇表这里不再显示，改之前的 words.txt 大致如下（前几个

```
0004 I go/am/went/work
0005 am I/the/only
0007 your friend/happiess/shoes
0008 name after/class/number
0010 my computer/parents/he/her
0012 bye bye/see/wave/say
0013 Miss Mrs/Mr/yours/polite
0016 you are/he/she/I
0017 are you/they/we
1338 is he/she/it
0020 good afternoon/job/well/fine/nice
0021 afternoon good/evening/noon/morning
0023 morning good/afternoon/noon/midnight
0025 night good/midnight/morning/noon
0027 this is/that/like
1340 that this/these/is/like
0028 Mr Miss/polite/gentle/custom
0030 to you/me/her/he
0031 nice good/better/well/people
0032 meet with/see/watch/walk
```

改之后的如下（同样是前几个

```
0004 I go/am/went/work
0005 am I/the/only
0007 your friend/happiness/shoes
0008 name after/class/number
0010 my computer/parents/he/her
0012 bye bye/see/wave/say
0013 Miss Mrs/Mr/yours/polite
0016 you are/he/she/I
0017 are you/they/we
1338 is he/she/it
0020 good afternoon/job/well/fine/nice
0021 afternoon good/evening/noon/morning
0023 morning good/afternoon/noon/midnight
0025 night good/midnight/morning/noon
0027 this is/that/like
1340 that this/these/is/like
0028 Mr Miss/polite/gentle/custom
0030 to you/me/her/he
0031 nice good/better/well/people
0032 meet with/see/watch/walk
```

注意到第三行的 happiess 已经改成了 happiness，所以程序大概发挥了应有的作用。

## 记账系统 v1.0

```C
// Amount System v1.0
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME_LENGTH 11
#define get_infn(prompt, input, cont)                                          \
    do {                                                                       \
        do {                                                                   \
            printf(prompt);                                                    \
        } while (scanf("%d", &input) == 1 && !(cont));                         \
    } while (0)
#define _print_list_text(_Ptr, i)                                              \
    do {                                                                       \
        printf("%05d   %-16s%-11d%-12d\n", _Ptr[i].id, _Ptr[i].name,           \
               _Ptr[i].income, _Ptr[i].outcome);                               \
    } while (0)

typedef struct Amount {
    int  id;
    char name[MAX_NAME_LENGTH];
    int  income;
    int  outcome;
} amount;

amount *amounts = NULL;
int     num;

int _void_strcmp(const void *s1, const void *s2) {
    return strcmp((char *) (((amount *) s2)->name),
                  (char *) (((amount *) s1)->name));
}

void Input_record(void);
void Sort_and_list(void);
void Search_records(void);
void Calculate(void);
void List_more(void);
void List_all_records(void);
void Exit(void);

// Some little function
void _list_beginning(void) {
    printf("ID UserName Income    Expenses\n"
           "-----   --------        ------     --------\n");
}

void _list_ending(void) {
    printf("-----   --------        ------     --------\n");
}

void _list_records(amount *amount_ptr) {
    _list_beginning();
    for (int i = 0; i < num; i++) {
        _print_list_text(amount_ptr, i);
    }
    _list_ending();
}

void (*function[7])() = {
    Exit,      Input_record, Sort_and_list,   Search_records,
    Calculate, List_more,    List_all_records};

int main(void) {
    int            input = 0;
    extern amount *amounts;
    do {
        do {
            printf("1.Input record\n"
                   "2.Sort and list records in reverse order by user name\n"
                   "3.Search records by user name\n"
                   "4.Calculate and list per capita income and expenses\n"
                   "5.List records which have more expenses than per capita "
                   "expenses\n"
                   "6.List all records\n"
                   "0.Exit\n"
                   "  Please enter your choice:");
        } while ((scanf("%d", &input) == 1) && (input >= 7 || input < 0));
        getchar();
        function[input](amounts, num);
    } while (1);

    return 0;
}

void Input_record() {
    if (amounts) {
        free(amounts);
    }
    printf("Input the number of recorders:");
    scanf("%d", &num);
    amounts = (amount *) calloc(num, sizeof(amount));
    for (int i = 0; i < num; i++) {
        get_infn("Input your ID (length less than 5):", amounts[i].id,
                 0 <= amounts[i].id && amounts[i].id < 100000);
        getchar();
        printf("Input your name :");
        fgets(amounts[i].name, 10, stdin);
        amounts[i].name[strlen(amounts[i].name) - 1] = 0;
        get_infn("Input your income :", amounts[i].income, 1);
        get_infn("Input your outcome :", amounts[i].outcome, 1);
    }
}
void Sort_and_list() {
    if (amounts) {
        amount *ptr = (amount *) calloc(num, sizeof(amount));
        for (int i = 0; i < num; i++) {
            ptr[i] = amounts[i];
        }
        qsort(ptr, num, sizeof(amount), _void_strcmp);
        _list_records((amount *) ptr);
        free(ptr);
    } else
        printf("Please input the datas firse.(choose 1).\n");
}
void Search_records() {
    if (amounts) {
        char _input_for_search[MAX_NAME_LENGTH];
        int  i = 0;
        printf("Please input the user name:");
        fgets(_input_for_search, 10, stdin);
        _input_for_search[strlen(_input_for_search) - 1] = 0;
        for (i = 0; i < num; i++) {
            if (!strcmp(_input_for_search, amounts[i].name)) {
                break;
            }
        }
        if (i < num) {
            _list_beginning();
            _print_list_text(amounts, i);
            _list_ending();
        } else
            printf("404 NOT FOUND\n");
    } else
        printf("Please input the datas firse.(choose 1).\n");
}

void Calculate() {
    if (amounts) {
        float _per_capita_income = 0, _per_capita_expenses = 0;
        for (int i = 0; i < num; i++) {
            _per_capita_income += amounts[i].income;
            _per_capita_expenses += amounts[i].outcome;
        }
        printf("Per capita income: %.2f\n", _per_capita_income / num);
        printf("Per capita expenses: %.2f\n", _per_capita_expenses / num);
    } else
        printf("Please input the datas firse.(choose 1).\n");
}

void List_more() {
    if (amounts) {
        float _per_capita_expenses = 0;
        for (int i = 0; i < num; i++) {
            _per_capita_expenses += amounts[i].outcome;
        }
        _per_capita_expenses /= num;
        _list_beginning();
        for (int i = 0; i < num; i++) {
            if (amounts[i].outcome > _per_capita_expenses) {
                _print_list_text(amounts, i);
            }
        }
        _list_ending();
    } else
        printf("Please input the datas firse.(choose 1).\n");
}

void List_all_records() {
    if (amounts) {
        _list_records(amounts);
    } else
        printf("Please input the datas firse.(choose 1).\n");
}

void Exit() {
    free(amounts);
    exit(0);
}

```

我一直认为类函数宏的用法是非常好的。其中一个很重要的原因就是，我们经常可以传入一些很神奇的参数。例如我们有一个结构体表示一个物品的颜色，里面有 RGB 三个量。显然很有可能我们对三个量的操作是类似的，甚至可能就只需要换一下对结构体的调用就可以了——但是你能够对函数传入参数 R 么？只有利用类函数宏才能随意的传入参数，因为类函数宏的调用和内联函数相似，是直接替换掉代码，这是一种很有用的方法。
