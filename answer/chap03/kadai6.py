#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# (注) listとin演算子を使うとよりスマートに記述できる
#
while 1:
    s = input('')
    if s == 'apple' or s == 'orange' or s == 'banana':
        print('---', s, 'is food')
    elif s == 'dog' or s == 'cat' or s == 'lion':
        print('---', s, 'is animal')
    elif s == 'car' or s == 'airplane' or s == 'motorcycle':
        print('---', s, 'is vehicle')
    elif s == 'exit':
        print('Now exit program...')
        break
    else:
        print('---', s, 'is others')
