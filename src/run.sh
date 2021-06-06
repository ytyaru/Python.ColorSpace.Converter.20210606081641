#!/usr/bin/env bash
set -Ceu
#---------------------------------------------------------------------------
# LabからRGBへ変換する。
# https://syncer.jp/color-converter
# CreatedAt: 2021-06-06
#---------------------------------------------------------------------------
Run() {
	THIS="$(realpath "${BASH_SOURCE:-0}")"; HERE="$(dirname "$THIS")"; PARENT="$(dirname "$HERE")"; THIS_NAME="$(basename "$THIS")"; APP_ROOT="$PARENT";
	L=45.0
	a=37.0
	b=52.0
	"$HERE/lab2rgb.py" $L,$a,$b

	L=55.0
	C=32.0
	h=65.0
	"$HERE/lab2rgb.py" $("$HERE/lch2lab.py" $L,$C,$h)

	R=175
	G=77
	B=11
	"$HERE/rgb2lab.py" $R,$G,$B

	L=45.0
	a=37.0
	b=52.0
	"$HERE/lab2lch.py" $L,$a,$b

	R=175
	G=77
	B=11
	"$HERE/rgb2lch.py" $R,$G,$B
}
Run "$@"
