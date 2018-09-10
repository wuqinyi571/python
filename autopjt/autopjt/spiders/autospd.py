# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request

class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = (
        'http://category.dangdang.com/pg1-cp01.19.10.00.00.00.html',
    )
    def parse(self, response):
        item=AutopjtItem()
        item["name"]=response.xpath("//a[@class='pic']/@title").extract()
        item["price"] = response.xpath("//span[@class='search_now_price']/text()").extract()
        item["link"] = response.xpath("//a[@class='pic']/@href").extract()
        item["comnum"] = response.xpath("//a[@class='search_comment_num']/text()").extract()
        yield item
        for i in range(1,76):
            url="http://category.dangdang.com/pg"+str(i)+"-cp01.19.10.00.00.00.html"
            yield Request(url, callback=self.parse)
