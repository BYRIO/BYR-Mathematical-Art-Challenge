import * as mathUtils from './math';
import * as constEnums from './const';
// install ts to global
declare global {
    const v2: typeof mathUtils.v2;
    const v3: typeof mathUtils.v3;
    const d2: typeof mathUtils.d2;
    const d3: typeof mathUtils.d3;
    const a2: typeof mathUtils.a2;
    const a3: typeof mathUtils.a3;
    const s2: typeof mathUtils.s2;
    const s3: typeof mathUtils.s3;
    const m2: typeof mathUtils.m2;
    const m3: typeof mathUtils.m3;
    const di2: typeof mathUtils.di2;
    const di3: typeof mathUtils.di3;
    const n2: typeof mathUtils.n2;
    const n3: typeof mathUtils.n3;
    const no2: typeof mathUtils.no2;
    const no3: typeof mathUtils.no3;
    const clp: typeof mathUtils.clp;
    const _sq: typeof mathUtils._sq;
    const _cb: typeof mathUtils._cb;
    const _cr: typeof mathUtils._cr;
    const fr: typeof mathUtils.fr;
    // extends Math
    const PI: number;
    const E: number;
    const sqrt: typeof Math.sqrt;
    const cbrt: typeof Math.cbrt;
    const pow: typeof Math.pow;
    const exp: typeof Math.exp;
    const log: typeof Math.log;
    const log2: typeof Math.log2;
    const log10: typeof Math.log10;
    const abs: typeof Math.abs;
    const ceil: typeof Math.ceil;
    const floor: typeof Math.floor;
    const round: typeof Math.round;
    const trunc: typeof Math.trunc;
    const sign: typeof Math.sign;
    const sin: typeof Math.sin;
    const cos: typeof Math.cos;
    const tan: typeof Math.tan;
    const asin: typeof Math.asin;
    const acos: typeof Math.acos;
    const atan: typeof Math.atan;
    const atan2: typeof Math.atan2;
    const sinh: typeof Math.sinh;
    const cosh: typeof Math.cosh;
    const tanh: typeof Math.tanh;
    const asinh: typeof Math.asinh;
    const acosh: typeof Math.acosh;
    const atanh: typeof Math.atanh;
    const hypot: typeof Math.hypot;
    const min: typeof Math.min;
    const max: typeof Math.max;
    const random: typeof Math.random;
    // const
    const N: number;
    const N1: number;
    const DIM: number;
    const DM1: number;
    const FPS: number;
    const FPS_INV: number;
    const TMAX: number;
    // globals
    const $: Record<string, any>;
}
// install to global
for (const key of Object.getOwnPropertyNames(mathUtils)) {
    // @ts-ignore
    globalThis[key] = mathUtils[key];
}
// install Math to global
for (const key of Object.getOwnPropertyNames(Math)) {
    // @ts-ignore
    globalThis[key] = Math[key];
}
// install const to global
for (const key of Object.getOwnPropertyNames(constEnums)) {
    // @ts-ignore
    globalThis[key] = constEnums[key];
}
// install globals to global
// @ts-ignore
globalThis.$ = {};