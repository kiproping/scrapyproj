# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JackpotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pos =  scrapy.Field()
    time =  scrapy.Field()
    date =  scrapy.Field()
    flag = scrapy.Field()
    homet = scrapy.Field()
    hometodds = scrapy.Field()
    drawodds = scrapy.Field()
    awayt = scrapy.Field()
    awaytodds = scrapy.Field()
    result = scrapy.Field()

