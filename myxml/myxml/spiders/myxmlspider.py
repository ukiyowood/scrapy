# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem

class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1812671331.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'rss' # change it accordingly

    def parse_node(self, response, node):
        i = MyxmlItem()
        i['title'] = node.xpath('/rss/channel/item/title/text()').extract()
        i['link'] = node.xpath('/rss/channel/item/link/text()').extract()
        i['author'] = node.xpath('/rss/channel/item/author/text()').extract()
        for j in range(len(i['title'])):
        	print(str(j+1) + ' th novel:')
        	print("title is: ")
        	print(i['title'][j])
        	print('link is: ')
        	print(i['link'][j])
        	print('author is: ')
        	print(i['author'][j])
        	print('--------------------------------')

        #i['url'] = selector.select('url').extract()
        #i['name'] = selector.select('name').extract()
        #i['description'] = selector.select('description').extract()
        return i
