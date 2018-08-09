# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json


class AutopjtPipeline(object):
    def __init__(self):
        self.file = codecs.open("/root/development/scrapy/autopjt/data/data2.json","wb",encoding = 'utf-8')

    def process_item(self,item,spider):
        
        
        for j in range(0,len(item['name'])):
            name = item['name'][j]
            price = item['price'][j]
            comnum = item['comnum'][j]
            link = item['link'][j]
            new_dict = {"name":name,"price":price,"comnum":comnum,"link":link}
            i = json.dumps(new_dict,ensure_ascii = False)
            line = i + '\n'
            self.file.write(line)
        return item
    def close_spider(self,spider):
        self.file.close()