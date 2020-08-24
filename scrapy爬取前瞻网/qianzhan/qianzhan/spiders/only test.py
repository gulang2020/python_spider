# import requests
# # nian=2020&jidu=%E4%B8%80%E5%AD%A3%E6%8A%A5&zoom=1&trade=&sort=&where=&page=1
# data = {'nian': '2020', 'jidu': '一季报', 'zoom': '1', 'trade': '', 'sort': '', 'where': '', 'page': '1'}
#
# url = 'https://stock.qianzhan.com/report/result/hs_zichan'
#
# # headers = {
# #     'accept': 'text/html, */*; q=0.01',
# #     'accept-encoding': 'gzip, deflate, br',
# #     'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
# #     'content-length': '76',
# #     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
# #     'cookie': 'qznewsite.uid=zu4y5sioq2xjvsugmcnrlg45; Hm_lvt_044fec3d5895611425b9021698c201b1=1594865548,1594960277,1594984067,1595064363; Hm_lvt_86780bd5c039f606162c443afad3a227=1595069923; Hm_lpvt_86780bd5c039f606162c443afad3a227=1595069923; Hm_lpvt_044fec3d5895611425b9021698c201b1=1595071829',
# #     'origin': 'https://stock.qianzhan.com',
# #     'referer': 'https://stock.qianzhan.com/report/table_hs_zichan.html',
# #     'sec-fetch-dest': 'empty',
# #     'sec-fetch-mode': 'cors',
# #     'sec-fetch-site': 'same-origin',
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
# #     'x-requested-with': 'XMLHttpRequest'
# # }
# print(data)
# html = requests.post(url, data=data)
# print(html.text)
#
#
