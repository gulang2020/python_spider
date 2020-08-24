# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/10 20:13
@file: test2.py
@desc: 
"""

import os
import json

import pymysql

class test_class:
    def __init__(self):
        self.abc = 2

    def next(self):
        self.hello = 2

    def pri(self):
        print(self.hello)
hi = test_class()
hi.pri