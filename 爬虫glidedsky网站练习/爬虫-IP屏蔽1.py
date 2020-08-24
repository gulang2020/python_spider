# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/3 8:54
@file: 爬虫-IP屏蔽1.py
@desc: 
"""

import requests
import redis_test
from lxml import etree
import aiohttp
import redis
import asyncio

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)
REDIS_KEY = 'jihe_proxy'


class TitleThree:
    def __init__(self):
        self.number = 0
        self.go_crawl()
        print('self.number = ', self.number)

    def go_crawl(self):
        url = 'http://www.glidedsky.com/level/web/crawler-ip-block-1'
        tasks = []
        for i in range(1, 3):
            full_url = url + '?page=' + str(i)
            c = self.do_request(full_url)
            # 生成任务
            task = asyncio.ensure_future(c)
            tasks.append(task)
            loop = asyncio.get_event_loop()
            loop.run_until_complete(asyncio.wait(tasks))

    async def fetch(self, session, url):
        header = {
            'Cookie': '_ga=GA1.2.1051924338.1596293046; _gid=GA1.2.1111790943.1596293047; __gads=ID=221133d840046023:T=1596293140:S=ALNI_MZL5-P7Qdfcm9nLC9pl96HGFTObpQ; footprints=eyJpdiI6IitDMXhsUFZkMEVXRVhPRHBuVzY5bFE9PSIsInZhbHVlIjoiT3NUT1RxSkVDTERSZmFqY243WmxHY0hZeEc3WmZXQmtYaVd4MWt5Z293bnhteFJzYlhcL0kyRXZBa0ErczFYQkMiLCJtYWMiOiJlOWJhYzFiYjI1MzJmNmYwNDUzYzBlZmY2NTg4MzljZTYxMTAyMWY4YTJiOGVmYTM4YTlkYTQ3MmUwYjgxM2I3In0%3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjR6MkRNKzdJTEhxTHlcLzI0TG1rMUlnPT0iLCJ2YWx1ZSI6ImdTNDBQS0pRdVlSWDNcL0Q3RmhneVdLRWErdHJJZUVpa1JodGtXUm9CMzF2elZ2c1FwV0RmQ0lUTkc5NFVjVStEZElcL3VJVW8yN3Z4bWZJSGN5YXAyQTFCUUMrTVRZOGJiYlMyQnYrNkhoVlwvWDVRbGhQOFk0OUZkM3dZQ0tReHdYQXlYYXZad1J0ZHhmSFFma2g0bjRrbG95cFgrV09WaGtvRFltOTVGRXdmcz0iLCJtYWMiOiJhOTU4MGRhNjU1Zjc2MjgyNjBkYzdiNzQwYTc4YjBkOWVhY2Y4YTc1MTA4MjQzNDVjNTljYTA4N2ViN2E0ZmU0In0%3D; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1596374824,1596374882,1596410690,1596442509; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1596443963; XSRF-TOKEN=eyJpdiI6IkV6b1BHVWVpV0x1c2NCOGFCRlJ4MkE9PSIsInZhbHVlIjoidG5aOVBDR1hpQzFYdVwvSDc5Y09INjFJZjNRdHhGWHhWN2dmRVwvdnZSN04ycVwvMlwvOGxhN0tkVXBIaHA3ZXVsc2UiLCJtYWMiOiIyZjcwYTM0ZWU4NDUwN2YzM2U5MWE5ZDBkYjI2ODBkYmE5ODk1NjhhNDE1ZGEyOWM3YzU0ODExNDhjYmNmNmRhIn0%3D; glidedsky_session=eyJpdiI6ImdsSlRuendHYUcwbUR3VjVicHd2Nmc9PSIsInZhbHVlIjoidmlCWWlFdGpLWHVWMUpRY3V0RmU1d1F0QUhYZHV4d1prS0RrRmswOGpnSUtHbEJoWWhhTEJscGtQMjVHK252RSIsIm1hYyI6IjMwZWMzMGYzZmExYzYwMWNhZmE1ZTg0NDExNjU5MzQ5N2E4ZWMxZWJhNTM3ZDY5NGJiZDI1OGYwNjhkODI4MDQifQ%3D%3D'
        }
        cookies = '_ga=GA1.2.1051924338.1596293046; _gid=GA1.2.1111790943.1596293047; __gads=ID=221133d840046023:T=1596293140:S=ALNI_MZL5-P7Qdfcm9nLC9pl96HGFTObpQ; footprints=eyJpdiI6IitDMXhsUFZkMEVXRVhPRHBuVzY5bFE9PSIsInZhbHVlIjoiT3NUT1RxSkVDTERSZmFqY243WmxHY0hZeEc3WmZXQmtYaVd4MWt5Z293bnhteFJzYlhcL0kyRXZBa0ErczFYQkMiLCJtYWMiOiJlOWJhYzFiYjI1MzJmNmYwNDUzYzBlZmY2NTg4MzljZTYxMTAyMWY4YTJiOGVmYTM4YTlkYTQ3MmUwYjgxM2I3In0%3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjR6MkRNKzdJTEhxTHlcLzI0TG1rMUlnPT0iLCJ2YWx1ZSI6ImdTNDBQS0pRdVlSWDNcL0Q3RmhneVdLRWErdHJJZUVpa1JodGtXUm9CMzF2elZ2c1FwV0RmQ0lUTkc5NFVjVStEZElcL3VJVW8yN3Z4bWZJSGN5YXAyQTFCUUMrTVRZOGJiYlMyQnYrNkhoVlwvWDVRbGhQOFk0OUZkM3dZQ0tReHdYQXlYYXZad1J0ZHhmSFFma2g0bjRrbG95cFgrV09WaGtvRFltOTVGRXdmcz0iLCJtYWMiOiJhOTU4MGRhNjU1Zjc2MjgyNjBkYzdiNzQwYTc4YjBkOWVhY2Y4YTc1MTA4MjQzNDVjNTljYTA4N2ViN2E0ZmU0In0%3D; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1596374824,1596374882,1596410690,1596442509; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1596443963; XSRF-TOKEN=eyJpdiI6IkV6b1BHVWVpV0x1c2NCOGFCRlJ4MkE9PSIsInZhbHVlIjoidG5aOVBDR1hpQzFYdVwvSDc5Y09INjFJZjNRdHhGWHhWN2dmRVwvdnZSN04ycVwvMlwvOGxhN0tkVXBIaHA3ZXVsc2UiLCJtYWMiOiIyZjcwYTM0ZWU4NDUwN2YzM2U5MWE5ZDBkYjI2ODBkYmE5ODk1NjhhNDE1ZGEyOWM3YzU0ODExNDhjYmNmNmRhIn0%3D; glidedsky_session=eyJpdiI6ImdsSlRuendHYUcwbUR3VjVicHd2Nmc9PSIsInZhbHVlIjoidmlCWWlFdGpLWHVWMUpRY3V0RmU1d1F0QUhYZHV4d1prS0RrRmswOGpnSUtHbEJoWWhhTEJscGtQMjVHK252RSIsIm1hYyI6IjMwZWMzMGYzZmExYzYwMWNhZmE1ZTg0NDExNjU5MzQ5N2E4ZWMxZWJhNTM3ZDY5NGJiZDI1OGYwNjhkODI4MDQifQ%3D%3D'
        proxy = r.spop(REDIS_KEY)
        proxy = proxy.decode()
        proxies = 'http//' + proxy
        async with session.get(url, proxy=proxies, cookies=cookies,) as response:
            return await response

    async def do_request(self, url):
        async with aiohttp.ClientSession() as session:
            response = await self.fetch(session, url)
            print('判断点')
            html = response.text
            html_xpath = etree.HTML(html)
            data = html_xpath.xpath('//div[@class="row"]/div/text()')
            for each in data:
                self.number += int(each)



TitleThree()


