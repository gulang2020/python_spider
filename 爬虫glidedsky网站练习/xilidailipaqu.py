# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/3 10:32
@file: xilidailipaqu.py
@desc:
http://www.xiladaili.com/gaoni/爬取代理
"""
import requests
from lxml import etree
import redis
import time

REDIS_KEY = 'proxy-redis-list'
MAX_PAGE = 500
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)


class XiladailiCrawler:
    def __init__(self):
        self.start_url = 'http://www.xiladaili.com/gaoni/'
        self.get_url()

    def get_url(self):
        for i in range(1, MAX_PAGE+1):
            url = self.start_url + str(i)
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
            }

            html = requests.get(url, headers=header)
            time.sleep(2)
            self.detail_url(html)

    # def detail_url(self, resp): # zadd存储
    #     etree_html = etree.HTML(resp.text)
    #     data = etree_html.xpath('//tbody/tr//td[1]/text()')
    #     score = 100
    #     print(data)
    #     for each in data:
    #         r.zadd(REDIS_KEY, score, each)

    def detail_url(self, resp):  # list存储
        etree_html = etree.HTML(resp.text)
        data = etree_html.xpath('//tbody/tr//td[1]/text()')
        print(data)
        for each in data:
            r.lpush(REDIS_KEY, each)


if __name__ == '__main__':
    # XiladailiCrawler()
    start = time.time()
    html = requests.get('http://localhost:5555/random')
    end = time.time()
    print(end-start)
    print(html)

