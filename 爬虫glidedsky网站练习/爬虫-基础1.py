# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/2 21:32
@file: 爬虫-基础1.py
@desc: 
"""

import requests
from lxml import etree


class TitleOne:
    def __init__(self):
        self.url = 'http://www.glidedsky.com/level/web/crawler-basic-1'
        self.go_crawl()

    def go_crawl(self):
        header = {
            'Cookie': '_ga=GA1.2.1051924338.1596293046; _gid=GA1.2.1111790943.1596293047; __gads=ID=221133d840046023:T=1596293140:S=ALNI_MZL5-P7Qdfcm9nLC9pl96HGFTObpQ; footprints=eyJpdiI6IkZQMCt6Tnh4WTNHXC82MG9pcWo0SFZnPT0iLCJ2YWx1ZSI6IkwrSHNSNDl6aXh3bWNEODdROEd6ZW9jeWExWUhoNlJBNXhVUjNFcmtkQVJRdWxwbGVTTjYybzlPUmVYUU1JaWciLCJtYWMiOiIzYWMyN2U1YWVjMzY5NmMyMjk4M2VkNjVkMjU2NjM3NjM1MmY2YTY1ZDU5N2IwNDFiODBjNmU3M2UwZDEzMDQ3In0%3D; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1596293046,1596374824,1596374882; XSRF-TOKEN=eyJpdiI6IksxQnY1YXhyMUh2TnJXWk44bmRKVWc9PSIsInZhbHVlIjoieSt5U0phVHhIaldcL09jTlFINEhoMW9KUHlSaUlwK1NrU3Q3KzExYkdqc1B4NVZZVm5IN2NhMUlEWjVQQ2QyekQiLCJtYWMiOiJjZWQxNGFhN2ZmMmNkZTBhNDc2OGRiZmQxNTBiMWUyMmU5N2IwMmMzNWYwNTRiMjQ5NmFkN2U2YmZhZjgwNGM3In0%3D; glidedsky_session=eyJpdiI6IjdxTlplNmhFYWJvU1Q0MEVXZXhRU3c9PSIsInZhbHVlIjoiTnJjQ3lMRkV0UFFkTGp0S0JRM2pmT2I2M2VYSTN5c2IxZjZWRHI1MUN2ZHphSk55VnUyRmFjSEZPWGV6WFRFNSIsIm1hYyI6ImUwMjk0OWRlZWYzMGY3Y2U4NmJlY2I2MzRhOTM2NjAyNDFlNGU5M2MwODZlZWZlNzllZDkxZjM3NWU2ZTA0ZDMifQ%3D%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1596376282'
        }
        html = requests.get(self.url, headers=header)
        html = etree.HTML(html.text)
        data = html.xpath('//div[@class="row"]/div/text()')
        number = 0
        for each in data:
            number += int(each)
        print(number)


if __name__ == '__main__':
    TitleOne()

