# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
from pymongo import MongoClient
from pymysql import connect

class NeccPipeline(object):
    def open_spider(self, spider):
        localtime = time.localtime()

        client = MongoClient(spider.settings.get('MONGO_HOST'), spider.settings.get('MONGO_PORT'))
        db = client[spider.settings.get('MONGO_DB')]
        self.col = db['cc{}'.format(localtime[2])]

        self.conn = connect(host='localhost', port=3306, database='necc', user='root', password='mysql', charset='utf8mb4')
        self.cs = self.conn.cursor()

        self.start_time = time.time()
        print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))

    def close_spider(self, spider):
        self.cs.close()
        self.conn.close()

        end_time = time.time()
        total_time = end_time - self.start_time
        print("Finish Time: {:.2f}s".format(total_time))

    def process_item(self, item, spider):
        self.col.save(dict(item))

        # 备用方法
        # sql = "INSERT INTO cc VALUES(0, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # 安全方法
        sql = "INSERT INTO cc (game_name, game_type, game_tag, _id, anchor_id, anchor_name, anchor_gender, anchor_hots, anchor_level, anchor_birthday, anchor_type, anchor_sign, city_code, province_code, vision_visitor, follower_num, room_start, live_minute) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        game_name = item['game_name']
        game_type = item['game_type']
        game_tag = item['game_tag']
        uid = item['_id']
        anchor_id = item['anchor_id']
        anchor_name = item['anchor_name']
        anchor_gender = item['anchor_gender']
        anchor_hots = item['anchor_hots']
        anchor_level = item['anchor_level']
        anchor_birthday = item['anchor_birthday']
        anchor_type = item['anchor_type']
        anchor_sign = item['anchor_sign']
        city_code = item['city_code']
        province_code = item['province_code']
        vision_visitor = item['vision_visitor']
        follower_num = item['follower_num']
        room_start = item['room_start']
        live_minute = item['live_minute']

        info = (game_name, game_type, game_tag, uid, anchor_id, anchor_name, anchor_gender, anchor_hots, anchor_level, anchor_birthday, anchor_type, anchor_sign, city_code, province_code, vision_visitor, follower_num, room_start, live_minute)

        try:
            self.cs.execute(sql, info)
            self.conn.commit()
        except:
            self.conn.rollback()

        return item