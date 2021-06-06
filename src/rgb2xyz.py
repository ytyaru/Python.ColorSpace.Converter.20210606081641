#!/usr/bin/env python3
# coding: utf8
from labconstants import LabConstants
def rgb2xyz(rgb):
    r, g, b = rgb
    r = rgb_xyz(r)
    g = rgb_xyz(g)
    b = rgb_xyz(b)
    x = xyz_lab((0.4124564 * r + 0.3575761 * g + 0.1804375 * b) / LabConstants.Xn)
    y = xyz_lab((0.2126729 * r + 0.7151522 * g + 0.0721750 * b) / LabConstants.Yn)
    z = xyz_lab((0.0193339 * r + 0.1191920 * g + 0.9503041 * b) / LabConstants.Zn)
    return (x,y,z)

def rgb_xyz(r):
    r /= 255.0
    if r <= 0.04045: return r / 12.92
    return pow((r + 0.055) / 1.055, 2.4)

def xyz_lab(t):
    if t > LabConstants.t3: return pow(t, 1 / 3)
    return t / LabConstants.t2 + LabConstants.t0

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='色空間を変換する。RGB->XYZ', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('rgb', help="色。カンマ区切りで渡す。0 <= R,G,B <= 255")
    args = parser.parse_args()
    rgb = args.rgb.split(',')
    rgb[0] = int(rgb[0])
    rgb[1] = int(rgb[1])
    rgb[2] = int(rgb[2])
    r, g, b = rgb2xyz(rgb)
    print('%f,%f,%f' % (r, g, b))

