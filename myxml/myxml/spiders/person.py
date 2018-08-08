# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem


class PersonSpider(XMLFeedSpider):
    name = 'person'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/test.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'person' # change it accordingly

    def parse_node(self, response, selector):
        i = MyxmlItem()
        i['title'] = selector.xpath('/person/email/text()').extract()
        print("E-Mails are: ")
        print(i['title'])
        #i['url'] = selector.select('url').extract()
        #i['name'] = selector.select('name').extract()
        #i['description'] = selector.select('description').extract()
        return i
