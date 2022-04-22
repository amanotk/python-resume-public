#!/usr/bin/env python
# -*- coding: utf-8 -*-

###
### カレントディレクトリのpythonソースの行数をそれぞれ表示する
###

import os
import subprocess


def count_py_lines1(dirname):
    print('*** count_by_lines1')
    # ファイルとディレクトリのリスト
    files = os.listdir(dirname)
    files.sort()
    for f in files:
        # 拡張子をチェックしてpythonのソースであれば行数を数える
        if os.path.splitext(f)[1] == '.py':
            with open(f, 'r') as fp:
                c = len(fp.readlines())
            print('{} : number of lines = {}'.format(f, c))


def count_py_lines2(dirname):
    print('*** count_by_lines2')
    # wcコマンドで行数を数える
    cmd = 'wc -l {}/*.py'.format(dirname)
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    # コマンドの出力からファイル名と行数を取り出す
    for line in r.stdout.split('\n'):
        l = line.strip().split()
        if len(l) == 2 and os.path.splitext(l[1])[1] == '.py':
            c = l[0]
            f = os.path.split(l[1])[1]
            print('{} : number of lines = {}'.format(f, c))


if __name__ == '__main__':
    # pythonのみで実装したもの
    count_py_lines1('.')
    # シェルコマンドの結果を処理したもの
    count_py_lines2('.')
