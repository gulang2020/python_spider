import scrapy
from scrapyandredis.items import NewItem
from scrapy_redis.spiders import RedisSpider
'''
cmd中,输入redis-cli，进入后,输入如下
lpush kingnamespider:start_urls http://www.kingname.info/archives/ [value ...]   

'''


class PachongSpider(RedisSpider):
    name = 'kingname'
    redis_key = 'kingnamespider:start_urls'
    allowed_domains = ['kingname.info']
    start_urls = ['http://www.kingname.info/archives/']

    def parse(self, response):
        host = 'http://www.kingname.info/'
        title_link_list = response.xpath('//a[@class="post-title-link"]')

        for each in title_link_list:
            item = NewItem()
            url = host + each.xpath('@href').extract_first()
            title = each.xpath('span[@itemprop="name"]/text()').extract_first()
            item['title'] = title
            item['url'] = url
            yield scrapy.Request(url, callback=self.detail_parse, meta={'item': item})

        next_url = response.xpath('//a[@rel="next"]/@href').extract_first()
        if next_url:
            next_url1 = host + next_url
            yield scrapy.Request(next_url1, callback=self.parse)

    def detail_parse(self, response):
        item = response.meta['item']
        yield item


