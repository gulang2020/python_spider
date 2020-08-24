# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/4 14:45
@file: some_test.py
@desc: 
"""

import redis
import random
import requests
from lxml import etree

html = requests.get('http://api.ip.data5u.com/dynamic/get.html?order=d0be5adfffe4ebccbfd342d0e845dd4a&random=1&sep=3')
data = html.text
c = data.split()
print(c)

a = random.choice(c)
print(a)
