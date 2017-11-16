# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        items = response.xpath('//*[contains(@class,"odd") or contains(@class,"even")]')
        for item in items:
            temp = dict(
                position=item.xpath("./td[1]/a/text()").extract()[0],
                detailLink="http://hr.tencent.com/" + item.xpath("./td[1]/a/@href").extract()[0],
                type=item.xpath('./td[2]/text()').extract()[0] if len(
                    item.xpath('./td[2]/text()').extract()) > 0 else None,
                need_num=item.xpath('./td[3]/text()').extract()[0],
                location=item.xpath('./td[4]/text()').extract()[0],
                publish_time=item.xpath('./td[5]/text()').extract()[0]
            )
            print(temp)
            yield temp
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

        # return i
