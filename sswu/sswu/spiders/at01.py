# -*- coding: utf-8 -*-
import scrapy


class At01Spider(scrapy.Spider):
    name = 'at01'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']

    def parse(self, response):
        pass
