# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/9 20:13
@file: css偏移发哪怕.py
@desc:
@目标网站： http://gz.ziroom.com/z/
@本例只爬取price
"""
import requests
import re
from lxml import etree
import muggle_ocr


class ZiroomSpdier:
    def __init__(self):
        self.html_offsets = []
        self.real_nums = {}
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        }

        base_url = 'http://gz.ziroom.com/z/'
        for i in range(1, 2):
            url = base_url + 'p' + str(i) + '/'
            self.get_html(url)

    def get_html(self, url):
        resp = requests.get(url, headers=self.header)
        html = resp.text
        xp_html = etree.HTML(html)
        # 提取图片链接
        photo_url = 'http:' + re.findall('<span class="num" style="background-image: url\((.*?)\)', html)[0]
        photo_name = photo_url.split('/')[-1]
        # 下载图片
        self.download_photo(photo_name, photo_url)
        # 解析图片
        self.parse_photo(photo_name)
        # xpath
        all_data = xp_html.xpath('//div[@class="item"]')
        for one_data in all_data:
            # result = etree.tostring(one_data, encoding='utf-8')
            # print(result)
            price = one_data.xpath('.//div[@class="price "]/span[contains(@class, "num")]/@style')
            price_list = []
            string = ''
            for each in price:
                comp = re.compile('background-position: -(.*)px')
                b = re.findall(comp, each)[0]
                b = int(float(b))
                price_list.append(self.real_nums[b])
                string = string + self.real_nums[b]
            print(price_list)
            print(string)

    def download_photo(self, photo_name, photo_url):
        resp = requests.get(photo_url, headers=self.header)
        with open(photo_name, 'wb') as f:
            print('photo_name写入=', photo_name)
            f.write(resp.content)

    def parse_photo(self, photo_name):
        # 初始化
        sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.OCR)
        with open(photo_name, "rb") as f:
            b = f.read()
            text = sdk.predict(image_bytes=b)
            list_nums = []
            for each in text:
                list_nums.append(each)
        # 生成偏移量与真实价格的对照表
        for i in range(0, 10+1):
            b = i * 21.4
            # b = format(b, '.1f')  # 保留小数一位
            b = int(b)
            self.html_offsets.append(b)
        #  组合两个列表成字典
        for k, v in zip(self.html_offsets, list_nums):
            self.real_nums[k] = v

    def get_price(self, html_offsets):
        pass


if __name__ == '__main__':
    ZiroomSpdier()

