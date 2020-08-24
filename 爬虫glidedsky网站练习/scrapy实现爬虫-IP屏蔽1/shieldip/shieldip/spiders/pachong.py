import scrapy
from shieldip.items import ShieldipItem

nihao = 0


class PachongSpider(scrapy.Spider):
    name = 'pachong'
    allowed_domains = ['www.glidedsky.com/']

    def start_requests(self):
        base_url = ('http://www.glidedsky.com/level/web/crawler-ip-block-1')
        # base_url = ('http://www.glidedsky.com/level/web/crawler-basic-2')
        for i in range(1, 1+1000):
            full_url = base_url + '?page=' + str(i)
            yield scrapy.Request(full_url, dont_filter=True)

    def parse(self, response):
        data = response.xpath('//div[@class="row"]/div/text()').extract()
        number = 0
        for each in data:
            number += int(each)
        global nihao
        nihao += number
        print('nihao=', nihao)
        # 答案2874065

