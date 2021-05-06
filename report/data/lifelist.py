#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob

BASE = 'https://amanotk.github.io/python-resume-public/report/data/life/'
DIR  = 'life'

if __name__ == '__main__':
    ff = glob.glob(os.path.join(DIR, '*.lif'))
    html =\
'''\
<html>
<body>
<ul>
'''
    for f in ff:
        f = os.path.basename(f)
        html += '<li><a href="{:s}{:s}"> {:s} </a></li>\n'.format(BASE, f, f)
    html +=\
'''\
</ul>
</body>
</html>
'''
    print(html)
