import scrapy
from qianzhan.items import NewItem
import csv
import re
from scrapy_redis.spiders import RedisSpider

def double_list_remove(double_list):
    '''
    删除二维列表中所有的空元素
    '''
    number = 0
    for i in range(len(double_list)):
        number = 0
        for j in range(len(double_list[i])):
            if double_list[i][j] == '':
                number += 1
        for num in range(0, number):
            double_list[i].remove('')
    return double_list


def xing_remove(str_data):
    '''
    删除字符串中的*，
    因为制造目录的时候，文件夹名字中不能带*
    '''
    for ch in str_data:
        if ch == '*':
            str_data = str_data.replace('*', '')
    return str_data


class PachongSpider(scrapy.Spider):
    name = 'pachong'
    allowed_domains = ['stock.qianzhan.com']
    def start_requests(self):
        url = 'https://stock.qianzhan.com/report/result/hs_zichan'
        cookies = {
            'qznewsite.uid': 'zu4y5sioq2xjvsugmcnrlg45',
            'Hm_lvt_86780bd5c039f606162c443afad3a227': '1595069923',
            'Hm_lvt_044fec3d5895611425b9021698c201b1': '1594984067, 1595064363, 1595111937, 1595120533',
            'qz.newsite': '458FBBB14D97EA5E0580710114211322ED77EA1867A743E5493C83506B2127CF64A0EC0E50C8C71532427AAF0E5D432FB4116D9D8531E4DDE67C5ED8F711D8A19691AC21065134F9174429D9B33C24F04B52623F48E789F6E3F8575A0675DC69502A887B455A9B322F06DE627195E5192D103F156E37DD73288778D211F42EB997E0572F',
            'user.email': '18808966438',
            'Hm_lpvt_044fec3d5895611425b9021698c201b1': '1595134397'
        }
        page_max = 79
        data = {'nian': '2020', 'jidu': '一季报', 'zoom': '1', 'trade': '', 'sort': '', 'where': '', 'page': ''}
        for page in range(1, page_max+1):
            data['page'] = str(page)
            yield scrapy.FormRequest(url=url , callback=self.parse, formdata=data, cookies=cookies)


    def parse(self, response):
        '''
        获取所有公司url，将其URL发送给下一个函数data_parse
        :param response:
        :return:
        '''
        host = 'https://stock.qianzhan.com'
        url_link = response.xpath('//tbody/tr//td[2]/a/@href').extract()
        for link in url_link:
            url = host + link
            yield scrapy.Request(url=url, callback=self.data_parse, dont_filter=True)

    def data_parse(self, response):
        item = NewItem()
        ns_name = response.xpath('//*[@id="div_stock_info"]/b[1]/text()').extract_first()
        ns_id = response.xpath('//*[@id="div_stock_info"]/b[1]/span/text()').extract_first()
        # ns_id = re.findall('（(.*)）', ns_id)[0]  # （000004.SZ） 将括号去掉
        ns_name = xing_remove(ns_name)
        item['ns_name'] = ns_name
        item['ns_id'] = ns_id

        host = 'https://stock.qianzhan.com'
        #  资产负债表
        half_url = response.xpath('//ul[@id="ul_left_menus"]/li[12]/a/@href').extract_first()  # 爬取资产负债表
        table_url = host + half_url  # 拼接url
        table_name = response.xpath('//ul[@id="ul_left_menus"]/li[12]/a/text()').extract_first()
        yield scrapy.Request(url=table_url, callback=self.detail_parse, meta={'table_name': table_name, 'item': item})
        #  利润表
        half_url = response.xpath('//ul[@id="ul_left_menus"]/li[13]/a/@href').extract_first()  # 爬取利润表
        table_url = host + half_url  # 拼接url
        table_name = response.xpath('//ul[@id="ul_left_menus"]/li[13]/a/text()').extract_first()
        yield scrapy.Request(url=table_url, callback=self.detail_parse, meta={'table_name': table_name, 'item': item})
        #  现金流量表
        half_url = response.xpath('//ul[@id="ul_left_menus"]/li[14]/a/@href').extract_first()  # 爬取利润表
        table_url = host + half_url  # 拼接url
        table_name = response.xpath('//ul[@id="ul_left_menus"]/li[14]/a/text()').extract_first()
        yield scrapy.Request(url=table_url, callback=self.detail_parse, meta={'table_name': table_name, 'item': item})

    def detail_parse(self, response):
        all_list = []  # 这里用二维列表实现表格
        first_list = response.xpath('//thead/tr/th/a/text()').extract()  # 拿到表的第一行
        first_list.insert(0, '-')
        all_list.append(first_list)
        #  second_list 构造第一行下面的表格
        second_list = response.xpath('//table[@id="tblBody1"]//tbody/tr')
        for each in second_list:
            list_data = each.xpath('td//text()').extract()
            list_data = list(map(str.strip, list_data))  # map 将strip传递到list里的每一个函数,返回一个迭代器,用list()转为列表
            all_list.append(list_data)
        all_list = double_list_remove(all_list)
        item = response.meta['item']
        item['table_name'] = response.meta['table_name']  # 表格名 (例如利润表)
        item['table_data'] = all_list  # 表格数据
        yield item


