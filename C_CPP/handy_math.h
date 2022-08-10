#define _sq(x) ((x) * (x))                          // square
#define _cb(x) abs((x) * (x) * (x))                 // absolute value of cube
#define _cr(x) (unsigned char)(pow((x), 1.0 / 3.0)) // cube root
#define fr(x) ((x)-floor(x))                     // fraction
inline float clp(float val, float minVal, float maxVal) {
  return val >= minVal ? (val <= maxVal ? val : maxVal) : minVal;
}
// handy vector functions
struct v2 {
  float x, y;
  v2(float x, float y) : x(x), y(y) {}
};
struct v3 {
  float x, y, z;
  v3(float x, float y, float z) : x(x), y(y), z(z) {}
};
// vector dot
inline float d2(v2 a, v2 b) { return a.x * b.x + a.y * b.y; }
inline float d3(v3 a, v3 b) { return a.x * b.x + a.y * b.y + a.z * b.z; }
// vector addition
inline v2 a2(v2 a, v2 b) { return v2{a.x + b.x, a.y + b.y}; }
inline v3 a3(v3 a, v3 b) { return v3{a.x + b.x, a.y + b.y, a.z + b.z}; }
// vector negative
inline v2 n2(v2 a) { return v2{-a.x, -a.y}; }
inline v3 n3(v3 a) { return v3{-a.x, -a.y, -a.z}; }
// vector subtraction
inline v2 s2(v2 a, v2 b) { return a2(a, n2(b)); }
inline v3 s3(v3 a, v3 b) { return a3(a, n3(b)); }
// vector multiplication
inline v2 m2(v2 a, v2 b) { return v2{a.x * b.x, a.y * b.y}; }
inline v3 m3(v3 a, v3 b) { return v3{a.x * b.x, a.y * b.y, a.z * b.z}; }
// vector division
inline v2 di2(v2 a, v2 b) { return v2{a.x / b.x, a.y / b.y}; }
inline v3 di3(v3 a, v3 b) { return v3{a.x / b.x, a.y / b.y, a.z / b.z}; }
// norm of vector
inline float no2(v2 a) { return d2(a, a); }
inline float no3(v3 a) { return d3(a, a); }
#define f(x) float(x)
