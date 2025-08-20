import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["remote.co"]
    start_urls = ["https://remote.co/remote-jobs/developer"]

    def parse(self, response):
        print("#############"+response)
