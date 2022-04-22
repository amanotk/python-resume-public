#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Print Greetings')
    # 整数
    parser.add_argument('-i', '--integer', type=int,
                       help='number of output')
    # 文字列
    parser.add_argument('-g', '--greeting', type=str,
                       help='greeting')
    # 真偽値（デフォルトはFalse）
    parser.add_argument('-c', '--capitalize', action='store_true', default=False,
                        help='capitalize or not')

    # デフォルトではsys.argvをパース
    return parser.parse_args()


def print_parse_result(args):
    # sys.argvを出力
    print('*** command-line arguments\n' +
          '{}'.format(sys.argv))
    print()
    # パース結果を出力
    print('*** parse results')
    kwargs = vars(args)
    for key, val in kwargs.items():
        print('option: {} => {}'.format(key, val))
    print()


if __name__ == '__main__':
    args = parse_args()
    print_parse_result(args)

    # パースしたオプションを使う
    print('*** show greetings')
    for i in range(args.integer):
        if args.capitalize:
            print(args.greeting.title())
        else:
            print(args.greeting)
