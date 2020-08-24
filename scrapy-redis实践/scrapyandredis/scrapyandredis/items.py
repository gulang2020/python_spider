# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewItem(scrapy.Item):
    collection = 'kingname.info'
    title = scrapy.Field()  # 题目
    url = scrapy.Field()  # 链接
    post_time = scrapy.Field()  # 发布时间
    category = scrapy.Field()  # 分类
    detail = scrapy.Field()  # 正文HTML格式


