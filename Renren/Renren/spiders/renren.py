# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = "renren"
    allowed_domains = ["renren.com"]
    start_urls = ['http://www.renren.com/PLogin.do']

    def start_requests(self):
        # url = self.start_urls[0]
        dataform = {
            'email':'17173805860',
            'password':'1qaz@WSX3edc',
        }
        yield scrapy.FormRequest(self.start_urls[0],formdata=dataform)

    def parse(self, response):
        with open('renren.html','wb') as f:
            f.write(response.body)
