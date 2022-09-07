# Java 脚手架使用说明

> 很遗憾你选择了 Java
> 
> 和其它脚手架相比，它太重了不是吗

本文档将简单介绍 Java 脚手架的目录与使用方法。

## Java 脚手架的目录结构

```
Java
├─README.md
├─compile_and_run.py
├─pom.xml
├─src
|  ├─m/j/w/b/b
|  |     ├─AbstractRender.java
|  |     ├─ByrMathematicalArtChallenge.java
|  |     ├─GifSequenceWriter.java
|  |     ├─Render.java
|  |     ├─model
|  |     |   ├─V2.java
|  |     |   └-V3.java
```

- `pom.xml` maven pom 文件

- `m/j/w/b/b/Render.java` 渲染类 **唯一一个用户可修改的代码文件**

- `m/j/w/b/b/AbstractRender.java` 抽象渲染类，`Render` 继承自本类。为了方便使用最少的代码量编写渲染函数，这个类内置了很多数学函数，直接访问即可 **调试时可以修改本类的一些常量以加快渲染速度，但记得不要提交这些修改**

- `m/j/w/b/b/model/V2.java` 二维向量

- `m/j/w/b/b/model/V3.java` 三维向量

- `m/j/w/b/b/ByrMathematicalArtChallenge.java` 程序入口

- `m/j/w/b/b/GifSequenceWriter.java` GIF Writer

## 使用方法

本小结以生成 JuliaSet 图像为例，介绍脚手架的使用方法。

![alt](example.gif)

要生成上方的图像，在Render中填写以下三个实现即可。

```java
public int red(int x, int y, double t) {
    V2 c = v2(-0.8, Math.cos(t) * 0.2);
    V2 z = v2(2.0 * x / f(N - 1) - 1.0, 2.0 * (f(y) / N - 0.5));
    int i = 0;
    while (no2(z) < 20 && i < 50) {
        V2 s = v2(z.x * z.x - z.y * z.y, z.x * z.y * 2.0);
        z = a2(c, s);
        i++;
    }
    return (int) Math.round(255 - i * 5.1);
}

public int green(int x, int y, double t) {
    V2 c = v2(-0.8, Math.cos(t) * 0.2);
    V2 z = v2(2.0 * x / f(N - 1) - 1.0, 2.0 * (f(y) / N - 0.5));
    int i = 0;
    while (no2(z) < 20 && i < 50) {
        V2 s = v2(z.x * z.x - z.y * z.y, z.x * z.y * 2.0);
        z = a2(c, s);
        i++;
    }
    return (int) Math.round(255 - i * 5.1);
}

public int blue(int x, int y, double t) {
    V2 c = v2(-0.8, Math.cos(t) * 0.2);
    V2 z = v2(2.0 * x / f(N - 1) - 1.0, 2.0 * (f(y) / N - 0.5));
    int i = 0;
    while (no2(z) < 20 && i < 50) {
        V2 s = v2(z.x * z.x - z.y * z.y, z.x * z.y * 2.0);
        z = a2(c, s);
        i++;
    }
    return (int) Math.round(255 - i * 5.1);
}
```

填写完代码后，需要运行程序生成 GIF 图像。构建依赖于 Maven。

如果你是 IDEA 和 Eclipse 之类IDE的用户，你只需要配置好 Maven ，指定 `ByrMathematicalArtChallenge` 为主类 `Run / Debug` 即可，默认渲染完成后会输出到工作目录的 `output.gif`。

如果你想直接使用 `vim` 等编辑器完成开发，请使用 `maven package` 构建 JAR 包制品，指令执行完成后，`target` 目录下会出现 `byrmathematicalartchallenge.jar`，你只需要使用 `java -jar <jar path>` 执行这个 JAR 即可。

使用愉快 :)  -- YozakuraDoge
