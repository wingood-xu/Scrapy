# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient
from scrapy.conf import settings


class SunPipeline(object):
    def open_spider(self, spider):
        self.file = open('dongguan.json', 'w',encoding='utf-8')

    def process_item(self, item, spider):
        str_data = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.file.write(str_data)
        return item

    def close_spider(self, spider):
        self.file.close()

class MongoPipeline(object):
    def open_spider(self, spider):
        host = settings['MONGO_HOST']
        port = settings['MONGO_PORT']
        dbname = settings['MONGO_DBNAME']
        colname = settings['MONGO_COLNAME']
        self.client = MongoClient(host,port)
        self.db = self.client[dbname]
        self.col = self.db[colname]


    def process_item(self, item, spider):
        data = dict(item)
        self.col.insert(data)
        return item

    def close_spider(self, spider):
        self.client.close()