# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    #设置要获取的信息，命名复合变量命名规则即可
    name = scrapy.Field()
    star = scrapy.Field()
    intr = scrapy.Field()
