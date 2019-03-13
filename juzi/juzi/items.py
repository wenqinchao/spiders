# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Field,Item

class JuziItem(Item):
    # define the fields for your item here like:
    #公司的id
    id = Field()
    #公司的简称
    part_name = Field()
    # 获投状态
    invest_status = Field()
    #公司类型
    c_type = Field()
    #业务类型
    service_type = Field()
    #公司地址
    c_address = Field()
    #公司全称
    total_name = Field()
    #成立时间
    build_time = Field()
    #公司规模
    c_size = Field()
    #简介
    intro = Field()
    #运营状态
    run_status = Field()
    #获取公司信息的url
    comp_url = Field()
    #获取时间
    do_time = Field()

