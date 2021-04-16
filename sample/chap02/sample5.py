#!/usr/bin/env python
# -*- coding: utf-8 -*-

###
### printf形式
###
s = '%s is more powerful than %s' % ('Python', 'Fortran')
print(s)

i = 2021
a = 3.1415
b = 2.7182
print("i  = %-5d" % (i))
print("pi = %4.2f" % (a))
print("e  = %5.3f" % (b))

###
### format()
###
# "Python is more powerful than Fortran" が出力される
s = "{} is more powerful than {}".format('Python', 'Fortran')
print(s)

# "Fortran is more powerful than Python" が出力される
s = "{1} is more powerful than {0}".format('Python', 'Fortran')
print(s)

print("i  = {:-5d}".format(i))
print("pi = {:4.2f}".format(a))
print("e  = {:5.3f}".format(b))
