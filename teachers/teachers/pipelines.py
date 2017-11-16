# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from collections import  Iterable

class TeachersPipeline(object):

    def __init__(self):
        self.f = open('item.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        # print(isinstance(item,Iterable))
        # print(item)
        # print(type(item))
        # for it in item:
        print(item)
        str_it = json.dumps(dict(item),ensure_ascii=False)+',\n'
            # print(str_it)
        # str_it = json.dumps(dict(item),ensure_ascii=False)+',\n'
        self.f.write(str_it)
        return item

    def __del__(self):
        self.f.close()
