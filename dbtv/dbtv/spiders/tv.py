# -*- coding: utf-8 -*-
import scrapy
import json
from dbtv.items import DbtvItem


class TvSpider(scrapy.Spider):
    name = 'tv'
    allowed_domains = ['movie.douban.com']

    def start_requests(self):

        # 携带Cookie，发送请求，获取响应
        cookie = 'bid=iDOwWeJdL_w; UM_distinctid=16cefcd94ec376-0f08adff05b724-5373e62-144000-16cefcd94ed2ad; ll="118283"; __utmc=30149280; __utmc=223695111; __yadk_uid=OCjuyaOrcvV3aQjobxy2EtfP7lHCnLYA; _vwo_uuid_v2=DC5E92E8CB1B8CF26B2C5378031A03941|77df642c751aef004d3fe3be4302dc05; __gads=ID=5c9c15bb1a40a422:T=1567391521:S=ALNI_MZKu1f8FVmPHftYO5MKEphbYj0lmw; trc_cookie_storage=taboola%2520global%253Auser-id%3De9277dc3-5c7d-4b54-8064-1d372532a87e-tuct45befd2; push_doumail_num=0; push_noty_num=0; CNZZDATA1272964020=349904066-1567390139-https%253A%252F%252Fwww.baidu.com%252F%7C1567476123; dbcl2="178898575:Oxaawjm2gjc"; ck=o1gl; __utma=30149280.987593826.1567391472.1567477757.1567481199.9; __utmz=30149280.1567481199.9.4.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utmt=1; __utmv=30149280.17889; __utmb=30149280.2.10.1567481199; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1567481211%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.258320206.1567391472.1567477757.1567481211.9; __utmz=223695111.1567481211.9.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=f784eca15f128c62.1567391500.9.1567481216.1567477825.; __utmb=223695111.2.10.1567481211'
        self.cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}

        self.page = 0
        self.temp_urls = 'https://movie.douban.com/j/new_search_subjects?start={}'
        start_url = self.temp_urls.format(self.page)
        yield scrapy.Request(
            start_url,
            callback=self.parse,
            cookies=self.cookies
        )

    def parse(self, response):
        tv_url = 'https://movie.douban.com/j/subject_abstract?subject_id={}'
        tv_list = json.loads(response.body.decode())['data']

        # 没内容，直接返回
        if (tv_list == []):
            return

        for tv in tv_list:
            item = DbtvItem()
            item['rate'] = tv['rate']
            item['title'] = tv['title']
            item['url'] = tv['url']
            item['_id'] = tv['id']
            yield scrapy.Request(
                tv_url.format(item['_id']),
                callback=self.tv_parse,
                meta={'item':item},
                cookies=self.cookies
            )

        # 翻页
        self.page += 20
        next_url = self.temp_urls.format(self.page)
        yield scrapy.Request(
            next_url,
            callback=self.parse,
            cookies=self.cookies
        )

    def tv_parse(self, response):
        item = response.meta['item']
        info = json.loads(response.body.decode())['subject']
        item['episodes_count'] = info["episodes_count"]
        item['star'] = info['star']
        item['subtype'] = info['subtype']
        item['directors'] = info['directors']
        item['actors'] = info['actors']
        item['duration'] = info['duration']
        item['region'] = info['region']
        item['types'] = info['types']
        item['release_year'] = info['release_year']
        yield item