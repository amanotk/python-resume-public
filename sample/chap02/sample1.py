#!/usr/bin/env python
# -*- coding: utf-8 -*-

# これはコメント行
if 1:
    # pythonでは構文ブロックは全てインデント（字下げ）によって区切られる
    print('Hello')
    print('This will be printed out')
else:
    # ここには到達しない
    print('This will be ignored')


# ここでは sys という名前のモジュールを import する
# プログラムを実行途中で終了するには sys.exit を呼ぶ
# sys.exitに与える整数は終了コード（通常は0が正常終了でそれ以外は異常終了）
import sys

if 1:
    sys.exit(0)
else:
    sys.exit(-1)
