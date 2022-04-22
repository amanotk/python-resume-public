#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input('Input n : '))
m = int(input('Input m : '))

if n < m:
    print(n, 'is smaller than', m)
elif n > m:
    print(n, 'is larger than', m)
else:
    print(n, 'is equal to', m)
