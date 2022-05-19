import scrapy


class SuumoSpider(scrapy.Spider):
    name = 'suumo'
    allowed_domains = ['suumo.jp']
    start_urls = ['https://suumo.jp/chintai']

    def parse(self, response):
        pass
