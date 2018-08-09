# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MysqlpjtPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(host='104.225.238.247',user='root',passwd='toor',db='mypydb',charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        title = item['title'][0]
        keywd = item['keywd'][0]

        sql = "insert into mytb(title,keywd) values('" + title + "','" + keywd + "')"
        #self.conn.query(sql)
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()
