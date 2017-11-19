# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = "douyu"
    allowed_domains = ["douyucdn.cn"]
    start_urls = ['http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=']
    offset = 0

    def parse(self, response):
        room_list = json.loads(response.text)['data']
        for room in room_list:
            item = DouyuItem()
            item['nick_name'] = room['nickname']
            item['uid'] = room['nickname']
            item['image_link'] = room['room_src']
            item['city'] = room['anchor_city']
            yield item

        if len(room_list) != 0:
            self.offset += 21
            yield scrapy.Request(self.start_urls[0] + str(self.offset),
                                 callback=self.parse)
