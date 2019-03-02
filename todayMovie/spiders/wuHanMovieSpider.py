# -*- coding: utf-8 -*-
import scrapy

from todayMovie.items import TodaymovieItem
class WuhanmoviespiderSpider(scrapy.Spider):
    name = 'wuHanMovieSpider'
    allowed_domains = ['douban.com']
    start_urls = []
    for i in range(0,10):
        start_urls.append('https://movie.douban.com/top250?start='+str(i*25)+'&filter=')

    def parse(self, response):
        subSelector = response.xpath('//ol[@class="grid_view"]/li')
        items = []
        for each in subSelector:
            item = TodaymovieItem()
            item['movieName'] = each.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract()
            items.append(item)
        return items

