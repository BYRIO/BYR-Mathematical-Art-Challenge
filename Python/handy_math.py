from typing import Tuple


f = float  
"""float 别名"""


def d2(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    """二维向量数量积"""
    return a[0] * b[0] + a[1] * b[1]


def d3(a: Tuple[float, float, float], b: Tuple[float, float, float]) -> float:
    """三维向量数量积"""
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def a2(a: Tuple[float, float], b: Tuple[float, float]) -> Tuple[float, float]:
    """二维向量加"""
    return (a[0] + b[0], a[1] + b[1])


def a3(a: Tuple[float, float, float], b: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """三维向量加"""
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def n2(a: Tuple[float, float]) -> Tuple[float, float]:
    """二维向量取反"""
    return (-a[0], -a[1])


def n3(a: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """三维向量取反"""
    return (-a[0], -a[1], -a[2])


def s2(a: Tuple[float, float], b: Tuple[float, float]) -> Tuple[float, float]:
    """二维向量减"""
    return a2(a, n2(b))


def s3(a: Tuple[float, float, float], b: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """三维向量减"""
    return a3(a, n3(b))


def m2(a: Tuple[float, float], b: Tuple[float, float]) -> Tuple[float, float]:
    """二维向量乘"""
    return (a[0] * b[0], a[1] * b[1])


def m3(a: Tuple[float, float, float], b: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """三维向量乘"""
    return (a[0] * b[0], a[1] * b[1], a[2] * b[2])


def di2(a: Tuple[float, float], b: Tuple[float, float]) -> Tuple[float, float]:
    """二维向量除"""
    return (a[0] / b[0], a[1] / b[1])


def di3(a: Tuple[float, float, float], b: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """三维向量除"""
    return (a[0] / b[0], a[1] / b[1], a[2] / b[2])


def no2(a: Tuple[float, float]) -> float:
    """二维向量单位向量"""
    return d2(a, a)


def no3(a: Tuple[float, float, float]) -> float:
    """三维向量单位向量"""
    return d3(a, a)
