# -*- coding: utf-8 -*-
import scrapy
from myspider.items import MyspiderItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    # 修改起始的url
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # 获取所有教师节点列表
        node_list = response.xpath('//div[@class="li_txt"]')
        # print (len(node_list))

        data_list = []
        # 便利节点列表
        for node in node_list:
            # 创建itme实例，用于存储数据
            item = MyspiderItem()
            # 抽取数据
            item['name'] = node.xpath('./h3/text()').extract()[0]
            item['title'] = node.xpath('./h4/text()').extract()[0]
            item['desc'] = node.xpath('./p/text()').extract()[0]

            # 存放数据
            data_list.append(item)

        # 返回数据列表
        print(data_list)
        return data_list