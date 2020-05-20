#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# whileループ
#

# 一番シンプルな例
i = 0
while i < 5:
    print(i)
    i += 1

# テイラー展開の公式でsin(x)の近似値が真の値に十分近づくまで計算する
import math

x = 0.2
i = 1
y = x
a = x
ytrue = math.sin(x)
print('i = ', i, ' --- sin(x) = ', y)

while abs((ytrue - y)/ytrue) > 1.0e-10:
    i += 2
    a = -a / ((i-1)*i) * x**2
    y = y + a
    print('i = ', i, ' --- sin(x) = ', y)

print('approximated = ', y)
print('exact        = ', ytrue)
print('rel. error   = ', abs((ytrue-y)/ytrue))
