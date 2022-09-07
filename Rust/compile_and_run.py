import os
import shutil
import subprocess as sp

def _check_cargo() -> bool:
    return os.system("cargo --version") == 0

def compile_program() -> tuple[bool, str]:
    if not _check_cargo():
        return False, "没有检测到编译工具链或者工具链损坏，请阅读README.md按照指示安装"
    if os.system("cargo build --release") == 0:
        return True, "编译成功"
    else:
        return False, "编译失败"

def render_gif(gif_path: str) -> tuple[bool, str]:
    result = sp.run(["cargo", "run", "--release"], check=False)
    if result.returncode == 0:
        shutil.copy('./result.gif', gif_path)
        return True, "运行成功"
    else:
        return False, "运行失败"