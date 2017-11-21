# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy_redis.pipelines import RedisPipeline
from scrapy.utils.serialize import ScrapyJSONEncoder
from twisted.internet import defer
from twisted.internet.threads import deferToThread

default_serialize = ScrapyJSONEncoder(ensure_ascii=False).encode

class JdbookPipeline(object):
    def process_item(self, item, spider):
        return item

class JdPipeline(RedisPipeline):


    def process_item(self, item, spider):
        return deferToThread(self._process, item, spider)


    def _process(self, item, spider):
        key = self.item_key(item, spider)
        data = default_serialize(item)
        self.server.rpush(key, data)
        return item
