import scrapy
from combined.items import Work3Item


class SpiderthreeSpider(scrapy.Spider):
    name = "spiderThree"
    allowed_domains = ["pythonjobs.github.io"]
    start_urls = ["https://pythonjobs.github.io/"]
    print("########################")
    def parse(self, response):
        a = response.xpath('//*[@class="go_button"]/@href').extract()

        for i in a:
            yield response.follow(i, callback=self.parse_job)

            
    def parse_job(self, response):
        items  = Work3Item()
        tags = response.xpath('//*[@class="tags clear"]/li/a/text()').extract()
        tags = [item.strip() for item in tags]
        items['job_Title'] =  response.xpath("//h1/text()").extract_first().strip()
        items['location'] =  response.xpath("(//span)[5]//text()").extract_first().strip()
        items['date'] =  response.xpath("(//span)[3]//text()").extract()[1].strip()
        items['category'] =  response.xpath("(//span)[4]//text()").extract_first().strip()
        items['skills'] =  ', '.join(tags)
        yield items