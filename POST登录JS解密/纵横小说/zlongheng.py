# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/23 12:46
@file: zlongheng.py
#https://passport.zongheng.com/
获取参数pwd
"""
import execjs
import os

os.environ["EXECJS_RUNTIME"] = "PhantomJS"
node = execjs.get()
with open('zongheng_js.js') as f:
    res = f.read()

js = node.compile(res)
b = js.call('start', '123123')
print('js.b=', b)