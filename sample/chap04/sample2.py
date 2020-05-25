#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# forループ
#

# 一番シンプルな例
for i in range(5):
    print(i)

# 1つおきのループ
for i in range(0, 5, 2):
    print('i     = ', i)
    print('i + 1 = ', i+1)

# 2重ループの例
for i in range(1, 3):
    for j in range(1, 5):
        print('i = ', i, ', j = ', j, ', i*j = ', i*j)

# テイラー展開の公式でsin(x)の近似値を求める
import math

x = 0.2

print('*** Taylor expansion of sin(x) ***')

y = x
a = x
i = 1
print('x = ', x)
print('i = ', i, ' --- sin(x) = ', y)

for i in range(3, 10, 2):
    a = -a / ((i-1)*i) * x**2
    y = y + a
    print('i = ', i, ' --- sin(x) = ', y)

print('exact   --- sin(x) = ', math.sin(x))
