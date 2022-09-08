# Typescript & Javascript 

也许你可能对类型很在意，因此你可以用TS/JS中的任何一个编写你的渲染代码。

你只需要：
 - 安装依赖。我们推荐使用先进的`pnpm`，但你可以使用任意你喜欢的包管理器
 - 打开`src`文件夹
 - 根据喜好完成`js.js`或者`ts.ts`
 - 在你完成的文件的第一行，设置`export const useThis = true`
 - `pnpm render result.gif`！(`npm run render result.gif`也不是不可以)
 - 查看你的`result.gif`。

工具函数位于`utils/global.ts`下，这些工具函数均已被挂载到全局上下文（globalThis），可以直接使用。同时，`Math`对象中的所有函数也已经被挂在到全局上下文中。

你可以在代码中通过全局对象`$`自由定义在多个函数之间共享的变量，如`$.a=1`，也可以使用nodejs的内置模块，但是不允许安装NPM包。

一个和其他语言一样的JuliaSet渲染代码如下：
```ts
export const useThis: boolean = true;
export const RD = (x: number, y: number, t: number) => {
    let c = v2(-0.8, cos(t) * 0.2);
    let z = v2((2.0 * x) / (N - 1) - 1.0, 2.0 * (y / N - 0.5));
    let i = 0;
    while (no2(z) < 20 && i < 50) {
        let s = v2(z.x * z.x - z.y * z.y, z.x * z.y * 2.0);
        z = a2(c, s);
        i++;
    }
    return 255 - i * 5.1;
};
export const GR = (x: number, y: number, t: number) => {
    return RD(x, y, t);
};
export const BL = (x: number, y: number, t: number) => {
    return RD(x, y, t);
};
```

### 构建脚本的额外参数
```
Usage: render [options] <output>
Arguments:
  output                  Output file
Options:
  -t, --threads <number>  number of threads (default: "cpus")
  -f, --from <number>     start frame (default: "0")
  -l, --length <number>   number of frames (default: "150")
```

如你所见，你可以通过指定参数来实现一些调试目的。比如，你可以指定从第10帧开始渲染，只渲染10帧，来让调试更方便；你也可以修改线程数。 **注意：** 特别高的线程数可能会导致主线程里只能同步阻塞执行的GIF Encoder卡住，从而变得比较少的线程数更慢。