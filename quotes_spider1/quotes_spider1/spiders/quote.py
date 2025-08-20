import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        quots = response.xpath('//*[@class ="quote"]')
        for i in quots:
            yield{
                'text':i.xpath('.//*[@class="text"]/text()').extract_first(),
                'author':i.xpath('.//*[@class="author"]/text()').extract_first(),
                'tags':i.xpath('.//*[@class="tag"]/text()').extract()
                }