# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from scrapy.exceptions import DropItem
import random

# class ScrapymanhuaPipeline:
#     def process_item(self, item, spider):
#         return item


class ImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        """
        第一步，从item中爬取url字段（也就是图片链接）并返回
        """
        # print('正在pipelines中，item[do_referer]为', item['do_referer'])
        # print('正在pipelines中，item[url]为', item['url'])
        if item['num'] != 1:
            real_referer = item['do_referer'] + '-P' + str(item['num'])
        else:
            real_referer = item['do_referer']
        do_request = Request(item['url'], headers={'referer': real_referer}, meta={'title': item['title'], 'num': item['num']})  # 把页码和目录名发送
        yield do_request
        # yield Request(item['url'])

    def file_path(self, request, response=None, info=None):
        url = request.url
        title = request.meta['title']
        self.num = request.meta['num']
        name = 'page' + str(self.num)
        path = 'jojo奇妙历险记/' + title.strip() + '/' + name.strip() + '.jpg'

        file_name = url.split('key')[-1]  # split用于分割字段，取url最后一段作为名字

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
        print('#########################下载成功#################################')
        return item









