#[derive(Debug, Clone, Copy)]
pub struct V2(pub f32, pub f32);

#[derive(Debug, Clone, Copy)]
pub struct V3(pub f32, pub f32, f32);

pub fn v2(x: f32, y: f32) -> V2 {
    return V2(x, y);
}

pub fn v3(x: f32, y: f32, z: f32) -> V3 {
    return V3(x, y, z);
}

// Vector dot
pub fn d2(V2(x1, y1): V2, V2(x2, y2): V2) -> f32 {
    return x1 * x2 + y1 * y2;
}

pub fn d3(V3(x1, y1, z1): V3, V3(x2, y2, z2): V3) -> f32 {
    return x1 * x2 + y1 * y2 + z1 * z2;
}

// Vector add
pub fn a2(V2(x1, y1): V2, V2(x2, y2): V2) -> V2 {
    return v2(x1 + x2, y1 + y2);
}

pub fn a3(V3(x1, y1, z1): V3, V3(x2, y2, z2): V3) -> V3 {
    return v3(x1 + x2, y1 + y2, z1 + z2);
}

// Vector negative
pub fn n2(V2(x, y): V2) -> V2 {
    return v2(-x, -y);
}

pub fn n3(V3(x, y, z): V3) -> V3 {
    return v3(-x, -y, -z);
}

// Vector subtraction
pub fn s2(V2(x1, y1): V2, V2(x2, y2): V2) -> V2 {
    return v2(x1 - x2, y1 - y2);
}

pub fn s3(V3(x1, y1, z1): V3, V3(x2, y2, z2): V3) -> V3 {
    return v3(x1 - x2, y1 - y2, z1 - z2);
}

// Vector multiplication
pub fn m2(V2(x1, y1): V2, V2(x2, y2): V2) -> V2 {
    return v2(x1 * x2, y1 * y2);
}

pub fn m3(V3(x1, y1, z1): V3, V3(x2, y2, z2): V3) -> V3 {
    return v3(x1 * x2, y1 * y2, z1 * z2);
}

// Vector division
pub fn div2(V2(x1, y1): V2, V2(x2, y2): V2) -> V2 {
    return v2(x1 / x2, y1 / y2);
}

pub fn div3(V3(x1, y1, z1): V3, V3(x2, y2, z2): V3) -> V3 {
    return v3(x1 / x2, y1 / y2, z1 / z2);
}

// Norm of vector
pub fn no2(V2(x, y): V2) -> f32 {
    return d2(V2(x, y), V2(x, y));
}

pub fn no3(V3(x, y, z): V3) -> f32 {
    return d3(V3(x, y, z), V3(x, y, z));
}