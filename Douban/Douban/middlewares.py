# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from Douban.settings import USER_AGENT_LIST,PROXY_LIST
# from Douban.proxy import get_proxy
import requests


class DoubanSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomUserAgent(object):
    def process_request(self, request, spider):
        ua = random.choice(USER_AGENT_LIST)
        print(ua)
        request.headers['User-Agent'] = ua


class RandomProxy(object):
    def process_request(self, request, spider):
        # 随机获取一个代理
        proxy = self.get_proxy()
        # 判断代理情况
        print(proxy)

        request.meta['proxy'] = 'http://'+proxy
    def process_response(self ,request, response, spider):
        if response.status != 200:
            proxy = self.get_proxy()
            # 判断代理情况
            print(proxy)
            request.meta['proxy'] = 'http://'+proxy
            return request
        return response
    def get_proxy(self):
        response = requests.get('http://127.0.0.1:5010/get/')
        return response.text