# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #序号
    serial_number = scrapy.Field()
    #电影名称
    movie_name = scrapy.Field()
    #电影介绍
    introduce = scrapy.Field()
    #电影星级
    star = scrapy.Field()
    #评论
    evaluate = scrapy.Field()
    #描述
    describe = scrapy.Field()