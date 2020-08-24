# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/17 18:40
@file: aiqiyi.py
@desc: 
"""
# 未完成

import execjs
import os

os.environ["EXECJS_RUNTIME"] = "PhantomJS"
node = execjs.get()
with open('do_js.js') as f:
    res = f.read()

js = node.compile(res)
b = js.call('start')
print('js.b=', b)