import scrapy
from combined.items import Work2Item

class SpidertwoSpider(scrapy.Spider):
    name = "spiderTwo"
    allowed_domains = ["remote.co"]
    start_urls = ["https://remote.co/remote-jobs/developer"]

    def parse(self, response):
        job_div = response.xpath('//*[@id="job-table-wrapper"]/div')

        for i in job_div:
            items = Work2Item()
            job_role = i.xpath(".//*[@class='sc-fzEeWY jYWVDl']/text()").get()
            if job_role!= None:
                items['job_role'] = i.xpath(".//*[@class='sc-fzEeWY jYWVDl']/text()").get()

                items['company'] = i.xpath('.//h3/text()').get()

                items['posted_on'] = i.xpath(".//span[2]/text()").get()

                items['salary'] = i.xpath(".//li[4]/text()").get()
        
                items['location'] = i.xpath(".//*[@class='sc-fdZtqL beUnFW']/text()").get()

                yield items

