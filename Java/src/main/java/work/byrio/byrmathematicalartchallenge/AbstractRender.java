package work.byrio.byrmathematicalartchallenge;

import work.byrio.byrmathematicalartchallenge.model.V2;
import work.byrio.byrmathematicalartchallenge.model.V3;

import javax.imageio.stream.FileImageOutputStream;
import javax.imageio.stream.ImageOutputStream;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

/**
 * 渲染抽象类，提供基本的数学函数与渲染功能。
 *
 * @author YozakuraDoge
 */
public abstract class AbstractRender {
    protected static final int WIDTH = 512;
    protected static final int HEIGHT = 512;
    protected static final int DURATION = 6;
    protected static final int FPS = 25;
    protected static final int N = WIDTH;
    protected static final int N1 = WIDTH - 1;

    protected V2 v2(double x, double y) {
        return new V2(x, y);
    }

    protected V3 v3(double x, double y, double z) {
        return new V3(x, y, z);
    }

    /**
     * 转 double
     *
     * @param v 值
     * @return double 值
     */
    protected double f(int v) {
        return v;
    }

    /**
     * 转 double
     *
     * @param v 值
     * @return double 值
     */
    protected double f(long v) {
        return v;
    }

    /**
     * 二维向量数量积
     *
     * @param a 向量 a
     * @param b 向量 b
     * @return 数量积
     */
    protected double d2(V2 a, V2 b) {
        return a.x * b.x + a.y * b.y;
    }

    /**
     * 三维向量数量积
     *
     * @param a 向量 a
     * @param b 向量 b
     * @return 数量积
     */
    protected double d3(V3 a, V3 b) {
        return a.x * b.x + a.y * b.y + a.z * b.z;
    }

    /**
     * 二维向量加
     *
     * @param a 向量 a
     * @param b 向量 b
     * @return 结果向量
     */
    protected V2 a2(V2 a, V2 b) {
        return new V2(a.x + b.x, a.y + b.y);
    }

    /**
     * 三维向量加
     *
     * @param a 向量 a
     * @param b 向量 b
     * @return 结果向量
     */
    protected V3 a3(V3 a, V3 b) {
        return new V3(a.x + b.x, a.y + b.y, a.z + b.z);
    }

    /**
     * 二维向量取反
     *
     * @param a 向量 a
     * @return 结果向量
     */
    protected V2 n2(V2 a) {
        return new V2(-a.x, -a.y);
    }

    /**
     * 三维向量取反
     *
     * @param a 向量 a
     * @return 结果向量
     */
    protected V3 n3(V3 a) {
        return new V3(-a.x, -a.y, -a.z);
    }

    /**
     * 二维向量减
     *
     * @param a 向量 a
     * @param b 向量 b
     * @return 结果向量
     */
    protected V2 s2(V2 a, V2 b) {
        return a2(a, n2(b));
    }

    /**
     * 三维向量减
     *
     * @param a 向量 a
     * @param b 向量 b
     * @return 结果向量
     */
    protected V3 s3(V3 a, V3 b) {
        return a3(a, n3(b));
    }

    /**
     * 二维向量乘
     *
     * @param a 向量 a
     * @param b 向量 b
     * @return 结果向量
     */
    protected V2 m2(V2 a, V2 b) {
        return new V2(a.x * b.x, a.y * b.y);
    }

    /**
     * 三维向量乘
     *
     * @param a 向量 a
     * @param b 向量 b
     * @return 结果向量
     */
    protected V3 m3(V3 a, V3 b) {
        return new V3(a.x * b.x, a.y * b.y, a.z * b.z);
    }

    /**
     * 二维向量除
     *
     * @param a 向量 a
     * @param b 向量 b
     * @return 结果向量
     */
    protected V2 di2(V2 a, V2 b) {
        return new V2(a.x / b.x, a.y / b.y);
    }

    /**
     * 三维向量除
     *
     * @param a 向量 a
     * @param b 向量 b
     * @return 结果向量
     */
    protected V3 di3(V3 a, V3 b) {
        return new V3(a.x / b.x, a.y / b.y, a.z / b.z);
    }

    /**
     * 二维向量范数
     *
     * @param a 向量 a
     * @return 结果向量
     */
    protected double no2(V2 a) {
        return d2(a, a);
    }

    /**
     * 三维向量范数
     *
     * @param a 向量 a
     * @return 结果向量
     */
    protected double no3(V3 a) {
        return d3(a, a);
    }

    /**
     * 返回红色值
     *
     * @param x x 坐标
     * @param y y 坐标
     * @param t 时间
     * @return 红色值
     */
    protected abstract int red(int x, int y, double t);

    /**
     * 返回绿色值
     *
     * @param x x 坐标
     * @param y y 坐标
     * @param t 时间
     * @return 绿色值
     */
    protected abstract int green(int x, int y, double t);

    /**
     * 返回蓝色值
     *
     * @param x x 坐标
     * @param y y 坐标
     * @param t 时间
     * @return 蓝色值
     */
    protected abstract int blue(int x, int y, double t);

    /**
     * 渲染并保存 GIF 到指定路径
     *
     * @param outputPath 输出路径 (foo/bar.gif)
     */
    public void render(String outputPath) {
        ImageOutputStream imageStream;
        GifSequenceWriter gifWriter;

        try {
            imageStream = new FileImageOutputStream(new File(outputPath));
            gifWriter = new GifSequenceWriter(
                    imageStream, BufferedImage.TYPE_INT_RGB, 1000 / FPS, true);
        } catch (Exception e) {
            System.out.println("fail to create GifSequenceWriter: " + e.getMessage());
            return;
        }

        for (int f = 0; f < DURATION * FPS; f++) {
            System.out.print("\rrendering frame " + f);
            System.out.flush();
            BufferedImage frame = new BufferedImage(WIDTH, HEIGHT, BufferedImage.TYPE_INT_RGB);
            for (int x = 0; x < WIDTH; x++) {
                for (int y = 0; y < HEIGHT; y++) {
                    int r = red(x, y, (double) f / FPS);
                    int g = green(x, y, (double) f / FPS);
                    int b = blue(x, y, (double) f / FPS);
                    frame.setRGB(x, y, new Color(r, g, b).getRGB());
                }
            }
            try {
                gifWriter.writeToSequence(frame);
            } catch (IOException e) {
                System.out.println("gif writer error on frame " + f + "(time: " + f / FPS + "s)");
                break;
            }
        }
        System.out.println();

        try {
            gifWriter.close();
            imageStream.flush();
            imageStream.close();
        } catch (IOException e) {
            System.out.println("fail to close GifSequenceWriter: " + e.getMessage());
        }
    }
}
