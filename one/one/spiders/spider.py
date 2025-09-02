import scrapy
from one.items import OneItem

class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for i in quotes:
            items = OneItem()
            items['quote']=i.xpath('.//*[@class="text"]/text()').get()
            items['author']=i.xpath('.//*[@class="author"]/text()').get()
            items['tags'] = i.xpath('.//div[@class="tags"]/meta[@class="keywords"]/@content').get()
            yield items

        next = response.xpath('//*[@class="next"]/a/@href').get()
        if next:
            new_url = response.urljoin(next)
            yield scrapy.Request(new_url)



     # yield{
            #     'quotes':i.xpath('.//*[@class="text"]/text()').extract_first(),
            #     'author':i.xpath('.//*[@class="author"]/text()').extract_first(),
            #     'tags':i.xpath('.//*[@class="tag"]/text()').extract()
            # }