import '../utils/global';
import * as jsR from '../src/js';
import * as tsR from '../src/ts';
let ren: typeof tsR;
function renderFrame(fn: number) {
    const f = fn / FPS;
    const imgBuf = new Uint8ClampedArray(DIM * DIM * 4);
    for (let x = 0; x < DIM; x++) {
        for (let y = 0; y < DIM; y++) {
            const i = (x + y * DIM) * 4;
            imgBuf[i + 0] = ren.RD(x, y, f);
            imgBuf[i + 1] = ren.GR(x, y, f);
            imgBuf[i + 2] = ren.BL(x, y, f);
            imgBuf[i + 3] = 255;
        }
    }
    return imgBuf;
}
export default function worker({ rename, fn }: { rename: 'ts' | 'js'; fn: number }) {
    if (rename === 'ts') {
        ren = tsR;
    } else if (rename === 'js') {
        ren = jsR;
    } else {
        throw new Error('Invalid renderer');
    }
    return renderFrame(fn);
}
