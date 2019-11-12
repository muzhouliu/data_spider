# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
from pymongo import MongoClient

class DbtvPipeline(object):
    def open_spider(self, spider):
        self.count = 0
        self.start_time = time.time()

        client = MongoClient(spider.settings.get('MONGO_HOST'), spider.settings.get('MONGO_PORT'))
        db = client[spider.settings.get('MONGO_DB')]
        self.col = db[spider.settings.get('MONGO_COLL')]

    def close_spider(self, spider):
        end_time = time.time()
        total_time = end_time - self.start_time
        print("Finish Time: {:.2f}s".format(total_time))

    def process_item(self, item, spider):
        self.count += 1
        self.col.save(dict(item))
        print('Save the {:0>4} document. >>> OK!'.format(self.count))
        return item
