# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TodaymoviePipeline(object):
    def process_item(self, item, spider):
        save = "movie.txt"
        with open(save,'a',encoding='utf-8') as fp:
            fp.write(item['movieName'][0]+'\n')
        return item