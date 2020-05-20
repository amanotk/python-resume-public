#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# ifによる分岐の基本
#
status = True

# インデントに注意
print('*** Now I am going to check status ***')

# ifによる分岐
if status:
    print('status is True')  # インデントが１段下がる
else:
    print('status is False') # ここも１段下がる

# ここからインデントが戻る
print('*** Checking status is done ***')


#
# 入れ子にするなどより細かい制御
#
a = 1
b = 2
c = 3

print('** A little more complicated example ***')

if a:
    print('a = ', a)
    # ifを入れ子にする
    if a + b > c:
        print('a + b > c')
    elif a + b < c:
        print('a + b < c')
    elif a + b == c:
        # さらに入れ子にする
        if c >= 0:
            print('a + b = c and c >= 0')
        else:
            print('a + b = c and c <  0')
    else:
        # passを使って「何もしない」ことを明示することもできる
        pass
# トップレベルのifに対応するelseは省略

#
# 論理演算子を使う例
#
print('** Use logical operators for complex conditionals ***')

if a < b and a < c:
    print('a is smaller than both b and c')

if a < b or a < c:
    print('a is smaller than either b or c')

if (a == 1 and a + b == c) or not (a == 1 and b == 2 and c == 3):
    print('example of complex conditional')
