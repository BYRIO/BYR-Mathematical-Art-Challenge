import '../utils/global';
import * as jsR from '../src/js';
import * as tsR from '../src/ts';

import { cpus } from 'os';
import Piscina from 'piscina';
import { program } from 'commander';
import GIFEncoder from 'gifencoder';
import { createWriteStream } from 'fs';
import { dirname, resolve } from 'path';
import { SingleBar } from 'cli-progress';
import { pipeline } from 'stream/promises';

program
    .option('-t, --threads <number>', 'number of threads', cpus().length.toString())
    .option('-f, --from <number>', 'start frame', '0')
    .option('-l, --length <number>', 'number of frames', (TMAX * FPS).toString())
    .argument('<output>', 'Output file')
    .action(async (output) => {
        console.log('BMAC JS/TS Build Script');
        let rename: 'ts' | 'js';
        const threads = Number(program.opts().threads) || cpus().length * 2;
        const startFrame = Number(program.opts().from) || 0;
        const totalFrames = Number(program.opts().length) || TMAX * FPS;
        if (tsR.useThis) {
            rename = 'ts';
        } else if (jsR.useThis) {
            rename = 'js';
        } else {
            console.log('Error: No renderer selected');
            process.exit(2);
        }
        // convert import.meta.url to __dirname
        let __dirname = dirname(decodeURI(new URL(import.meta.url).pathname));
        // if windows
        if (process.platform === 'win32') {
            __dirname = __dirname.substr(1);
        }
        const p = new Piscina({
            filename: resolve(__dirname, './worker.js'),
            maxThreads: threads,
        });
        console.log(
            `Rendering frmaes ${startFrame}-${
                startFrame + totalFrames - 1
            } with ${threads} threads with ${rename.toUpperCase()} renderer...`,
        );
        const encoder = new GIFEncoder(DIM, DIM);
        const stream = encoder.createReadStream();
        encoder.start();
        encoder.setRepeat(0); // 0 for repeat, -1 for no-repeat
        encoder.setDelay(FPS_INV * 1000); // frame delay in ms
        encoder.setQuality(10);
        const bar = new SingleBar(
            {},
            {
                format: '[{bar}] {percentage}% | ETA: {eta}s | {value}/{total}',
                barCompleteChar: '=',
                barIncompleteChar: '-',
            },
        );
        bar.start(totalFrames, 0);
        const promises = [];
        let nowtime = Date.now();
        let renderedFrame = startFrame;
        const cachedFrames = new Map<number, Uint8ClampedArray>();
        for (let fn = startFrame; fn < totalFrames; fn++) {
            promises.push(
                p.run({ rename, fn }).then((imgBuf) => {
                    if (renderedFrame == fn) {
                        encoder.addFrame(imgBuf);
                        bar.increment();
                        renderedFrame++;
                        while (cachedFrames.has(renderedFrame)) {
                            encoder.addFrame(cachedFrames.get(renderedFrame) as any);
                            cachedFrames.delete(renderedFrame);
                            renderedFrame++;
                            bar.increment();
                        }
                    } else if (renderedFrame < fn) {
                        cachedFrames.set(fn, imgBuf);
                    } else {
                        throw new Error('Invalid frame sequence');
                    }
                }),
            );
        }
        await Promise.all(promises);
        encoder.finish();
        bar.update(totalFrames);
        bar.stop();
        console.log('Saving GIF...');
        await pipeline(stream, createWriteStream(output));
        console.log('Done in ' + ((Date.now() - nowtime) / 1000).toFixed(2) + 's.');
    })
    .parse(process.argv);
