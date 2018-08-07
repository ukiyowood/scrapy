# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SswuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class MyFirstProjectItem(scrapy.Item):
	#pass
	urlname = scrapy.Field()
	urlkey = scrapy.Field()
	urlrc = scrapy.Field()
	urladdr = scrapy.Field()