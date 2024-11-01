---
title: 磁力计数据读取--以IST8310为例
date: 2022-12-03
authors:
  - name: Minghang Li
    link: https://github.com/lmh12138
    image: https://github.com/lmh12138.png
description: 这里以博世传感器公司产出的BMI088型号的IMU为例
excludeSearch: false
math: true
---

> 这里以iSentek公司产出的IST8310型号的磁力计为例，尺寸为 3.0 *3.0* 1.0mm，支持快速 I2C 通信，可达 400kHz，14 位磁场数据，测量范围可达1600uT(x,y-axis)和 2500uT(z-axis)， 最高 200Hz 输出频率
>
> IST8310的数据手册附在文件夹里面，可以自行阅读
>
> 同时这里的磁力计是安装在大疆公司出产的RoboMaster开发板C型，单片机芯片是STM32F407IGH6，其外围电路已经设计好，只需要读取磁力计数据即可。
>
> 本篇不会介绍SPI、I2C等嵌入式通信协议，需要有一定嵌入式开发基础的同学来看（可以去看底层中介绍的STM32开发视频）
>
> 文末附代码

## 零、数据手册分析

第一章讲了IST8310的特性，I2C通信，最高支持400kHz通信速率，14位或者16位自适应数据输出等特性

![image-20221203143646334](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_45_56_7b57dc46de2c0df92e3c6e2834090e6b.png)

第二章讲了内部结构

![image-20221203143810184](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_46_1_19fe50fb8bb2acf9c1e67205fa3b4b89.png)

第三章讲了电气特性

![image-20221203143859175](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_46_7_be434063ae03763a916c0b36f15cf21d.png)

第四章讲了如何联系他们

![image-20221203144121246](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_46_17_379d843b68088eb96070aa0be858a1e2.png)

然后数据手册就没了。。。在大疆的开发手册中找到了寄存器的手册，如下：

![image-20221203165413897](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_46_22_130ba1b817405924e9ca747bd18209bc.png)

![image-20221203165444657](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_46_37_c6c7b64d4474532cb8c0afcb499547d3.png)

![image-20221203165507558](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_46_47_101024a952ae686e76fdb3f7937ce9f4.png)

![image-20221203165822701](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_47_11_c829375c8e5f9a68cc477c13364e48e8.png)

![image-20221203165838781](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_47_22_cb339b7f55f945768a63e19be3cd41ae.png)

![image-20221203165849045](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_47_36_a512864f9a89d5c414c277a5fb3f4361.png)

## 一、CubeMX配置

点开I2C配置选项， 下图是配好的：

![image-20221203165955297](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_47_43_7f875afb73fef98a090324fdff56d29f.png)

观察IST8310的数据手册，发现其支持最大400kHz的I2C通信速率，也就是快速I2C模式，所以第一行I2C Speed Mode我们选Fast Mode

![image-20221203170120553](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_47_51_6f5500cbb2b3d40ab923e41aa41cc77d.png)

同时不要忘记了在C板中I2C3的两个IO口分别是PA8和PC9（一般来说都是这两个）

![image-20221203170657996](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_47_58_419c6a92d707ad6d6520b67d0a9058b5.png)

之后观察大疆和IST8310的数据手册，发现控制IST8310重启的是PG6的GPIO口，低电平为重启，所以我们将其设置为高电平上拉输出模式

![image-20221203170402663](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_48_4_0ab146aa0575b26ce86a33907e7e10ab.png)

![image-20221203170428263](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_48_10_c66eedc2e832c13207a918b0171db1a2.png)

![image-20221203170517446](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_48_15_fa555c8a89213c55ea626d87074e9bca.png)

![image-20221203170602068](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_48_19_4617ef0cf0b026a785287c1d8f916dd7.png)

因为我们读取IST8310的程序运行在1kHz的freertos线程中，无需使用中断方式，所以我们不配置中断口

## 二、数据读取

总代码附在文末，这里放一些核心函数

IST8310初始化：

```C
void IST8310_INIT(ist8310_data_t* ist8310_data) {
    memset(ist8310_data, 0, sizeof(ist8310_data_t));

    ist8310_data->meg_error = IST8310_NO_ERROR;

    // 把磁力计重启
    HAL_GPIO_WritePin(IST8310_GPIOx, IST8310_GPIOp, GPIO_PIN_RESET);
    HAL_Delay(50);
    HAL_GPIO_WritePin(IST8310_GPIOx, IST8310_GPIOp, GPIO_PIN_SET);
    HAL_Delay(50);

    // 基础配置
    // 不使能中断，直接读取
    WriteSingleDataFromIST8310(IST8310_CNTL2_ADDR, IST8310_STAT2_NONE_ALL);
    // 平均采样四次
    WriteSingleDataFromIST8310(IST8310_AVGCNTL_ADDR, IST8310_AVGCNTL_FOURTH);
    // 200Hz的输出频率
    WriteSingleDataFromIST8310(IST8310_CNTL1_ADDR, IST8310_CNTL1_CONTINUE);

    ist8310_data->meg_error |= VerifyMegId(&ist8310_data->chip_id);
}
```

