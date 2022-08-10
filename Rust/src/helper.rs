#[derive(Debug, Clone, Copy)]
pub struct V2(pub f32, pub f32);

pub fn v2(x: f32, y: f32) -> V2 {
    return V2(x, y);
}

pub fn d2(V2(x1, y1): V2, V2(x2, y2): V2) -> f32 {
    return x1 * x2 + y1 * y2;
}

pub fn a2(V2(x1, y1): V2, V2(x2, y2): V2) -> V2 {
    return v2(x1 + x2, y1 + y2);
}

pub fn no2(V2(x, y): V2) -> f32 {
    return d2(V2(x, y), V2(x, y));
}

pub fn cos(x: f32) -> f32 {
    return x.cos();
}