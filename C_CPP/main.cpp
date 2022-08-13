#include <string.h>

#include <cstdio>
#include <cstdlib>

#include "gif.h"
#include "render.h"

static unsigned char framebuffer[DIM * DIM * 4];

void pixel_write(int, int, float);
int main() {
  float t = 0.0;
  GifWriter gWriter;
  int delay = FPS_INV * 100.0;
  int iframe = 0;
  int frameTotal = TMAX * FPS;
  GifBegin(&gWriter, "result.gif", DIM, DIM, delay);
  while (t < TMAX) {
    iframe++;
    printf("\rRendering frame (%d/%d) sec.",
           iframe <= frameTotal ? iframe : frameTotal, frameTotal);
    fflush(stdout);
    for (int y = 0; y < DIM; y++) {
      for (int x = 0; x < DIM; x++) {
        pixel_write(x, y, t);
      }
    }
    GifWriteFrame(&gWriter, framebuffer, DIM, DIM, delay);
    t += FPS_INV;
  }
  printf("\n");
  GifEnd(&gWriter);
  return 0;
}
void pixel_write(int x, int y, float t) {
  int base = y * DIM + x;
  base = base << 2;
  framebuffer[base] = RD(x, y, t) & 255;
  framebuffer[base + 1] = GR(x, y, t) & 255;
  framebuffer[base + 2] = BL(x, y, t) & 255;
  framebuffer[base + 3] = 255;
}