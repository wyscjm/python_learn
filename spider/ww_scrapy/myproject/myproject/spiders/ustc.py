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
            yield item
