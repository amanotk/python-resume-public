#!/usr/bin/env python
# -*- coding: utf-8 -*-

delta = 1.0e-3
alpha = 1.0 + delta

# alphaを変化させながら実行
while alpha < 3.0:
    p = 0.9
    # 初期の100個
    for i in range(100):
        p = p + alpha*p*(1-p)
    # 100から200までを出力
    for i in range(101):
        print(alpha, p)
        p = p + alpha*p*(1-p)
    alpha += delta