读取单个数据：

```C
uint8_t ReadSingleDataFromIST8310(uint8_t addr) {
    uint8_t data;
    HAL_I2C_Mem_Read(&IST8310_I2C, (IST8310_I2C_ADDR << 1), addr, I2C_MEMADD_SIZE_8BIT, &data, 1, 10);
    return data;
}
```

读取多个数据：

```C
void ReadMultiDataFromIST8310(uint8_t addr, uint8_t* data, uint8_t len) {
    HAL_I2C_Mem_Read(&IST8310_I2C, (IST8310_I2C_ADDR << 1), addr, I2C_MEMADD_SIZE_8BIT, data, len, 10);
}
```

写入单个数据：

```C
void WriteSingleDataFromIST8310(uint8_t addr, uint8_t data) {
    HAL_I2C_Mem_Write(&IST8310_I2C, (IST8310_I2C_ADDR << 1), addr, I2C_MEMADD_SIZE_8BIT, &data, 1, 10);
}
```

写入多个数据：

```C
void WriteMultiDataFromIST8310(uint8_t addr, uint8_t* data, uint8_t len) {
    HAL_I2C_Mem_Write(&IST8310_I2C, (IST8310_I2C_ADDR << 1), addr, I2C_MEMADD_SIZE_8BIT, data, len, 10);
}
```

这里会发现一个比较有意思的事情，就是这里的地址都左移了一位，是因为根据I2C协议，[7:0]的一个字节的数据，前七位是地址，后一位是代表读或者写的位，这样子就需要把地址左移

读取磁力计数据：

```C
void ReadIST8310Data(ist8310_raw_data_t* meg_data) {
    uint8_t buf[6];
    int16_t temp_ist8310_data = 0;
    ReadMultiDataFromIST8310(IST8310_DATA_XL_ADDR, buf, 6);
    temp_ist8310_data = (int16_t)((buf[1] << 8) | buf[0]);
    meg_data->x = MAG_SEN * temp_ist8310_data;
    temp_ist8310_data = (int16_t)((buf[3] << 8) | buf[2]);
    meg_data->y = MAG_SEN * temp_ist8310_data;
    temp_ist8310_data = (int16_t)((buf[5] << 8) | buf[4]);
    meg_data->z = MAG_SEN * temp_ist8310_data;
}
```

这里乘了一个系数MAG_SEN，它的值是0.3，是将读取到的数据转化为单位为uT的磁场值

下面就是源码，把`IST8310_INIT()`函数放在程序开始的地方，然后剩下的读取函数放在不断执行的线程里，就可以得到磁力计数据了

`ist8310.c`

```C
/**
 * @Author         : Minghang Li
 * @Date           : 2022-12-03 14:29
 * @LastEditTime   : 2022-12-03 16:52
 * @Note           :
 * @Copyright(c)   : Minghang Li Copyright
 */
#include "ist8310.h"

#include <string.h>

#include "i2c.h"
#include "ist8310reg.h"

void IST8310_INIT(ist8310_data_t* ist8310_data) {
    memset(ist8310_data, 0, sizeof(ist8310_data_t));

    ist8310_data->meg_error = IST8310_NO_ERROR;

    // 把磁力计重启
    HAL_GPIO_WritePin(IST8310_GPIOx, IST8310_GPIOp, GPIO_PIN_RESET);
    HAL_Delay(50);
    HAL_GPIO_WritePin(IST8310_GPIOx, IST8310_GPIOp, GPIO_PIN_SET);
    HAL_Delay(50);

    // 基础配置
    // 不使能中断，直接读取
    WriteSingleDataFromIST8310(IST8310_CNTL2_ADDR, IST8310_STAT2_NONE_ALL);
    // 平均采样四次
    WriteSingleDataFromIST8310(IST8310_AVGCNTL_ADDR, IST8310_AVGCNTL_FOURTH);
    // 200Hz的输出频率
    WriteSingleDataFromIST8310(IST8310_CNTL1_ADDR, IST8310_CNTL1_CONTINUE);

    ist8310_data->meg_error |= VerifyMegId(&ist8310_data->chip_id);
}

uint8_t ReadSingleDataFromIST8310(uint8_t addr) {
    uint8_t data;
    HAL_I2C_Mem_Read(&IST8310_I2C, (IST8310_I2C_ADDR << 1), addr, I2C_MEMADD_SIZE_8BIT, &data, 1, 10);
    return data;
}

void WriteSingleDataFromIST8310(uint8_t addr, uint8_t data) {
    HAL_I2C_Mem_Write(&IST8310_I2C, (IST8310_I2C_ADDR << 1), addr, I2C_MEMADD_SIZE_8BIT, &data, 1, 10);
}

void ReadMultiDataFromIST8310(uint8_t addr, uint8_t* data, uint8_t len) {
    HAL_I2C_Mem_Read(&IST8310_I2C, (IST8310_I2C_ADDR << 1), addr, I2C_MEMADD_SIZE_8BIT, data, len, 10);
}

void WriteMultiDataFromIST8310(uint8_t addr, uint8_t* data, uint8_t len) {
    HAL_I2C_Mem_Write(&IST8310_I2C, (IST8310_I2C_ADDR << 1), addr, I2C_MEMADD_SIZE_8BIT, data, len, 10);
}

void ReadIST8310Data(ist8310_raw_data_t* meg_data) {
    uint8_t buf[6];
    int16_t temp_ist8310_data = 0;
    ReadMultiDataFromIST8310(IST8310_DATA_XL_ADDR, buf, 6);
    temp_ist8310_data = (int16_t)((buf[1] << 8) | buf[0]);
    meg_data->x = MAG_SEN * temp_ist8310_data;
    temp_ist8310_data = (int16_t)((buf[3] << 8) | buf[2]);
    meg_data->y = MAG_SEN * temp_ist8310_data;
    temp_ist8310_data = (int16_t)((buf[5] << 8) | buf[4]);
    meg_data->z = MAG_SEN * temp_ist8310_data;
}

ist8310_error_e VerifyMegId(uint8_t* id) {
    *id = ReadSingleDataFromIST8310(IST8310_CHIP_ID_ADDR);
    if (*id != IST8310_CHIP_ID_VAL) {
        return MEG_ID_ERROR;
    } else {
        return IST8310_NO_ERROR;
    }
}

```

