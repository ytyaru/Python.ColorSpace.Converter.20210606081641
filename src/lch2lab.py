#!/usr/bin/env python3
# coding: utf8
def lch2lab(lch):
    import math
    l, c, h = lch
    if math.isnan(h): h = 0
    h = h * math.pi / 180;
    return (l, math.cos(h) * c, math.sin(h) * c)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='色空間を変換する。LCh->Lab', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('lch', help="色。カンマ区切りで渡す。\n  0.0 <= l <= 100.0\n  0.0 <= c <= 133.81586\n  0.0 <= h <= 360.0")
    args = parser.parse_args()
    lch = args.lch.split(',')
    lch[0] = float(lch[0])
    lch[1] = float(lch[1])
    lch[2] = float(lch[2])
    l, a, b = lch2lab(lch)
    print('%f,%f,%f' % (l, a, b))

