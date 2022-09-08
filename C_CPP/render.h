#include "handy_math.h"
#include <math.h>

#define FPS 25
#define FPS_INV (1.0 / FPS)
#define TMAX 6.0
#define DIM 512
#define DM1 (DIM - 1)
// image size
#define N DIM
#define N1 (DIM - 1)

unsigned char RD(int x, int y, float t) {v2 c=v2(-0.8,cos(t)*0.2);v2 z = v2(2.0*x/f(N-1)-1.0,2.0*(f(y)/N-0.5));int i=0;while(no2(z)<20&&i<50){v2 s=v2(z.x*z.x-z.y*z.y,z.x*z.y*2.0);z=a2(c,s);i++;}return 255-i*5.1;}
unsigned char GR(int x, int y, float t) {v2 c=v2(-0.8,cos(t)*0.2);v2 z = v2(2.0*x/f(N-1)-1.0,2.0*(f(y)/N-0.5));int i=0;while(no2(z)<20&&i<50){v2 s=v2(z.x*z.x-z.y*z.y,z.x*z.y*2.0);z=a2(c,s);i++;}return 255-i*5.1;}
unsigned char BL(int x, int y, float t) {v2 c=v2(-0.8,cos(t)*0.2);v2 z = v2(2.0*x/f(N-1)-1.0,2.0*(f(y)/N-0.5));int i=0;while(no2(z)<20&&i<50){v2 s=v2(z.x*z.x-z.y*z.y,z.x*z.y*2.0);z=a2(c,s);i++;}return 255-i*5.1;}
