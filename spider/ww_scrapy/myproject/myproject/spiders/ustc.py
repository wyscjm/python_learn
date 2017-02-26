# -*- coding: utf-8 -*-
import scrapy
from myproject.items import UstcItem

class UstcSpider(scrapy.Spider):
    name = "ustc"
    allowed_domains = ["ustc.edu.cn"]
    start_urls = [
           "http://gradschool.ustc.edu.cn/articles/2010/09/18.html"
            ]

    def parse(self, response):
        item = UstcItem()
        sel = scrapy.Selector(response)
        sites = sel.xpath("//td[@class='article']/a")
        for site in sites:
            item["title"] = site.xpath("text()").extract()
            item["link"] = site.xpath("@href").extract()
            #item["file_urls"] = item["link"][0]
            item["file_urls"] = site.xpath("@href").extract()
            yield item

    def spider_closed(self, spider):
        import pdb
        pdb.set_trace()
        print spider.item
        print "spider closed"
