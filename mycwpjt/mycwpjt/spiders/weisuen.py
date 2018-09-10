# -*- coding: utf-8 -*-
import sys
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mycwpjt.items import MycwpjtItem

class WeisuenSpider(CrawlSpider):
    name = 'weisuen'
    allowed_domains = ['sohu.com']
    start_urls = ['http://news.sohu.com/']

    rules = (
        Rule(LinkExtractor(allow=('.*?/a/.*?'),allow_domains=('sohu.com')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = MycwpjtItem()
        reload(sys)
        sys.setdefaultencoding('utf-8')
        type = sys.getfilesystemencoding()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i["name"] = response.xpath("/html/head/title/text()").extract().decode('utf-8').encode(type)
        i["link"] = response.xpath("//link[@rel='canonical']/@href").extract().decode('utf-8').encode(type)
        return i
