# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/4 11:04
@file: 66ipdaili.py
@desc: 
"""
import requests
from pyquery import PyQuery as pq
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)


def parse(html):
    """
    parse html file to get proxies
    :return:
    """
    doc = pq(html.text)
    trs = doc('.containerbox table tr:gt(0)').items()
    for tr in trs:
        host = tr.find('td:nth-child(1)').text()
        port = int(tr.find('td:nth-child(2)').text())
        proxy = str(host) + ':' + str(port)
        print(proxy)
        r.sadd('jihe_proxy', proxy)


BASE_URL = 'http://www.66ip.cn/{page}.html'
MAX_PAGE = 4000

urls = [BASE_URL.format(page=page) for page in range(1, MAX_PAGE + 1)]
for url in urls:
    parse(requests.get(url))

