# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/3 11:57
@file: redis_test.py
@desc: 
"""
import redis

REDIS_KEY = 'KEYKEY'
MAX_PAGE = 1
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)


def save_redis():
    proxy = [1, 2, 3, 4]
    score = 2
    for each in proxy:
        r.zadd(REDIS_KEY, score, each)


def read_redis_proxy():
    name = 'proxies:universal'
    num = r.zcard(name)

    b = r.zrevrange(name, 0, 256)
    new_b = list(map(lambda x: x.decode(), b))
    return new_b


def read_test():
    name = 'proxies:universal'
    a = r.zrevrange(name, 0, 0)
    print(a)



if __name__ == '__main__':
    # print(read_redis_proxy())
    read_test()