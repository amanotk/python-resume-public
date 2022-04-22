#!/usr/bin/env python
# -*- coding: utf-8 -*-

N = int(input('Input N : '))
epsilon = float(input('Input epsilon : '))

if not (N > 1 and 0 < epsilon and epsilon < 1):
    # 途中で終了するには sys.exit を用いる
    import sys
    sys.exit(-1)


import math

status = False
etrue = math.exp(1.0)
e = 0.0
c = 1.0
for i in range(N+1):
    e = e + c
    c = c / (i+1)
    # 収束判定
    if abs((etrue-e)/etrue) < epsilon:
        status = True
        break

# 収束したかどうか
if status:
    print('Converged !')
else:
    print('Did not converge !')

# 結果の表示
print('N                  : ', i)
print('Exact value        : ', etrue)
print('Approximated value : ', e)
print('Error              : ', abs((etrue-e)/etrue))
