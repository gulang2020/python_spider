# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/10 14:36
@file: test1.py
@desc: 
"""

import muggle_ocr

import time

# 导入包
import muggle_ocr

# 初始化；model_type 包含了 ModelType.OCR/ModelType.Captcha 两种
sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.OCR)

# ModelType.Captcha 可识别光学印刷文本


def test_file(file):
    with open(file, "rb") as f:
        b = f.read()
        text = sdk.predict(image_bytes=b)
        list_num = []
        for i in text:
            list_num.append(i)
        print(list_num)
test_file('{}.png'.format(1))

# ModelType.Captcha 可识别4-6位验证码
# sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
# with open(r"2.jpg", "rb") as f:
#     b = f.read()
# for i in range(5):
#     st = time.time()
#     text = sdk.predict(image_bytes=b)
#     print(text, time.time() - st)

# for i in range(1, 7+1):
#     print('kaishi ', i)
#     test_file('{}.png'.format(i))