# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/1 12:11
@file: youdaofanyi.py
@desc:
有道翻译爬虫
"""
import requests
import get_js_param as gjp
import time
import hashlib
import random

# 找出salt 、sign 、ts的构造方法
# salt: 15962551925901
# sign: 2cc53672c23cbfbb877fdcbfc4c364ff
# ts: 1596255192590
word = "how old are you "

ts = str(int(time.time() * 1000))
print(ts)
salt = ts + str(random.randint(0, 9))
print(salt)
# sign: n.md5("fanyideskweb" + e + i + "mmbP%A-r6U3Nw(n]BjuEU")
# e是翻译的句子 i是salt
string = "fanyideskweb{}{}mmbP%A-r6U3Nw(n]BjuEU"
sign = hashlib.md5(string.format(word, salt).encode()).hexdigest()
print(sign)


class ydspider:
    def __init__(self):
        self.data = {
            'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'ts': ts,
            'bv': '7b07590bbf1761eedb1ff6dbfac3c1f0',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        self.ydstart()

    def ydstart(self):
        headers = {
            'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
            'Connection': 'keep-alive',
            'Content-Length': '246',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1847745080@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=211589491.07177573; JSESSIONID=aaaZR54m0iuMuegMkoOox; ___rl__test__cookies=1596255220215',
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        html = requests.post('http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule', data=self.data, headers=headers)
        print(html.text)


youdao = ydspider()

