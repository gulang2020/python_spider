# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import os


class csvPipeline:
    def process_item(self, item, spider):
        ns_id = item['ns_id']  # 证券代码
        ns_name = item['ns_name']  # 证券名称
        table_name = item['table_name']  # 表格名
        all_name = ns_id.strip() + ns_name.strip()
        file_name = 'E:\\爬虫实战项目\\scrapy爬取前瞻网\\qianzhan\\qianzhan\\前瞻网数据库csv信息' + '\\' + all_name
        try:
            os.mkdir(file_name)
        except FileExistsError:
            print('文件已存在')
        data_name = os.path.join(file_name, table_name)
        data_name = data_name + '.csv'
        print(data_name)
        with open(data_name, 'w', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(item['table_data'])
        return item
