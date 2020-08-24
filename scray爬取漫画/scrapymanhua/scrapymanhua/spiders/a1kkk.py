import scrapy
from scrapy import selector
from scrapymanhua.items import ScrapymanhuaItem
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pyquery import PyQuery as pq

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])



class A1kkkSpider(scrapy.Spider):
    name = '1kkk'
    allowed_domains = ['dm5.com']
    # start_urls = ['http://www.1kkk.com/manhua539/']
    # start_urls = ['http://www.1kkk.com/manhua51618/']
    start_urls = ['http://www.dm5.com/manhua-jojo-qimiaomaoxian/']

    def __init__(self):  # 为selenium使用
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })
        super().__init__()

    def close(self, spider):
        self.driver.quit()

    def parse(self, response):
        pass
        base_url = 'http://www.dm5.com'
        # print('开始解析目录')
        # catalog = response.selector.xpath('//ul[@id="detail-list-select-3"]//li/a/@href').extract()
        # catalog = response.selector.xpath('//ul[@id="detail-list-select-3"]//li')  # 本漫画网页有正文和翻页
        catalog = response.selector.xpath('//ul[@id="detail-list-select-3"]//li')
        for each in catalog:
            link = each.xpath('./a/@href').extract_first()
            title = each.xpath('./a/text()').extract_first()  # 目录下的章节名
            url = base_url + link
            # print(name)
            # print(url)
            yield scrapy.Request(url, callback=self.manhua_one_parse, meta={'title': title})

    def manhua_one_parse(self, response):
        # print('##########################manhua_one_parse开始了##################################')
        """
        获得了最大页数, 章节名通过meta传递过来
        考虑在这一页建立文件夹
        :param response:
        :return:
        """
        title = response.meta['title']
        max_label = response.selector.xpath('//*[@id="chapterpager"]/a[last()]/text()').extract_first()

        num = int(max_label)
        for each in range(1, num+1):  # 获取一章漫画的全部下载网页，之后还要获取网页中的图片链接
            num = each  # 页数
            urlone = re.findall('(.*)/', response.url)

            url_Two = re.findall('http://www.dm5.com/(.*)', response.url)[0]
            url_start = 'http://www.dm5.com/'
            do_referer = url_start + url_Two
            # do_referer = re.findall('(.*)/', response.url)

            urlnumber = '-P' + str(each) + '/#ipg' + str(each)
            url = urlone[0] + urlnumber
            # print('do_referer值为', do_referer)
            # print('url值为', url)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
            }
            yield scrapy.Request(url, headers=headers, dont_filter=True, callback=self.manhua_two_parse, meta={'title': title, 'num': num, 'do_referer': do_referer})
            # yield scrapy.Request(url, callback=self.manhua_two_parse,
            #                      meta={'title': title, 'num': num, 'do_referer': do_referer})

    def manhua_two_parse(self, response):

        # print('传递过来的最终链接', response.url)
        tail = '#ipg' + str(response.meta['num'])
        page_link = response.url + tail
        # print(page_link)
        pass
        """
        这里获得了每一页的图片，然而图片被js加载
        :param response:
        :return:
        """
        image = response.selector.xpath('//p[id="imgloading"]/p/img/@src').extract()

        wait = WebDriverWait(self.driver, 2)  # 为selenium使用
        # self.driver.get(response.url)
        self.driver.get(page_link)
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#cp_image'))
        )
        html = self.driver.page_source
        doc = pq(html)
        a = doc('#cp_image')

        item = ScrapymanhuaItem()
        item['name'] = response.url
        item['url'] = a.attr('src')  # selenium使用
        item['title'] = response.meta['title']  # 目录章节名
        # item['url'] = image
        item['num'] = response.meta['num']  # 每一话的页码
        item['do_referer'] = response.meta['do_referer']
        yield item
