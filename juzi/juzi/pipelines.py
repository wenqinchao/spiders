# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
class JuziPipeline(object):
    def process_item(self, item, spider):
        item['do_time'] = time.strftime("%d-%b-%Y %H:%M:%S")
        item['spider'] = spider.name
        return item
