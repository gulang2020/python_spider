# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import redis
import random
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)
REDIS_KEY = 'fufeiproxy'
import requests

# def get_proxy():
#     proxy_list = r.srandmember(REDIS_KEY)
#     proxy = random.choice(proxy_list)
#     return proxy.decode()
def get_proxy():
    #wuyoudaili
    # proxy = r.srandmember(REDIS_KEY)
    proxy = r.spop(REDIS_KEY)
    return proxy.decode()

def get_api_proxy():
    # wuyoudaoli
    html = requests.get('http://api.ip.data5u.com/dynamic/get.html?order=d0be5adfffe4ebccbfd342d0e845dd4a&random=1&sep=3')
    data = html.text
    c = data.split()
    a = random.choice(c)
    return a


class ShieldipDownloaderMiddleware():

    def process_request(self, request, spider):
        proxy = get_proxy()
        # proxy = get_api_proxy()
        if request.url.startswith("http://"):
            request.meta['proxy'] = "http://" + proxy  # http代理
        elif request.url.startswith("https://"):
            request.meta['proxy'] = "https://" + proxy

        request.cookies = {'_ga': 'GA1.2.1051924338.1596293046',
                           ' _gid': 'GA1.2.1111790943.1596293047', ' __gads': 'ID=221133d840046023:T=1596293140:S=ALNI_MZL5-P7Qdfcm9nLC9pl96HGFTObpQ', ' footprints': 'eyJpdiI6IitDMXhsUFZkMEVXRVhPRHBuVzY5bFE9PSIsInZhbHVlIjoiT3NUT1RxSkVDTERSZmFqY243WmxHY0hZeEc3WmZXQmtYaVd4MWt5Z293bnhteFJzYlhcL0kyRXZBa0ErczFYQkMiLCJtYWMiOiJlOWJhYzFiYjI1MzJmNmYwNDUzYzBlZmY2NTg4MzljZTYxMTAyMWY4YTJiOGVmYTM4YTlkYTQ3MmUwYjgxM2I3In0%3D', ' remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': 'eyJpdiI6IjR6MkRNKzdJTEhxTHlcLzI0TG1rMUlnPT0iLCJ2YWx1ZSI6ImdTNDBQS0pRdVlSWDNcL0Q3RmhneVdLRWErdHJJZUVpa1JodGtXUm9CMzF2elZ2c1FwV0RmQ0lUTkc5NFVjVStEZElcL3VJVW8yN3Z4bWZJSGN5YXAyQTFCUUMrTVRZOGJiYlMyQnYrNkhoVlwvWDVRbGhQOFk0OUZkM3dZQ0tReHdYQXlYYXZad1J0ZHhmSFFma2g0bjRrbG95cFgrV09WaGtvRFltOTVGRXdmcz0iLCJtYWMiOiJhOTU4MGRhNjU1Zjc2MjgyNjBkYzdiNzQwYTc4YjBkOWVhY2Y4YTc1MTA4MjQzNDVjNTljYTA4N2ViN2E0ZmU0In0%3D', ' Hm_lvt_020fbaad6104bcddd1db12d6b78812f6': '1596374824,1596374882,1596410690,1596442509', ' Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6': '1596443963', ' XSRF-TOKEN': 'eyJpdiI6IkV6b1BHVWVpV0x1c2NCOGFCRlJ4MkE9PSIsInZhbHVlIjoidG5aOVBDR1hpQzFYdVwvSDc5Y09INjFJZjNRdHhGWHhWN2dmRVwvdnZSN04ycVwvMlwvOGxhN0tkVXBIaHA3ZXVsc2UiLCJtYWMiOiIyZjcwYTM0ZWU4NDUwN2YzM2U5MWE5ZDBkYjI2ODBkYmE5ODk1NjhhNDE1ZGEyOWM3YzU0ODExNDhjYmNmNmRhIn0%3D', ' glidedsky_session': 'eyJpdiI6ImdsSlRuendHYUcwbUR3VjVicHd2Nmc9PSIsInZhbHVlIjoidmlCWWlFdGpLWHVWMUpRY3V0RmU1d1F0QUhYZHV4d1prS0RrRmswOGpnSUtHbEJoWWhhTEJscGtQMjVHK252RSIsIm1hYyI6IjMwZWMzMGYzZmExYzYwMWNhZmE1ZTg0NDExNjU5MzQ5N2E4ZWMxZWJhNTM3ZDY5NGJiZDI1OGYwNjhkODI4MDQifQ%3D%3D'
                           }

    def process_response(self, request, response, spider):
        if response.status == 403:
            print('进入403失败重连')
            return request
        return response

    def process_exception(self, request, exception, spider):
        return request


    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
