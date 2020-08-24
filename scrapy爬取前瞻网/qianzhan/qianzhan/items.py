# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class NewItem(Item):


    def __repr__(self):
        '''
        魔法方法 改变terminal里的item显示的数据
        :return:
        '''
        return 'saved'

    s_number = Field()  # 序号
    ns_id = Field()  # 证券代码
    ns_name = Field()  # 证券名称
    table_name = Field()  # 表格名
    table_data = Field()  # 表的数据


