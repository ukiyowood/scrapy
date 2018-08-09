# -*- coding: utf-8 -*-
import scrapy
from mypjt.items import MypjtItem


class SswuSpider(scrapy.Spider):
    name = 'sswu'
    allowed_domains = ['sina.com.cn']
    start_urls = [
    	'http://tech.sina.com.cn/d/s/2016-09-17/doc-ifxvyqwa3324638.shtml',
    	'http://sina.com.cn',
    	]

    def parse(self, response):
        item = MypjtItem()
        item['title'] = response.xpath("/html/head/title/text()").extract()
        item['key'] = response.xpath("//meta[@name='keywords']/@content").extract()
        #print(item['title)
        #print(item)
        return item