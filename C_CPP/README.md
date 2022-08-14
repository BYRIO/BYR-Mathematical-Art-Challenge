## C/C++

编写`render.h`。我们在`handy_math.h`中为你提供了一些便利的数学方法，你可以随意使用它们。

### 编写的额外要求

- C语言使用C11标准
- C++不允许使用STL，使用C++14标准
- 统一在`C_CPP/render.h`中编写。

### 环境要求

- Linux/MacOSX: `make`和`g++`
- Windows: [Visual Studio](https://visualstudio.microsoft.com/zh-hans/downloads/)和[Cmake](https://cmake.org/download/)

要求编译器支持C++14标准（这个标准现在已经被大多数编译器支持，通常你不需要太过担心这一点）

### 手动编译和运行

虽然更推荐使用[快速构建脚本](../README.md#快速构建脚本)来构建和运行这个项目，但是你仍然可以通过如下流程手动构建运行：

**Linux/MacOSX下**:
在shell中执行如下命令：

```bash
cd C_CPP
make render
```

即可得到可执行的渲染文件`render`，使用`./render`执行，得到输出`result.gif`。

**Windows+Visual Studio**: 
在CMD或PowerShell里运行以下代码：

```cmd
cd C_CPP
.\win_msvc.bat
```

即可得到可执行的渲染文件`render.exe`，使用`.\render.exe`执行，得到输出`result.gif`。