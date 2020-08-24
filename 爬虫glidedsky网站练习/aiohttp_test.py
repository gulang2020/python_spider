# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/4 13:03
@file: aiohttp_test.py
@desc: 
"""

import aiohttp
import requests
import redis_test
from lxml import etree
import aiohttp
import redis
import asyncio

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)
REDIS_KEY = 'jihe_proxy'

def main():