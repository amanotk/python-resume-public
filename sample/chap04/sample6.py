#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 以下の呼び出しはエラー(この時点ではhelloは定義されていない)
#hello1()

def hello2(name):
    hello1() # 実行時にhello1が定義済みであればOK
    print('I am', name)

# 以下の呼び出しもエラー(この時点ではhello2が呼び出すhello1は定義されていない)
#hello2('John')

def hello1():
    print('Hello')

hello1()
hello2('John')
