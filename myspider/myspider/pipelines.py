# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MyspiderPipeline(object):
    def open_spider(self, spider):
        self.file = open('itcast.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        # 将item转换成字典
        dict_data = dict(item)
        # 将 字典转换成字符串
        str_data = json.dumps(dict_data,ensure_ascii=False) + ',\n'
        # 写文件
        self.file.write(str_data)
        return item

    def close_spider(self, spider):
        self.file.close()
