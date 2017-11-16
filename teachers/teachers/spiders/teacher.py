# -*- coding: utf-8 -*-
import scrapy
from teachers.items import TeachersItem


class TeacherSpider(scrapy.Spider):
    name = "teacher"
    allowed_domains = ["itcast.cn"]
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # techers = []
        teacher_list = response.xpath('//div[@class="li_txt"]')
        for teacher in  teacher_list:
            item = TeachersItem()
            item['name'] = teacher.xpath('./h3/text()').extract_first()
            item['level'] = teacher.xpath('./h4/text()').extract_first()
            item['info'] = teacher.xpath('./p/text()').extract_first()
            # techers.append(item)
            yield item
        # return techers




