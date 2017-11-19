# -*- coding: utf-8 -*-
import os

import scrapy
from tencent_hr.items import TencentHrItem


class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["tencent.com"]
    start_urls = ['http://hr.tencent.com/position.php']

    def parse(self, response):
        work_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        for work in work_list:
            item = TencentHrItem()

            item['name'] = work.xpath('.//a/text()').extract_first()
            item['link'] = 'http://hr.tencent.com/' + work.xpath('.//a/@href').extract_first()
            item['type'] = work.xpath('./td[2]/text()').extract_first()
            item['num'] = work.xpath('./td[3]/text()').extract_first()
            item['site'] = work.xpath('./td[4]/text()').extract_first()
            item['pub_time'] = work.xpath('./td[5]/text()').extract_first()

            yield scrapy.Request(item['link'], callback=self.parse_detail, meta={'chuanzhi': item})

            # 获取下一页数据
            try:
                next_url = 'http://hr.tencent.com/' + response.xpath('//a[@id="next"]/@href').extract()[0]
                yield scrapy.Request(next_url, callback=self.parse)
            except:
                pass

    def parse_detail(self, response):
        item = response.meta['chuanzhi']
        item['duty'] = ''.join(response.xpath('//tr[3]/td/ul/li/text()').extract())
        item['require'] = ''.join(response.xpath('//tr[4]/td/ul/li/text()').extract())
        yield item
