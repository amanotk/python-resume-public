#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = float(input('Input x : '))

c1 = x
c3 =-c1 * x**2 / (3*2)
c5 =-c3 * x**2 / (5*4)
c7 =-c5 * x**2 / (7*6)

print('1st order = ', c1)
print('3rd order = ', c1 + c3)
print('5th order = ', c1 + c3 + c5)
print('7th order = ', c1 + c3 + c5 + c7)

import math
print('exact     = ', math.sin(x))
