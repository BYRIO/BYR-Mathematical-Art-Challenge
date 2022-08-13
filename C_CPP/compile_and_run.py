# 默认根路径已经设置为了对应语言下的文件夹
import subprocess as sp
import platform
import shutil
import os

'''返回
bool: 是否编译成功
str: 编译的message，将会打印'''


def compile() -> tuple[bool, str]:
    sp.run(['make', 'clean'])
    result = sp.run(['make', 'render'])
    if result.returncode == 0:
        return True, '编译成功'
    else:
        return False, '编译失败'


'''返回
bool: 是否运行成功
str: 运行的message，将会打印'''


def render(gif_path: str) -> tuple[bool, str]:
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
