#!/usr/bin/env python3
# coding: utf8
from labconstants import LabConstants
def lab2lch(lab):
    import math
    l, a, b = lab;
    c = math.sqrt(a * a + b * b);
    h = (math.atan2(b, a) * (180 / math.pi) + 360) % 360;
    if 0 == round(c*10000): h = math.nan;
    return (l, c, h);

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='色空間を変換する。Lab->LCh', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('lab', help="色。カンマ区切りで渡す。\n  0.0 <= l <= 100.0\n  -86.18463 <= a <= 98.25422\n  -107.863686 <= b <= 94.48248")
    args = parser.parse_args()
    lab = args.lab.split(',')
    lab[0] = float(lab[0])
    lab[1] = float(lab[1])
    lab[2] = float(lab[2])
    l, c, h = lab2lch(lab)
    print('%f,%f,%f' % (l, c, h))

