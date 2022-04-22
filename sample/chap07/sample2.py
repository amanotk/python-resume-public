#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def find_functions(src):
    # 関数定義のパターン
    pattern = r'^\W*def\W+([a-zA-Z0-9_]+)\((.*)\):'
    # ファイルを全て読み込む
    with open(src, 'r') as f:
        text = f.read()
    # ファイルから読み込んだ文字列の中から関数定義を検索
    for m in re.finditer(pattern, text, re.MULTILINE):
        groups = m.groups()
        if len(groups) >= 1:
            # 関数名
            name = groups[0]
            # 引数リスト
            args = groups[1].split(', ')
            while args.count('') > 0:
                args.remove('')
            narg = len(args)
            print('found function named {} with {} argument(s)'.format(name, narg))


def test_func1():
    pass


def test_func2(x, y):
    pass


if __name__ == '__main__':
    # __file__ はこのファイルの名前
    find_functions(__file__)
