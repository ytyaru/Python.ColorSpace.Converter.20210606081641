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
}
Run "$@"
