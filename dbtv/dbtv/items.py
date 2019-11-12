# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DbtvItem(scrapy.Item):
    # define the fields for your item here like:
    rate = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    _id = scrapy.Field()
    episodes_count = scrapy.Field()
    star = scrapy.Field()
    subtype = scrapy.Field()
    directors = scrapy.Field()
    actors = scrapy.Field()
    duration = scrapy.Field()
    region = scrapy.Field()
    types = scrapy.Field()
    release_year = scrapy.Field()

