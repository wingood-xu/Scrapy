# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdbookItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    big_sort = scrapy.Field() ###
    small_sort = scrapy.Field() ###
    cover_link = scrapy.Field() #
    detail_link = scrapy.Field()  #
    authors = scrapy.Field() #
    publisher = scrapy.Field() #
    pub_time = scrapy.Field() #
    price = scrapy.Field()
    big_url = scrapy.Field() ###
    small_url = scrapy.Field() ###
    pass
