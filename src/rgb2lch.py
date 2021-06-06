#!/usr/bin/env python3
# coding: utf8
#from labconstants import LabConstants
#from rgb2xyz import rgb2xyz
from rgb2lab import rgb2lab
from lab2lch import lab2lch
def rgb2lch(rgb):
    R, G, B = rgb
    l, a, b = rgb2lab(rgb)
    return lab2lch((l, a, b))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='色空間を変換する。RGB->LCh', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('rgb', help="色。カンマ区切りで渡す。0 <= R,G,B <= 255")
    args = parser.parse_args()
    rgb = args.rgb.split(',')
    rgb[0] = int(rgb[0])
    rgb[1] = int(rgb[1])
    rgb[2] = int(rgb[2])
    l, c, h = rgb2lch(rgb)
    print('%f,%f,%f' % (l, c, h))

