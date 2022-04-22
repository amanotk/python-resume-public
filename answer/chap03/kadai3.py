#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

for i in range(19):
    x = i * 10.0
    y = x * math.pi/180
    print(x, math.sin(y), math.cos(y))
