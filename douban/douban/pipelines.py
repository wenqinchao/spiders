# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from douban.items import DoubanItem

class DoubanPipeline(object):
    def process_item(self, item, spider):
        for name,star,intr in item['name'],item['star'],item['intr']:
            print "电影名：%s\t评分：%s\t简介：%s\t"%(name,star,intr)
