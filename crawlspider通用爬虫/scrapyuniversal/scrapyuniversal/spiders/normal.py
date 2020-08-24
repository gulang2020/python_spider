import scrapy


class NormalSpider(scrapy.Spider):
    name = 'normal'
    allowed_domains = ['tech.china.com']
    start_urls = ['https://tech.china.com/telphone/']

    def parse(self, response):
        url = response.xpath('//div[@class="pages"]//a[contains(., "下一页")]/@href').extract_first()
        yield scrapy.Request(url, dont_filter=True)

    def test_parse(self, response):
        print(response.url)