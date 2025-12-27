import scrapy
from two.items import TwoItem

class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["python.org"]
    start_urls = ["https://python.org/jobs/"]

    def parse(self, response):
        joblist = response.xpath('//ol/li')
        print("///////////////")
        for i in joblist:
            item = TwoItem()
            item['title'] = i.xpath('.//h2/span/a/text()').extract_first()
            yield item

