#!/usr/bin/env python3
# coding: utf8
from labconstants import LabConstants
from rgb2xyz import rgb2xyz
def rgb2lab(rgb):
    r, g, b = rgb
    x, y, z = rgb2xyz(rgb);
    l = 116 * y - 16;
    return (0 if l < 0 else l, 500 * (x - y), 200 * (y - z))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='色空間を変換する。RGB->Lab', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('rgb', help="色。カンマ区切りで渡す。0 <= R,G,B <= 255")
    args = parser.parse_args()
    rgb = args.rgb.split(',')
    rgb[0] = int(rgb[0])
    rgb[1] = int(rgb[1])
    rgb[2] = int(rgb[2])
    l, a, b = rgb2lab(rgb)
    print('%f,%f,%f' % (l, a, b))

