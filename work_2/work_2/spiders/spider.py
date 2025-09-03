import scrapy
from work_2.items import Work2Item

class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["remote.co"]
    start_urls = ["https://remote.co/remote-jobs/developer"]

    def parse(self, response):
        job_div = response.xpath('//*[@id="job-table-wrapper"]/div')
        data = job_div[0]

        # for i in job_div:
        #     job_role = i.xpath(".//*[@class='sc-fzEeWY jYWVDl']/text()").get()
        #     if job_role!= None:

        #         company = i.xpath('.//h3/text()').get()

        #         posted_on = i.xpath(".//span[2]/text()").get()

        #         salary = i.xpath(".//li[4]/text()").get()
        
        #         location = i.xpath(".//*[@class='sc-fdZtqL beUnFW']/text()").get()

        #         yield{
        #             'job_role':job_role,
        #             'company':company,
        #             'posted_on':posted_on,
        #             'salary':salary,
        #             'location':location,
        #         }

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