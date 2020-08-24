import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversal.items import NewItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose


class NewsLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ChinaLoader(NewsLoader):
    text_out = Compose(Join(), lambda s: s.strip())
    source_out = Compose(Join(), lambda s: s.strip())


class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['https://tech.china.com/articles/']
    # start_urls = ['https://tech.china.com/article/20200716/20200716560249.html']
    rules = (
        Rule(LinkExtractor(allow='article/.*.html',
                           restrict_xpaths='//div[@class="item-con-inner"]//h3[@class="tit"]'), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pages"]//a[contains(., "下一页")]')),
    )

    def make_requests_from_url(self, url):
        return scrapy.Request(url, dont_filter=True)

    # def parse(self, response):
        # item = NewItem()
        # item['title'] = response.xpath('//*[@id="chan_newsTitle"]/text()').extract_first()
        # item['url'] = response.url
        # item['text'] = ''.join(response.xpath('//div[@id="chan_newsDetail"]//text()').extract()).strip()
        # # item['datetime'] = response.xpath('//div[@id="js-article-title"]//span[@class="time"]/text()').extract_first()
        # item['datetime'] = response.xpath('//div[@id="js-article-title"]//span[@class="time"]/text()').re_first('(\d+-\d+-\d+\s\d+:\d+:\d+)')
        # item['source'] = response.xpath('//div[@id="js-article-title"]//span[@class="source"]/text()').re_first('来源：(.*)').strip()
        # item['website'] = '中华网'
        # yield item

    def parse_item(self, response):

        loader = ChinaLoader(item=NewItem(), response=response)
        loader.add_xpath('title', '//*[@id="chan_newsTitle"]/text()')
        loader.add_value('url', response.url)
        # loader.add_xpath('text', '//div[@id="chan_newsDetail"]//text()')
        loader.add_xpath('datetime', '//div[@id="js-article-title"]//span[@class="time"]/text()', re='(\d+-\d+-\d+\s\d+:\d+:\d+)')
        loader.add_xpath('source', '//div[@id="js-article-title"]//span[@class="source"]/text()', re='来源：(.*)')
        loader.add_value('website', '中华网')
        yield loader.load_item()

