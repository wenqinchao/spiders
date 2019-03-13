# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import  Rule
from juzi.items import JuziItem
from scrapy_redis.spiders import RedisCrawlSpider
import time

class JzSpider(RedisCrawlSpider):
    name = 'jz'
    # allowed_domains = ['itjuzi.com']
    # start_urls = ['http://itjuzi.com/']
    redis_key="jzspider:start_urls"
    #每一页的链接
    page_urls = LinkExtractor(allow=r"https://www.itjuzi.com/company?page=\d+")
    #每个公司的链接
    company_urls = LinkExtractor(allow="https://www.itjuzi.com/company/\d+")

    rules = (
        Rule(link_extractor=page_urls, follow=True),
        Rule(link_extractor=company_urls,callback="parse_item"),
    )
    #动态生成限制域
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(JzSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        item = JuziItem()
        item['id'] = response.url.split('/')[-1]
        item['part_name'] = self.get_part_name(response)
        item['invest_status'] = self.get_invest_status(response)
        item['c_type'] = self.get_c_type(response)
        item['c_address'] = self.get_c_address(response)
        item['service_type'] = self.get_service_type(response)
        item['total_name'] = self.get_total_name(response)
        item['build_time'] = self.get_bulid_time(response)
        item['c_size'] = self.get_c_size(response)
        item['intro'] = self.get_intro(response)
        item['run_status'] = self.get_run_status(response)
        item['comp_url'] = response.url
        item['do_time'] = time.strftime("%d-%b-%Y %H:%M:%S")
        return item

    #获取公司的简称
    def get_part_name(self,response):
        try:
            part_name = response.xpath('//div[@class="picinfo"]/div[@class="line-title"]//h1/text()').extract()[0].strip()
        except:
            part_name = "None"
        return part_name

    #获取公司的获投状况
    def get_invest_status(self,response):
        try:
            invest_status = response.xpath('//div[@class="picinfo"]/div[@class="line-title"]//h1/span/text()').extract()[0].strip()
        except:
            invest_status = "None"
        return invest_status

    #获取公司的类型
    def get_c_type(self,response):
        try:
            c_type = response.xpath('//div[@class="picinfo"]/div[@class="info-line"]/h2/text()').extract()[0]
        except:
            c_type = "None"
        return c_type

    #获取公司的地址
    def get_c_address(self,response):
        address_list = response.xpath('//div[@class="picinfo"]/div[@class="info-line"][2]/span[2]/a/text()').extract()
        if address_list != []:
            c_address = "-".join(address_list)
        else:
            c_address = "None"
        return c_address

    #获取公司的业务类型
    def get_service_type(self,response):
        service_list = response.xpath('//div[@class="tagset dbi c-gray-aset"]/a/span/text()').extract()
        if len(service_list):
            service_type = ",".join(service_list)
        else:
            service_type = "None"
        return service_type

    #获取公司的全称
    def get_total_name(self,response):
        try:
            total_name = response.xpath('//div[@class="des-more"]/div[1]/h2/text()').extract()[0][5:]
        except:
            total_name = "None"
        return total_name

    #获取公司的成立时间
    def get_bulid_time(self,response):
        try:
            build_time = response.xpath('//div[@class="des-more"]/div[2]/h2[1]/text()').extract()[0][5:]
        except:
            build_time ="None"
        return build_time

    #获取公司的规模
    def get_c_size(self,response):
        try:
            c_size = response.xpath('//div[@class="des-more"]/div[2]/h2[2]/text()').extract()[0].strip()[5:]
        except:
            c_size = "None"
        return c_size

    #获取公司的简介
    def get_intro(self,response):
        intro_list = response.xpath('//div[@class="block"][2]/div/text()').extract()
        if len(intro_list) == 1:
            intro = intro_list[0]
        elif len(intro_list) > 1:
            intro = "".join(intro_list)
        else:
            intro = "None"
        return intro

    #获取运营状态
    def get_run_status(self,response):
        try:
            run_status = response.xpath('//div[@class="des-more"]//span/text()').extract()[0]
        except:
            run_status = "None"
        return run_status

