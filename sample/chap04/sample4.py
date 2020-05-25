#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# 複雑な反復処理
#

i = 1
while True:
    i += 1
    if   i%2 == 0:
        print('Multiple of 2 --- ', i)
        continue
    elif i%3 == 0:
        print('Multiple of 3 --- ', i)
        continue
    elif i%5 == 0:
        print('Multiple of 5 --- ', i)
        continue
    elif i >= 10:
        print('Exit')
        break
    print('Not a multiple of 2, 3, 5 --- ', i)
