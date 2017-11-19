# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentHrItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    type = scrapy.Field()
    num = scrapy.Field()
    site = scrapy.Field()
    pub_time = scrapy.Field()
    duty = scrapy.Field()
    require = scrapy.Field()

