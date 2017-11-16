# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 存储照片的名字
    imagesUrls = scrapy.Field()  # 照片的url路径
    imagesPath = scrapy.Field()  # 照片保存在本地的路径
    pass
