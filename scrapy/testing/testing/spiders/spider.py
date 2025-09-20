import scrapy

class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        tags = response.xpath('//*[@class="tag-item"]/a/@href')
        print("#################")
        for link in tags:
            print(link)
            yield response.follow(link,callback=self.extract)
        
       
        
    def extract(self,response):
        data = {}

        type = response.xpath('//h3/a/text()').extract_first()
        quote =  response.xpath('//*[@class="quote"]')
        next =  response.xpath('//*[@class="next"]/a/@href').extract_first()

        
        for i in quote:
            text = i.xpath('.//*[@class="text"]/text()').extract_first()
            auth = i.xpath('.//*[@class="author"]/text()').extract_first()
            data[auth]=text
        
        if next != None:
            yield response.follow(next,callback=self.extract)
        
        yield{
            type:data
        }
