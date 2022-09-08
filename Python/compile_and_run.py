"""工具模块 用于渲染和不必要的语法检查"""
import importlib
import sys
import traceback
import multiprocessing

from multiprocessing.pool import AsyncResult
from typing import List

from PIL import Image


_WIDTH = 512
_HEIGHT = 512
_DURATION = 6
_FRAME_PER_SEC = 25


def compile_program() -> tuple[bool, str]:
    """装模作样语法检查

    返回值:
        tuple[bool, str]: (是否成功, 消息)
    """
    try:
        importlib.import_module('render')
    except ImportError as err:
        traceback.print_exc()
        return (False, err.msg)
    return (True, "运行成功")


def _render_frame(f: int, rd, gr, bl) -> Image.Image:
    frame = Image.new('RGB', (_WIDTH, _HEIGHT), (0, 0, 0))
    for x in range(_WIDTH):
        for y in range(_HEIGHT):
            r = rd(x, y, f / _FRAME_PER_SEC)
            g = gr(x, y, f / _FRAME_PER_SEC)
            b = bl(x, y, f / _FRAME_PER_SEC)
            frame.putpixel((x, y), (r, g, b))
    return frame


def render_gif(output_path: str) -> tuple[bool, str]:
    """渲染并输出 GIF 文件

    参数:
        output_path (str): GIF 文件输出路径

    返回值:
        tuple[bool, str]: (是否成功, 消息)
    """
    import render as render_lib

    with multiprocessing.Pool(processes=6) as pool:
        frames: List[Image.Image] = []
        results: List[AsyncResult] = []
        for f in range(_DURATION * _FRAME_PER_SEC):
            res = pool.apply_async(_render_frame, (f, render_lib.rd, render_lib.gr, render_lib.bl))
            results.append(res)

        cnt = 0
        for res in results:
            print(f"\rrendering frame {cnt}", end="")
            frame = res.get()
            frames.append(frame)
            cnt += 1
            sys.stdout.flush()

        frames[0].save(output_path,
                       save_all=True,
                       append_images=frames[1:],
                       optimize=False,
                       duration=1000 // _FRAME_PER_SEC,
                       loop=0)
        print()
        return (True, "运行成功")
