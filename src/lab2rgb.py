#!/usr/bin/env python3
# coding: utf8
from labconstants import LabConstants
def lab2rgb(lab):
    import math
    l, a, b = lab

    y = (l + 16) / 116
    x = y if math.isnan(a) else y + a / 500
    z = y if math.isnan(b) else y - b / 200

    y = LabConstants.Yn * lab_xyz(y)
    x = LabConstants.Xn * lab_xyz(x)
    z = LabConstants.Zn * lab_xyz(z)

    r = xyz_rgb(3.2404542 * x - 1.5371385 * y - 0.4985314 * z)  # D65 -> sRGB
    g = xyz_rgb(-0.9692660 * x + 1.8760108 * y + 0.0415560 * z)
    b_ = xyz_rgb(0.0556434 * x - 0.2040259 * y + 1.0572252 * z)
    return (r, g, b_)

def xyz_rgb(r):
    return 255 * (12.92 * r if r <= 0.00304 else 1.055 * pow(r, 1 / 2.4) - 0.055)

def lab_xyz(t):
    return t * t * t if t > LabConstants.t1 else LabConstants.t2 * (t - LabConstants.t0)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='色空間を変換する。Lab->RGB', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('lab', help="色。カンマ区切りで渡す。\n  0.0 <= l <= 100.0\n  -86.18463 <= a <= 98.25422\n  -107.863686 <= b <= 94.48248")
    args = parser.parse_args()
    lab = args.lab.split(',')
    lab[0] = float(lab[0])
    lab[1] = float(lab[1])
    lab[2] = float(lab[2])
    r, g, b = lab2rgb(lab)
    print('%d;%d;%d' % (r, g, b))

