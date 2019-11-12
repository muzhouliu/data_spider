# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NeccItem(scrapy.Item):
    # define the fields for your item here like:
    top_priority = scrapy.Field()
    game_hots = scrapy.Field()
    game_name = scrapy.Field()
    game_type = scrapy.Field()
    game_tag = scrapy.Field()
    game_face = scrapy.Field()

    _id = scrapy.Field()
    anchor_id = scrapy.Field()
    anchor_name = scrapy.Field()
    anchor_gender = scrapy.Field()
    anchor_hots = scrapy.Field()
    anchor_face = scrapy.Field()
    anchor_level = scrapy.Field()

    anchor_style = scrapy.Field()
    anchor_birthday = scrapy.Field()
    anchor_type = scrapy.Field()
    anchor_sign = scrapy.Field()

    vision_visitor = scrapy.Field()
    vision_width = scrapy.Field()
    vision_height = scrapy.Field()

    city_code = scrapy.Field()
    province_code = scrapy.Field()

    follower_num = scrapy.Field()
    room_face = scrapy.Field()
    room_title = scrapy.Field()
    room_start = scrapy.Field()
    live_minute = scrapy.Field()
    live_type = scrapy.Field()
