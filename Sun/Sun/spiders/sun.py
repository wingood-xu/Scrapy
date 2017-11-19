# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Sun.items import SunItem
import chardet


class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']

    rules = (
        # 'questionType?type=4&page=\d+'
        Rule(LinkExtractor(allow=r'questionType\?type=4&page=\d+'), follow=True),
        # 'html/question/201711/352493.shtml'
        Rule(LinkExtractor(allow=r'html/question/\d+/\d+.shtml'), callback='parse_item'),
    )

    def parse_item(self, response):
        # print(response.url)
        # print(chardet.detect(response.body))

        item = SunItem()
        item['number'] = response.xpath('/html/body/div[6]/div/div[1]/div[1]/strong/text()').extract()[0].split(':')[-1].strip()
        title = response.xpath('/html/body/div[6]/div/div[1]/div[1]/strong/text()').extract()[0].split('：')[-1].split()[0]
        item['title'] = title.split(' ')[0]

        item['link'] = response.url
        content = response.xpath('//div[@class="c1 text14_2"]/text()|//div[@class="contentext"]/text()').extract()
        print(content)
        item['content'] = ''.join([i.replace(' ','') for i in content]).replace('\xa0', '')

        yield item
