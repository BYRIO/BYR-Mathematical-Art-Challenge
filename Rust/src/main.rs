#![allow(dead_code)]

mod helper;
mod render;

use gif::{Frame, Encoder, Repeat};
use std::fs::File;

fn main() {
    let mut image = File::create("result.gif").unwrap();
    let mut encoder = Encoder::new(&mut image, render::DIM, render::DIM, &[]).unwrap();
    encoder.set_repeat(Repeat::Infinite).unwrap();
    
    let mut t = 0.0f32;
    let mut iframe = 0;
    let frame_total: u16 = render::TMAX as u16 * render::FPS;
    let mut data = vec![0; (render::DIM as usize * render::DIM as usize) * 4];
    let delay = (render::FPS_INV * 100.0) as u16;
    while t.lt(&render::TMAX) && iframe < frame_total {
        iframe += 1;
        print!("\rRendering GIF frame {} of {}", iframe, frame_total);
        for y in 0..render::DIM {
            for x in 0..render::DIM {
                let base = ((y as usize * render::DIM as usize + x as usize) as usize) << 2;
                let r = render::red(x.into(), y.into(), t);
                let g = render::green(x.into(), y.into(), t);
                let b = render::blue(x.into(), y.into(), t);
                data[base] = r & 255;
                data[base + 1] = g & 255;
                data[base + 2] = b & 255;
                data[base + 3] = 255 & 255;
            }
        }
        let mut frame = Frame::from_rgba(render::DIM, render::DIM, &mut data);
        frame.delay = delay;
        encoder.write_frame(&frame).unwrap();
        t += render::FPS_INV;
    }
}
