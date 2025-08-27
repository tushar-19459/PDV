import scrapy
from work_1.items import Work1Item
from scrapy.loader import ItemLoader
class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["python.org"]
    start_urls = ["https://python.org/jobs/"]

    # using the normal yield methord 
    # def parse(self, response):
    #     ol = response.xpath('//ol/li')
    #     for i in ol:
    #         yield{
    #             'job Title':i.xpath('.//*[@class="listing-company-name"]/a/text()').extract()[0],
    #             'location':i.xpath('.//*[@class="listing-location"]/a/text()').extract()[0],
    #             'skill set required':i.xpath('.//*[@class="listing-job-type"]/a/text()').extract(),
    #             'data of job posted':i.xpath('.//*[@class="listing-posted"]/time/text()').extract()[0],
    #             'category':i.xpath('.//*[@class="listing-company-category"]/a/text()').extract()[0],
    #         }
            
    # using the normal items and yield 
    def parse(self, response):
        items = Work1Item()
        ol = response.xpath('//ol/li')

        for i in ol:
            items['job_title'] = i.xpath('.//*[@class="listing-company-name"]/a/text()').extract()[0]
            items['location'] = i.xpath('.//*[@class="listing-location"]/a/text()').extract()[0]
            items['Skills'] = i.xpath('.//*[@class="listing-job-type"]/a/text()').extract()
            items['date'] = i.xpath('.//*[@class="listing-posted"]/time/text()').extract()[0]
            items['category'] = i.xpath('.//*[@class="listing-company-category"]/a/text()').extract()[0]
            yield items
            