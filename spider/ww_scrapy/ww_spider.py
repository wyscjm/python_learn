import scrapy

class ww_PdfSpider(scrapy.Spider):
    name = 'ww_PdfSpider'
    start_urls = ['http://gradschool.ustc.edu.cn/articles/2010/09/18.html']

    def parse(self, response):
        #for title in response.selector.xpath("//td.article/text()"):
        for title in response.css('html.body'):
            yield {'title': title.css('a ::text').extract_first()}

        next_page = response.css('div.prev-post > a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
