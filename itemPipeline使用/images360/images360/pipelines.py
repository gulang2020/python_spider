# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URL'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        print('开始process_item')
        name = item.collection
        self.db[name].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()

class ImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        url = request.url
        meinv = '美女                        '
        title = request.meta['title']
        file_name = url.split('/')[-1]  # split用于分割字段，取url最后一段作为名字
        # path = 'full/' + meinv + '/' + title + '.jpg'
        path = 'jojo奇妙历险记/' + meinv.strip() + '/' + title.strip() + '.jpg'
        # return file_name
        return path

    def item_completed(self, results, item, info):
        """
        :param results:下载的结果(成功或者失败) ，对应的是item，results是一个列表形式
        :param item:
        :param info:
        :return:
        关于[x['path'] for ok, x in results if ok ] 可以看https://blog.csdn.net/u014033518/article/details/85250388
        """
        print('检查图片是否存在')
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:  # 如果没图片，抛出异常，raise后面的不执行
            raise DropItem('Image download failed')
        return item

    def get_media_requests(self, item, info):
        """
        第一步，从item中爬取url字段（也就是图片链接）并返回
        """
        yield Request(item['url'], meta={'title': item['title']})