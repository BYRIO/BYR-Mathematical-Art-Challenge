import platform
import subprocess as sp


def compile_program() -> tuple[bool, str]:
    left = ['cmd', '/c', 'mvn'] if platform.system() == 'Windows' else ['mvn']
    result = sp.run(left + ['package'], check=False)
    if result.returncode != 0:
        return False, "maven构建发生错误"
    return True, '构建成功'


def render_gif(gif_path: str) -> tuple[bool, str]:
    result = sp.run(
        ['java', '-jar', 'target/byrmathematicalartchallenge.jar', gif_path], check=False)
    if result.returncode != 0:
        return False, 'gif渲染时发生错误'
    return True, '渲染成功'
