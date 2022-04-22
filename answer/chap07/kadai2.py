#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import chardet
from urllib import request


def get_url_contents(url):
    response = request.urlopen(url)
    stream   = response.read()
    # chardet.detectで文字コードを推測
    encoding = chardet.detect(stream).get('encoding')
    return stream.decode(encoding)


def get_html_title(contents):
    # titleタグのパターン
    pattern = r'<title>(.*)</title>'

    # 検索してタグの中身を取り出す
    match = re.search(pattern, contents)
    if match is not None:
        return match.groups()[0]
    else:
        return 'Error: title tag was not found'


if __name__ == '__main__':
    contents = get_url_contents(sys.argv[1])
    print(get_html_title(contents))
