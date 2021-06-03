import scrapy


class ChecktrdeSpider(scrapy.Spider):
    name = 'checktrde'
    allowed_domains = ['checktrade.com']
    start_urls = ['http://checktrade.com/']

    def parse(self, response):
        pass
