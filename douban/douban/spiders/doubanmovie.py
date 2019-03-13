# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
#将默认的编码格式改为utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class DoubanmovieSpider(scrapy.Spider):
    #爬虫名
    name = 'doubanmovie'
    #爬虫的限制域
    allowed_domains = ['douban.com']
    num = 0
    #爬虫起始的url
    start_urls = ["https://movie.douban.com/top250"]

    #函数名不能更改
    def parse(self, response):
        item = DoubanItem()
        movie = response.xpath('//div[@class="info"]')
        for each in movie:
            #获取电影名
            item['name'] = each.xpath('./div[@class="hd"]/a[@class=""]/span[@class="title"]/text()').extract()[0]
            #获取电影评分
            item['star'] = each.xpath('./div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            try:
                #获取电影简介
                item['intr'] = each.xpath('./div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()').extract()[0]
            except:
                item['intr'] = ""
            print u"电影名：%s\t评分：%s\t简介：%s\t" %(item['name'], item['star'], item['intr'].replace(u"\u22ef",u""))
            # print type(item['name']),type(item['star']),type(item['intr'])

        #循环爬取所有的页面
        if self.num <= 225:
            self.num += 25
            newurl = "https://movie.douban.com/top250?start=%s&filter="%self.num
            yield scrapy.Request(newurl,callback=self.parse)

