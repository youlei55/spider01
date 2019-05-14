# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UniversatyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    grade = scrapy.Field()
    school = scrapy.Field()
    top = scrapy.Field()
    start = scrapy.Field()
    layout = scrapy.Field()
    score = scrapy.Field()
