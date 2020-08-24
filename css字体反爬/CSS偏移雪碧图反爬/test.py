# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/10 10:23
@file: test.py
@desc: 
"""
import requests
import re
from lxml import etree
from PIL import Image
import pytesseract
import time
import matplotlib.pyplot as plt



def test(file_name):
    img = Image.open(file_name)
    # plt.figure("dog")
    # plt.imshow(img)
    # plt.show()
    # x = 1
    # width = 1000 * x
    # height = 300 * x
    # img = img.resize((width, height), Image.ANTIALIAS)
    # img = img.point(lambda x :255 if x > 129 else 0)
    # img = img.convert('L')
    plt.imshow(img)
    plt.show()

    nums = pytesseract.image_to_string(img)
    if not nums:
        print('不存在')
    print(nums)


test('1.png')
print('--------------------------------------')
# test('0f2d52da9106e522530305f1a1fa0788.png')
# print('-=----------------------------------')
# test('9aef59e0b28bf1225780d84f37520891.png')
