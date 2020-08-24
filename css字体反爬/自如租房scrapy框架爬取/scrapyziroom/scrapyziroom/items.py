# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy import Item, Field


class ScrapyziroomItem(Item):
    collection = table = 'collection_table_ziroom'
    price = Field()  # 价格
    pic = Field()  # 图片链接
    title = Field()  # 标题
    tag = Field()  # 特点
    link = Field()  # 链接
