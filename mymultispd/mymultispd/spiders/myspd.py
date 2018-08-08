# -*- coding: utf-8 -*-
import scrapy


class MyspdSpider(scrapy.Spider):
    name = 'myspd'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://sina.com.cn/']

    def parse(self, response):
        pass
