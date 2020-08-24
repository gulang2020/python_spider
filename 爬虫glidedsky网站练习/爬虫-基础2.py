# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/3 7:26
@file: 爬虫-基础2.py
@desc: 
"""

import requests
from lxml import etree
import time

class TitleTwo:
    def __init__(self):
        self.go_crawl()

    def go_crawl(self):
        start_url = 'http://www.glidedsky.com/level/web/crawler-basic-2?page='
        header = {
            'Cookie': '_ga=GA1.2.1051924338.1596293046; _gid=GA1.2.1111790943.1596293047; __gads=ID=221133d840046023:T=1596293140:S=ALNI_MZL5-P7Qdfcm9nLC9pl96HGFTObpQ; footprints=eyJpdiI6IitDMXhsUFZkMEVXRVhPRHBuVzY5bFE9PSIsInZhbHVlIjoiT3NUT1RxSkVDTERSZmFqY243WmxHY0hZeEc3WmZXQmtYaVd4MWt5Z293bnhteFJzYlhcL0kyRXZBa0ErczFYQkMiLCJtYWMiOiJlOWJhYzFiYjI1MzJmNmYwNDUzYzBlZmY2NTg4MzljZTYxMTAyMWY4YTJiOGVmYTM4YTlkYTQ3MmUwYjgxM2I3In0%3D; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1596293046,1596374824,1596374882,1596410690; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjR6MkRNKzdJTEhxTHlcLzI0TG1rMUlnPT0iLCJ2YWx1ZSI6ImdTNDBQS0pRdVlSWDNcL0Q3RmhneVdLRWErdHJJZUVpa1JodGtXUm9CMzF2elZ2c1FwV0RmQ0lUTkc5NFVjVStEZElcL3VJVW8yN3Z4bWZJSGN5YXAyQTFCUUMrTVRZOGJiYlMyQnYrNkhoVlwvWDVRbGhQOFk0OUZkM3dZQ0tReHdYQXlYYXZad1J0ZHhmSFFma2g0bjRrbG95cFgrV09WaGtvRFltOTVGRXdmcz0iLCJtYWMiOiJhOTU4MGRhNjU1Zjc2MjgyNjBkYzdiNzQwYTc4YjBkOWVhY2Y4YTc1MTA4MjQzNDVjNTljYTA4N2ViN2E0ZmU0In0%3D; XSRF-TOKEN=eyJpdiI6ImtkUjBkalwvN3pJRVB3ZVF2VTZZM0tnPT0iLCJ2YWx1ZSI6Ik1OTFp5VWo0WndYVUdtdnVPcDEzdDhVUTRuV2dFQjdCemJsdFJLREJDaGNzVkpnMTJZTHNYck13Z3dDNHhqTkQiLCJtYWMiOiIwODMyZDY0YzBjMjg1MmVlYjVlZDkyMmJhNWVmMjliMTc3NjA0MzMwNWQyNGQ5M2ZmOWI4YThlYTg2YmI2NWFlIn0%3D; glidedsky_session=eyJpdiI6Im05ajVvK2toSURhTFR1TlhMUUkwV1E9PSIsInZhbHVlIjoidXIxSDNFQzQ1VWNUdUltS2ZmZGowdGpWSnVuZGhzd0RiTHlWaUllS1daRWRIcGFBbHlFZ1lCUkh1aENCRDRFdiIsIm1hYyI6ImJmNjQ1ZTkyY2M1YmZhZjg2YTUwYmRlOWQxY2Y1MmU4NDlhMTRhNGY3NTVlY2VmZmUyYWRkNTRhNGIxMzViYWIifQ%3D%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1596410728'
        }
        page = 1000
        number = 0
        for i in range(1, page+1):
            url = start_url + str(i)
            html = requests.get(url, headers=header)
            html_xpath = etree.HTML(html.text)
            data = html_xpath.xpath('//div[@class="row"]/div/text()')
            for each in data:
                number += int(each)
        print(number)


if __name__ == '__main__':
    start = time.time()
    TitleTwo()
    end = time.time()
    time = round(end-start, 2)
    print('time={}seconds'.format(time))

