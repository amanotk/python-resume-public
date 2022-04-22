#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = int(input('Input m: '))
b = int(input('Input n: '))

m = a
n = b
r = m%n
while r != 0:
    m = n
    n = r
    r = m%n

print('Greatest common divisor of ', a, 'and', b, ' : ', n)
