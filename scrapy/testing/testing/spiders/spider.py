import scrapy

class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
       li = response.xpath('//*[@class="quote"]')
       print("//////")
    #    print(len(li))
       for i in li:
           print(i.xpath(".//*[@class='text']/@itemprop").get())
