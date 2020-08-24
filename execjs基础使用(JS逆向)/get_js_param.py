# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/1 12:23
@file: get_js_param.py
@desc: 
"""
# 获得有道翻译salt 、sign 、ts
import execjs
import hashlib


def get_salt():
    # word = 'how are you'
    js = '''
        function salt(word) { 
            r = "" + (new Date).getTime();
            i = r + parseInt(10 * Math.random(), 10);
            g = word
            return g
        }
    '''
    resp = execjs.compile(js)
    salt_data = resp.call('salt', 'how')
    return salt_data


if __name__ == '__main__':
    a = get_salt()
    print(a)