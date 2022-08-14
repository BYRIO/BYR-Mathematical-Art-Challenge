"""渲染函数模块

这个文件是你参赛时使用的、允许修改的文件。
分别在 `rd` `gr` `bl` 里填写你的渲染函数。
渲染时，会在同一像素位置 (x, y) 上分别调用
这三个函数获取像素位置的颜色 (R, G, B)。
"""

from math import *

from handy_math import *


FPS = 25
FPS_INV = 1.0 / FPS
TMAX = 6.0
DIM = 512
DM1 = (DIM - 1)

# image size
N = DIM
N1 = DIM - 1


def rd(x: int, y: int, t: float) -> int:
    """像素红色

    参数:
        x (int): x 坐标
        y (int): y 坐标
        t (float): 时间 (单位：秒)

    返回值:
        int: 红色值 (0-255)
    """
    # 在这里填写你的代码
    return 0


def gr(x: int, y: int, t: float) -> int:
    """像素绿色

    参数:
        x (int): x 坐标
        y (int): y 坐标
        t (float): 时间 (单位：秒)

    返回值:
        int: 绿色值 (0-255)
    """
    # 在这里填写你的代码
    return 0


def bl(x: int, y: int, t: float) -> int:
    """像素蓝色

    参数:
        x (int): x 坐标
        y (int): y 坐标
        t (float): 时间 (单位：秒)

    返回值:
        int: 蓝色值 (0-255)
    """
    # 在这里填写你的代码
    return 0
