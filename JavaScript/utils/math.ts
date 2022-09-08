/* 本工具类基于C_CPP中相关代码修改 */

export type v2 = { x: number; y: number };
export const v2 = (x: number, y: number): v2 => ({ x, y });

export type v3 = { x: number; y: number; z: number };
export const v3 = (x: number, y: number, z: number): v3 => ({ x, y, z });

/** 二维向量数量积 */
export const d2 = (a: v2, b: v2): number => a.x * b.x + a.y * b.y;
/** 三维向量数量积 */
export const d3 = (a: v3, b: v3): number => a.x * b.x + a.y * b.y + a.z * b.z;

/** 二维向量加 */
export const a2 = (a: v2, b: v2): v2 => ({ x: a.x + b.x, y: a.y + b.y });
/** 三维向量加 */
export const a3 = (a: v3, b: v3): v3 => ({ x: a.x + b.x, y: a.y + b.y, z: a.z + b.z });

/** 二维向量减 */
export const s2 = (a: v2, b: v2): v2 => ({ x: a.x - b.x, y: a.y - b.y });
/** 三维向量减 */
export const s3 = (a: v3, b: v3): v3 => ({ x: a.x - b.x, y: a.y - b.y, z: a.z - b.z });

/** 二维向量乘 */
export const m2 = (a: v2, b: number): v2 => ({ x: a.x * b, y: a.y * b });
/** 三维向量乘 */
export const m3 = (a: v3, b: number): v3 => ({ x: a.x * b, y: a.y * b, z: a.z * b });

/** 二维向量除 */
export const di2 = (a: v2, b: number): v2 => ({ x: a.x / b, y: a.y / b });
/** 三维向量除 */
export const di3 = (a: v3, b: number): v3 => ({ x: a.x / b, y: a.y / b, z: a.z / b });

/** 二维向量取反 */
export const n2 = (a: v2): v2 => ({ x: -a.x, y: -a.y });
/** 三维向量取反 */
export const n3 = (a: v3): v3 => ({ x: -a.x, y: -a.y, z: -a.z });

/** 二维向量范数 */
export const no2 = (a: v2): number => d2(a, a);
/** 三维向量范数 */
export const no3 = (a: v3): number => d3(a, a);

/** 将数字限制在[minVal, maxVal]之间 */
export function clp(val: number, minVal: number, maxVal: number): number {
    return val >= minVal ? (val <= maxVal ? val : maxVal) : minVal;
}

/** 平方 */
export const _sq = (x: number) => x * x;
/** 立方绝对值 */
export const _cb = (x: number) => Math.abs(x * x * x);
/** 立方根 */
export const _cr = (x: number) => Math.pow(x, 1.0 / 3.0);
/** 取小数部分 */
export const fr = (x: number) => x - Math.floor(x);
