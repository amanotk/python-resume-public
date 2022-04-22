#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import datetime
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Simple emulation of ls command')
    parser.add_argument('-S', action='store_true', default=False,
                        help='sort in size')
    parser.add_argument('-r', action='store_true', default=False,
                        help='reverse sort order')
    args = parser.parse_args()

    # ソートキー
    if args.S:
        key = 'size'
    else:
        key = 'name'

    # ソートオーダー
    reverse = args.r

    return key, reverse

def myls(dirname, key=None, reverse=False):
    if key is None:
        key == 'name'

    # ファイルリストと属性値を取得
    files = list()
    with os.scandir(dirname) as it:
        for entry in it:
            name = entry.name
            stat = entry.stat()
            files.append(dict(name=name,
                              size=stat.st_size,
                              time=stat.st_mtime))

    # ソート
    if key == 'name':
        files.sort(key=lambda x: x['name'], reverse=False ^ reverse)
    elif key == 'size':
        files.sort(key=lambda x: x['size'], reverse=True ^ reverse)
    elif key == 'time':
        files.sort(key=lambda x: x['time'], reverse=True ^ reverse)
    else:
        raise ValueError('Error: Invaid sort key: {}'.format(key))

    # フォーマットして出力
    for f in files:
        t = datetime.datetime.fromtimestamp(f['time'])
        f['timestr'] = t.ctime()
        print('{size:8d} {timestr} {name}'.format(**f))


if __name__ == '__main__':
    key, reverse = parse_args()
    myls('.', key, reverse)
