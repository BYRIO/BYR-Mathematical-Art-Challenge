## C/C++

编写`render.h`。我们在`handy_math.h`中为你提供了一些便利的数学方法，你可以随意使用它们。

C语言使用C11标准；C++不允许使用STL，使用C++14标准。统一在`C_CPP/render.h`中编写。

### 编译和运行

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