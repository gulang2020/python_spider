# encoding: utf-8
# https://www.ciweimao.com/chapter/105757872
"""
@author: 
@contact: 
@time: 2020/8/16 20:30
@file: ciweimao.py
@desc: 
"""
import json
import requests
import execjs
import os

os.environ["EXECJS_RUNTIME"] = "PhantomJS"
node = execjs.get()
with open('do_js.js') as f:
    res = f.read()

js = node.compile(res)
b = js.call('start')
print('js.b=', b)

header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '20',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'UM_distinctid=1737c23b8b78d1-0e7783fb2a36e5-b7a1334-1fa400-1737c23b8b892e; Hm_lvt_1dbadbc80ffab52435c688db7b756e3a=1595515583,1597578525; CNZZDATA1276028418=84608687-1595512578-https%253A%252F%252Fwww.baidu.com%252F%7C1597574869; Hm_lpvt_1dbadbc80ffab52435c688db7b756e3a=1597580314; ci_session=elj2ooncs88dt6gsrj6v4tennq8asd6m; readPage_visits=13',
    'Host': 'www.ciweimao.com',
    'Origin': 'https://www.ciweimao.com',
    'Referer': 'https://www.ciweimao.com/chapter/105757872',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
header2 = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '48',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'UM_distinctid=1737c23b8b78d1-0e7783fb2a36e5-b7a1334-1fa400-1737c23b8b892e; Hm_lvt_1dbadbc80ffab52435c688db7b756e3a=1595515583,1597578525; CNZZDATA1276028418=84608687-1595512578-https%253A%252F%252Fwww.baidu.com%252F%7C1597574869; Hm_lpvt_1dbadbc80ffab52435c688db7b756e3a=1597580314; ci_session=elj2ooncs88dt6gsrj6v4tennq8asd6m; readPage_visits=13',
    'Host': 'www.ciweimao.com',
    'Origin': 'https://www.ciweimao.com',
    'Referer': 'https://www.ciweimao.com/chapter/105757872',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
form_data = {
    'chapter_id': '105757872',
}
url = 'https://www.ciweimao.com/chapter/ajax_get_session_code'
resp = requests.post(url, headers=header, data=form_data)
print(resp)
print(resp.text)

a = json.loads(resp.text)

url1 = 'https://www.ciweimao.com/chapter/get_book_chapter_detail_info'
content_data = {
    'chapter_id': '105757872',
    'chapter_access_key': a['chapter_access_key'],
}
print(content_data)
resp1 = requests.post(url1, headers=header, data=content_data)
print(resp1)
print(resp1.text)
