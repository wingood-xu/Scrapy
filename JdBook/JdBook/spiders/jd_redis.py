# -*- coding: utf-8 -*-
import scrapy
from JdBook.items import JdbookItem
import json
from scrapy_redis.spiders import RedisSpider
import subprocess


class JdSpider(RedisSpider):
    name = "jd_redis"

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(JdSpider, self).__init__(*args, **kwargs)
        # self.asyn_redis2mongo()


    redis_key = 'python3'

    def asyn_redis2mongo(self):
        subprocess.call(['python', 'H:/PyProjects/Scrapy/JdBook/JdBook/redis2mongo.py'])

    def parse(self, response):
        big_list = response.xpath('//*[@id="booksort"]/div[2]/dl/dt')
        for big in big_list:
            sort = {}
            sort['big_sort'] = big.xpath('./a/text()').extract()[0]
            sort['big_url'] = 'https:' + big.xpath('./a/@href').extract()[0]
            small_list = big.xpath('./following-sibling::dd[1]/em/a')
            for small in small_list:
                temp = {}
                temp.update(sort)
                temp['small_sort'] = small.xpath('./text()').extract()[0]
                temp['small_url'] = 'https:' + small.xpath('./@href').extract()[0]

                # print(temp)
                yield scrapy.Request(temp['small_url'],
                                     callback=self.parse_list,
                                     meta={'meta_1': temp})

    def parse_list(self, response):
        temp = response.meta['meta_1']

        book_list = response.xpath('//*[@id="plist"]/ul/li/div//div[@class="p-img"]')
        for book in book_list:
            temp1 = {}
            temp1.update(temp)
            temp1['name'] = \
                book.xpath('./following-sibling::div[@class="p-name"]/a/em/text()').extract()[0].strip()
            temp1['authors'] = \
                book.xpath('./following-sibling::div[@class="p-bookdetails"]/span[1]/span/a/text()').extract_first()
            temp1['publisher'] = \
                book.xpath('./following-sibling::div[@class="p-bookdetails"]/span[2]/a/text()').extract_first()
            temp1['pub_time'] = \
                book.xpath('./following-sibling::div[@class="p-bookdetails"]/span[3]/text()').extract_first().strip()
            temp1['detail_link'] = \
                'https:' + book.xpath('./following-sibling::div[@class="p-name"]/a/@href').extract()[0]
            temp1['cover_link'] = 'https:' + book.xpath('.//img/@src|.//img/@data-lazy-img').extract_first()
            # 构建price链接
            uid = ''.join(filter(str.isdigit, temp1['detail_link']))
            url = 'https://p.3.cn/prices/mgets?skuIds=J_{}&pduid=15096921403451209881805'.format(uid)
            # item = JdbookItem()
            # item.update(temp1)
            # yield item

            # url = 'https://www.baidu.com'
            # print(temp1)
            yield scrapy.Request(url, callback=self.parse_price, meta={'meta_2': temp1})

    def parse_price(self, response):

        temp2 = response.meta['meta_2']
        # price_list = response.text
        item = JdbookItem()
        item.update(temp2)
        # item['price'] = json.loads(price_list)[0]["op"]
        # item['price']=response.status
        yield item
