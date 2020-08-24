# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy import Item
from scrapy import Field

#
# class ScrapymanhuaItem(Item):
#     name = Field()
#     url = Field()

class ScrapymanhuaItem(Item):
    title = Field()
    name = Field()
    url = Field()
    num = Field()  # 页号
    do_referer = Field()
