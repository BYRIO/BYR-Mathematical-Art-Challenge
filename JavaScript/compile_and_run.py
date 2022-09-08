import os
from platform import platform
import shutil
import subprocess as sp


def _check_modules() -> bool:
    return os.system("npm run step:check") == 0


def compile_program() -> tuple[bool, str]:
    if not _check_modules():
        return False, "请先安装依赖！"
    if os.system("npm run step:compile") == 0:
        return True, "Type Check Passed"
    else:
        return False, "Type Check Faild"


def render_gif(gif_path: str) -> tuple[bool, str]:
    cmd = ["npm", "run",
           "step:run", gif_path]
    if platform() == "Windows":
        cmd = ["cmd", "/c"] + cmd
    result = sp.run(cmd, check=False)
    if result.returncode == 0:
        return True, "运行成功"
    else:
        return False, "运行失败"
