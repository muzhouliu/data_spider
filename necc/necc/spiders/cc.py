# -*- coding: utf-8 -*-
import scrapy
import json
from necc.items import NeccItem


class CcSpider(scrapy.Spider):
    name = 'cc'
    allowed_domains = ['cc.163.com']
    start_urls = ['http://cc.163.com/category/?format=json']

    def parse(self, response):
        category_json = json.loads(response.body.decode())
        game_list = category_json['game_list']
        for game in game_list:
            item = NeccItem()
            item['top_priority'] = game['top_priority']
            item['game_hots'] = game['hot_score']
            item['game_name'] = game['gamename']
            item['game_type'] = game['gametype']
            item['game_tag'] = game['game_tag']
            item['game_face'] = game['img']
            yield scrapy.Request(
                'http://cc.163.com/api/category/{}/?format=json'.format(item['game_type']),
                callback=self.room_parse,
                meta={'item': item}
            )

    def room_parse(self,response):
        item = response.meta['item']
        if response.url != 'http://cc.163.com/ent/':
            lives_json = json.loads(response.body.decode())
            room_list = lives_json['lives']
            for room in room_list:
                item['_id'] = room['uid']
                item['anchor_id'] = room['ccid']
                item['anchor_name'] = room['nickname']
                item['anchor_gender'] = room['gender']
                item['anchor_hots'] = room['hot_score']
                item['anchor_face'] = room['purl']
                item['anchor_level'] = room['anchor_level']['level']

                item['anchor_style'] = room.get('anchor_style')
                item['anchor_birthday'] = room.get('birthday')
                item['anchor_type'] = room.get('anchor_type')
                item['anchor_sign'] = room['game_sign_info']['signtime'] \
                    if room.get('game_sign_info') else None

                item['city_code'] = room.get('city')
                item['province_code'] = room.get('province')

                item['vision_visitor'] = room['vision_visitor']
                item['vision_width'] = room['width']
                item['vision_height'] = room['height']

                item['follower_num'] = room['follower_num']
                item['room_face'] = room['poster']
                item['room_title'] = room['title']
                item['room_start'] = room['startat']
                item['live_minute'] = room['liveMinute']
                item['live_type'] = room['livetype']
                yield item
