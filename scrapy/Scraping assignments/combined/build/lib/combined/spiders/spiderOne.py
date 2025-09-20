import scrapy
from combined.items import Work1Item

class SpideroneSpider(scrapy.Spider):
    name = "spiderOne"
    allowed_domains = ["python.org"]
    start_urls = ["https://python.org/jobs/"]

    
    def parse(self, response):
        ol = response.xpath('//ol/li')

        for i in ol:
            items = Work1Item()
            items['job_title'] = i.xpath('.//*[@class="listing-company-name"]/a/text()').extract()[0]
            items['location'] = i.xpath('.//*[@class="listing-location"]/a/text()').extract()[0]
            items['Skills'] = ", ".join(i.xpath('.//*[@class="listing-job-type"]/a/text()').extract())
            items['date'] = i.xpath('.//*[@class="listing-posted"]/time/text()').extract()[0]
            items['category'] = i.xpath('.//*[@class="listing-company-category"]/a/text()').extract()[0]
            yield items 
        
        next = response.xpath('//*[@class="next"]/a/@href').get()
        if next != "":
            new = response.urljoin(next)
            yield response.Request(new)