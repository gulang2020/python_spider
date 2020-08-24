import scrapy
import re
import requests
import muggle_ocr
import os
import json
from scrapyziroom.items import ScrapyziroomItem
PAGE = 49


def download_photo(photo_name, photo_url):
    resp = requests.get(photo_url)
    file = 'numbers/' + photo_name
    if not os.path.exists(file):
        with open(file, 'wb') as f:
            f.write(resp.content)


def parse_photo(photo_name):
    '''返回偏移量对照表'''
    json_file = 'json_dict/' + photo_name + '.json'
    if os.path.exists(json_file):
        print('开始读取字典')
        with open(json_file, 'r') as f:
            return json.load(f)
    # 初始化
    sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.OCR)
    file = 'numbers/' + photo_name
    with open(file, "rb") as f:
        b = f.read()
        text = sdk.predict(image_bytes=b)
        list_nums = []
        for each in text:
            list_nums.append(each)
    # 生成偏移量与真实价格的对照表
    html_offsets = []
    for i in range(0, 10+1):
        b = i * 21.4
        # b = format(b, '.1f')  # 保留小数一位
        b = int(b)
        html_offsets.append(b)
    #  组合两个列表成字典
    real_nums = {}
    for k, v in zip(html_offsets, list_nums):
        real_nums[k] = v
    with open(json_file, 'w') as f:
        print('写入字典')
        json.dump(real_nums, f)
    return real_nums


def do_price(real_nums, price_link):
    '''
    :param real_nums: 偏移对照字典
    :param price_link: 包含偏移量的列表
    :return: 例如1950这样的string
    '''
    price_list = []
    price = ''
    for each in price_link:
        b = each.re('background-position: -(.*)px')[0]
        b = int(float(b))
        price = price + real_nums[str(b)]
    price = price + '/月'
    return price

class ZiroomSpider(scrapy.Spider):
    name = 'ziroom'
    allowed_domains = ['ziroom.com']
    base_url = 'http://gz.ziroom.com/z/'
    start_urls = []
    for i in range(1, PAGE+1):
        url = base_url + 'p' + str(i) + '/'
        start_urls.append(url)

    def parse(self, response):
        html = response.text
        # 提取图片链接
        photo_url = 'http:' + re.findall('<span class="num" style="background-image: url\((.*?)\)', html)[0]
        photo_name = photo_url.split('/')[-1]
        # 下载图片
        download_photo(photo_name, photo_url)
        #  解析图片,返回偏移量字典
        real_nums = parse_photo(photo_name)
        # xpath 处理开始
        all_data = response.xpath('//div[@class="item"]')  # 先抓大在抓小
        for one_data in all_data:
            item = ScrapyziroomItem()
            # 先获取价值
            price_link = one_data.xpath('.//div[@class="price "]/span[contains(@class, "num")]/@style')
            item['price'] = do_price(real_nums, price_link)
            #
            item['pic'] = one_data.xpath('.//div[@class="pic-box"]/a/img/@data-original').extract_first()  # 图片链接
            item['title'] = one_data.xpath('.//div[@class="info-box"]/h5/a/text()').extract_first()  # 标题
            # item['tag']
            tag = one_data.xpath('.//div[@class="info-box"]/div[@class="tag"]//text()').extract()  # 特点
            tag = list(map(lambda x: x.strip(), tag))
            item['tag'] = [i for i in tag if i != '']
            #
            item['link'] = one_data.xpath('.//div[@class="pic-box"]/a/@href').extract_first()  # 链接
            yield item
