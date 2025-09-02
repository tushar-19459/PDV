import scrapy
from quotes_spider1.items import QuotesSpider1Item
class QuoteSpider(scrapy.Spider):
    name = "quote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]
    
    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for i in quotes:
            yield{
                'quotes':i.xpath('.//*[@class="text"]/text()').extract_first(),
                'author':i.xpath('.//*[@class="author"]/text()').extract_first(),
                'tags':i.xpath('.//*[@class="tag"]/text()').extract()
            }
        next = response.xpath('//*[@class="next"]/a/@href').extract_first()
        new_url = response.urljoin(next)
        yield scrapy.Request(new_url)
