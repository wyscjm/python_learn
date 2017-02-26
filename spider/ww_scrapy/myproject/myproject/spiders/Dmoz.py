# -*- coding: utf-8 -*-
import scrapy

from myproject.items import DmozItem 

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
            ]

    def parse(self, response):
        sel = scrapy.Selector(response)
        sites =  sel.xpath('//ul/li')
        for site in sites:
            item = DmozItem()
            item["title"] = site.xpath('a/text()').extract()
            item["link"] = site.xpath('a/@href').extract()
            item["desc"] = site.xpath("text()").extract()
            yield item
            #print title
