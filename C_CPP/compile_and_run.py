# 默认根路径已经设置为了对应语言下的文件夹
import os
import subprocess as sp
import platform
import shutil

'''返回
bool: 是否编译成功
str: 编译的message，将会打印'''


def _check_toolchain(plat) -> bool:
    tool = 'cmake' if plat == 'Windows' else 'make'
    try:
        sp.call([tool, '--version'], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
        return True
    except:
        return False


def compile_program() -> tuple[bool, str]:
    plat = platform.system()
    if not _check_toolchain(plat):
        return False, '没有检测到编译工具链或者工具链损坏，请阅读README.md按照指示安装'
    if plat == 'Windows':
        result = sp.run(['cmake', '-B', 'build'])
        if result.returncode != 0:
            return False, '使用cmake预构建时出错'
        result = sp.run(['cmake', '--build', 'build', '--config', 'Release'])
        if result.returncode != 0:
            return False, '使用cmake+msvc编译时出错'
        shutil.copy(os.path.join('build', 'Debug', 'render.exe'), '.\\render.exe')
    else:
        sp.run(['make', 'clean'])
        result = sp.run(['make', 'render'])
    if result.returncode == 0:
        return True, '编译成功'
    else:
        return False, '编译失败'


'''返回
bool: 是否运行成功
str: 运行的message，将会打印'''


def render_gif(gif_path: str) -> tuple[bool, str]:
    system_str = platform.system()
    if system_str == 'Windows':
        exe = '.\\render.exe'
    else:
        exe = './render'
    result = sp.run([exe])
    if result.returncode == 0:
        shutil.copy('./result.gif', gif_path)
        return True, '运行成功'
    else:
        return False, '运行失败'
