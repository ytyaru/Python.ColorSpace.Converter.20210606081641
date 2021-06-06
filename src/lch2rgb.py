#!/usr/bin/env python3
# coding: utf8
from lch2lab import lch2lab
from lab2rgb import lab2rgb 
def lch2rgb(lch):
    l, c, h = lch;
    L, a, b = lch2lab(lch);
    R, G, B = lab2rgb((L,a,b));
    return (R, G, B)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='色空間を変換する。LCh->RGB', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('lch', help="色。カンマ区切りで渡す。\n  0.0 <= l <= 100.0\n  0.0 <= c <= 133.81586\n  0.0 <= h <= 360.0")
    args = parser.parse_args()
    lch = args.lch.split(',')
    lch[0] = float(lch[0])
    lch[1] = float(lch[1])
    lch[2] = float(lch[2])
    r, g, b = lch2rgb(lch)
    print('%d,%d,%d' % (r, g, b))

