# -*- coding: utf-8 -*-
import scrapy


class RenrenFormSpider(scrapy.Spider):
    name = "renren_form"
    allowed_domains = ["renren.com"]
    start_urls = ['http://renren.com/']

    def parse(self, response):
        dataform = {
            'email': '17173805860',
            'password': '1qaz@WSX3edc',
        }
        yield scrapy.FormRequest.from_response(response,formdata=dataform,callback = self.after_login)


    def after_login(self,response):
        with open('renren_form.html','wb') as f:
            f.write(response.body)