# BYR-Mathematical-Art-Challenge

![GitHub](https://img.shields.io/github/license/Hyiker/BYR-Mathematical-Art-Challenge?style=flat-square)

北邮人数学艺术挑战赛，灵感来自[Tweetable Mathematical Art](http://codegolf.stackexchange.com/questions/35569/tweetable-mathematical-art)

## 介绍 Description

生成一幅图像的本质是一个建立一个屏幕空间到颜色空间的映射关系，因此我们完全可以使用一段很短的代码来生成一幅具有艺术性的图像。本次挑战中，我们要求参赛者使用**限定长度**的代码来编写**三个函数（R、G、B）**，最终生成一张大小512x512，时长6秒、25FPS（总共150帧）的**动态图像GIF**。

![JuliaSet](./assets/example.gif)

举个例子，上面的JuliaSet图像我们可以用下面的代码生成：

```c++
unsigned char RD(int x, int y, float t) {v2 c=v2(-0.8,cos(t)*0.2);v2 z = v2(2.0*x/f(N-1)-1.0,2.0*(f(y)/N-0.5));int i=0;while(no2(z)<20&&i<50){v2 s=v2(z.x*z.x-z.y*z.y,z.x*z.y*2.0);z=a2(c,s);i++;}return 255-i*5.1;}
unsigned char GR(int x, int y, float t) {v2 c=v2(-0.8,cos(t)*0.2);v2 z = v2(2.0*x/f(N-1)-1.0,2.0*(f(y)/N-0.5));int i=0;while(no2(z)<20&&i<50){v2 s=v2(z.x*z.x-z.y*z.y,z.x*z.y*2.0);z=a2(c,s);i++;}return 255-i*5.1;}
unsigned char BL(int x, int y, float t) {v2 c=v2(-0.8,cos(t)*0.2);v2 z = v2(2.0*x/f(N-1)-1.0,2.0*(f(y)/N-0.5));int i=0;while(no2(z)<20&&i<50){v2 s=v2(z.x*z.x-z.y*z.y,z.x*z.y*2.0);z=a2(c,s);i++;}return 255-i*5.1;}
```

上面的每个函数体中的代码长度都只有170个字符。

等待提交截止后，我们会在北京邮电大学校内发起投票，让各位同学们票选出自己心目中最优秀的作品。

## 规则 Rules

首先，本次比赛使用MIT开源协议，所有提交者必须以某种形式（GitHub/Gitee）**开源**自己的代码（最简单的办法：Fork这个仓库，然后编写自己的代码）。提交时，需要提交自己的**仓库地址**和**渲染结果**。比赛**允许**查阅资料，但是**不允许**抄袭、滥用的行为，相关行为一经举报查证，成绩将立即作废。

我们已经把各个语言对应的startup文件放置在对应名字的文件夹下了，你要做的是按照规则编写对应的渲染函数：RD、GR、BL，分别对应红、绿、蓝三个颜色分量。

其中，渲染函数形如（以C/C++语言为例）：

```c
unsigned char RD(int x, int y, float t);
```

前两个参数为像素的横坐标和纵坐标，第三个参数为时间，以秒为单位，我们会以24fps（一秒均匀截取24帧）为标准传入第三个参数；输出的是颜色分量的值。前两个参数为整数，范围{0,1, 2...,511}，第三个参数为浮点数，范围[0.0, 6.0]；输出为范围在[0, 255]的整数。

我们的一些常规要求如下：

- 如果没有特别说明，每个函数的长度**不超过200个字符**（不包括函数的声明部分，只包含函数体，不包括最外层的大括号）
- 只能使用math.h标准库和我们提供的一些数学方法，不能使用额外的库文件
- 不允许读取外部文件，只能使用程序**过程化地生成图片**
- 你只能在这三个函数的函数体中编写代码，不能额外添加函数（但是你可以在函数中编写闭包函数）

我们支持用以下这些语言提交，其中对于各个不同的语言的额外要求如下：

- [C/C++](./C_CPP/README.md)
- [JavaScript](./JavaScript/README.md)
- [Rust](./Rust/README.md)
- [Python](./Python/README.md)
- [Java](./Java/README.md)

### 快速构建脚本

我们提供了一个脚本`run.py`来自动进行编译、运行、编码等工作以减轻参赛者的心智负担，我们假定你的计算机上已经下载了[python运行环境](https://www.python.org/downloads/)。

1. 编写对应的语言代码
2. 安装python依赖`pip install -r requirements_dev.txt`
3. 依照说明修改脚本中的`language`变量
4. 运行脚本（linux和macos用户需要自行安装ffmpeg，windows下会自动从服务器拉取可用的ffmpeg二进制预编译exe）`python run.py`
5. 项目根目录下即可找到`result.mp4`

### 提示 Hint

对于参加比赛的选手，我们有如下的建议和提示：

- 你可以在debug的时候任意改变渲染的图像数目和FPS来加速你的debug速度，但是记住请务必按照比赛要求提交渲染结果，否则记录无效
- 你可以在编写的时候正常定义函数，提交的时候再进行**代码压缩**

### 一些有用的参考资料 Reference

- 太极图形课：[程序动画：生成你的第一个二维动画](https://www.bilibili.com/video/BV14Q4y1q7C9)
- [ShaderToys](https://www.shadertoy.com/)
- Inigo Quilez[Intro to Painting with Maths](https://www.youtube.com/watch?v=0ifChJ0nJfM&t=778s)

## 协议 LICENSE

此{项目, 比赛}遵循MIT开源协议。
