# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/4 20:18
@file: 付费代理存入redis.py
@desc: 
"""
import redis
import requests
import time
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

REDIS_KEY = 'fufeiproxy'
# wuyoudaoli
for each in range(1, 10011111):
    time.sleep(4)
    html = requests.get('http://api.ip.data5u.com/dynamic/get.html?order=d0be5adfffe4ebccbfd342d0e845dd4a&random=1&sep=3')
    data = html.text
    c = data.split()
    print(c)
    if r.scard(REDIS_KEY) > 30:
        for i in range(1, r.scard(REDIS_KEY)-1):
            r.spop(REDIS_KEY)

    for each1 in c:
        r.sadd(REDIS_KEY, each1)