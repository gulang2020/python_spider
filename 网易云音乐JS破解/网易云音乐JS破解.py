# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/13 16:09
@file: 网易云音乐JS破解.py
@desc: 
"""
import execjs

with open('test3.js') as f:
    res = f.read()

js = execjs.compile(res)
b = js.call('start')
print(b)