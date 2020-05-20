#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# approximation of exp(x) via taylor expansion up to order n
def exp_taylor(x, n):
    c = 1.0
    f = 1.0
    for i in range(n):
        c /= (i+1)
        f += c * x**(i+1)
    return f


# global variables for fibonacci
a =-1
b = 1

def fibonacci():
    # a and b refer to the global variables
    global a, b
    c = a + b
    a = b
    b = c
    return c


print('--- exp_taylor ---')
x = 0.5
print('x     = ', x)
print('1st   = ', exp_taylor(x, 1))
print('2nd   = ', exp_taylor(x, 2))
print('3rd   = ', exp_taylor(x, 3))
print('4th   = ', exp_taylor(x, 4))
print('5th   = ', exp_taylor(x, 5))
print('6th   = ', exp_taylor(x, 6))
print('7th   = ', exp_taylor(x, 7))
print('8th   = ', exp_taylor(x, 8))
print('exact = ', math.exp(x))

print('--- fibonacci ---')
for i in range(20):
    print(fibonacci())
