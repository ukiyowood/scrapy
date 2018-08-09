# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class MypjtPipeline(object):
    def __init__(self):
        self.file = codecs.open("/root/development/scrapy/mypjt/data/1.json","w",encoding = 'utf-8')
    def process_item(self, item, spider):
        #l = str(item) + '\n'
        #print(l)
        print(dict(item))
        i = json.dumps(dict(item),ensure_ascii = False)
        line = i + "\n"
        print(line)

        self.file.write(line)
        return item
    def close_spider(self,spider):
        self.file.close()
