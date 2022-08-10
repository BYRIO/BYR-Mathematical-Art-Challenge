# BYR-Mathematical-Art-Challenge

北邮人数学艺术挑战赛，灵感参考[Tweetable Mathematical Art](http://codegolf.stackexchange.com/questions/35569/tweetable-mathematical-art)

## 介绍 Description

生成一幅图像的本质是一个建立一个屏幕空间到颜色空间的映射关系，因此我们完全可以使用一段很短的代码来生成一幅具有艺术性的图像。本次挑战中，我们要求参赛者使用**限定长度**的代码来编写**三个函数（R、G、B）**，最终生成一张*大小*512x512，*时长*8秒的**动图**。

等待提交截止后，我们会在北京邮电大学校内发起投票，让同学们票选出自己心目中最优秀的作品。

## 规则 Rules

首先，本次比赛使用MIT开源协议，所有提交者必须以某种形式（GitHub/Gitee）**开源**自己的代码。提交时，需要提交自己的**仓库地址**和**渲染结果**。比赛**允许**查阅资料，但是**不允许**抄袭、滥用的行为。

本次比赛允许使用以下几种语言：

- C/C++
- JavaScript
- Rust

我们已经把各个语言对应的startup文件放置在对应名字的文件夹下了，你要做的是按照规则编写对应的渲染函数：RD、GR、BL，分别对应红、绿、蓝三个颜色分量。

其中，渲染函数形如（以C/C++语言为例）：

```c
unsigned char RD(int x, int y, float t);
```

前两个参数为像素的横坐标和纵坐标，第三个参数为时间，以秒为单位，我们会以24fps（一秒均匀截取24帧）为标准传入第三个参数；输出的是颜色分量的值。前两个参数为整数，范围${0,1, 2...,511}$，第三个参数为浮点数，范围$[0.0, 8.0]$；输出为范围在$[0, 255]$的整数。

我们的一些常规要求如下：

- 每个函数的长度**不超过200个字符**（不包括函数的声明部分，只包含函数体）
- 不允许额外引入第三方库和系统库、不允许读取外部文件，只能使用程序**过程化地生成图片**

其中对于各个不同的语言的额外要求如下

### C & C++

编写`render.h`。

C语言使用C11标准；C++不允许使用STL，使用C++14标准。统一在`C_CPP/render.h`中编写。

#### 编译和运行

**Linux/MacOSX下**：我们假设你安装了make和**g++**并且其支持c++14标准，执行如下命令：

```bash
cd C_CPP
make render
```

即可得到可执行的渲染文件`render`，使用`./render`执行，得到输出`result.gif`。

**Windows下（我们更建议你使用MSYS2或者WSL环境来使用Linux完成）**：我们假设你安装了make和[clang++](https://github.com/llvm/llvm-project/releases/download/llvmorg-14.0.6/LLVM-14.0.6-win64.exe)并且其支持c++14标准，在`PowerShell`下执行如下命令：

```bash
cd C_CPP
make render
```

即可得到可执行的渲染文件`render`，使用`.\render.exe`执行，得到输出`result.gif`。

### JavaScript

TODO

### Rust

TODO