`ist8310.h`

```
/**
 * @Author         : Minghang Li
 * @Date           : 2022-12-03 14:29
 * @LastEditTime   : 2022-12-03 16:49
 * @Note           :
 * @Copyright(c)   : Minghang Li Copyright
 */
#pragma once

#include <stdint.h>

typedef struct ist8310_raw_data_t {
    float x;
    float y;
    float z;
} ist8310_raw_data_t;

typedef enum ist8310_error_e {
    IST8310_NO_ERROR = 0x00,
    MEG_ID_ERROR = 0x01,
} ist8310_error_e;

typedef struct ist8310_data_t {
    uint8_t chip_id;
    ist8310_raw_data_t meg_data;
    ist8310_error_e meg_error;
} ist8310_data_t;

/*-----整形向uT转换-----*/
#define MAG_SEN 0.3f

/*-----I2C接口定义-----*/
#define IST8310_I2C_ADDR 0x0E
#define IST8310_I2C hi2c3

/*-----GPIO口定义-----*/
#define IST8310_GPIOx GPIOG
#define IST8310_GPIOp GPIO_PIN_6

void IST8310_INIT(ist8310_data_t* ist8310_data);

// 基础读取函数
uint8_t ReadSingleDataFromIST8310(uint8_t addr);
void WriteSingleDataFromIST8310(uint8_t addr, uint8_t data);
void ReadMultiDataFromIST8310(uint8_t addr, uint8_t* data, uint8_t len);
void WriteMultiDataFromIST8310(uint8_t addr, uint8_t* data, uint8_t len);

// 功能函数
void ReadIST8310Data(ist8310_raw_data_t* meg_data);

// 校验函数
ist8310_error_e VerifyMegId(uint8_t* id);

```

`ist8310reg.h`

```
/**
 * @Author         : Minghang Li
 * @Date           : 2022-12-03 15:27
 * @LastEditTime   : 2022-12-03 16:53
 * @Note           :
 * @Copyright(c)   : Minghang Li Copyright
 */
#pragma once

/*-----IST8310寄存器地址-----*/
#define IST8310_CHIP_ID_ADDR 0x00
#define IST8310_CHIP_ID_VAL 0x10

#define IST8310_STAT1_ADDR 0x02

#define IST8310_DATA_XL_ADDR 0x03
#define IST8310_DATA_XH_ADDR 0x04
#define IST8310_DATA_YL_ADDR 0x05
#define IST8310_DATA_YH_ADDR 0x06
#define IST8310_DATA_ZL_ADDR 0x07
#define IST8310_DATA_ZH_ADDR 0x08

#define IST8310_STAT2_ADDR 0x09

#define IST8310_CNTL1_ADDR 0x0A
#define IST8310_CNTL1_SLEEP 0x00
#define IST8310_CNTL1_SINGLE 0x01
#define IST8310_CNTL1_CONTINUE 0x0B

#define IST8310_CNTL2_ADDR 0x0B
#define IST8310_STAT2_NONE_ALL 0x00

#define IST8310_SELF_CHECK_ADDR 0x0C

#define IST8310_TEMPL_ADDR 0x1C
#define IST8310_TEMPH_ADDR 0x1D

#define IST8310_AVGCNTL_ADDR 0x41
#define IST8310_AVGCNTL_TWICE 0x09
#define IST8310_AVGCNTL_FOURTH 0x12
```

效果如下：
![image-20221203171539401](https://git.nrs-lab.com/LiMinghang23m/picgo-pic/-/raw/main/pictures/2023/01/18_11_48_45_275c18206f1dadb023bf19e5d13377c3.png)
