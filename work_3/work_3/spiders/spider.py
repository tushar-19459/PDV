import scrapy
from work_3.items import Work3Item
class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["pythonjobs.github.io"]
    start_urls = ["https://pythonjobs.github.io/"]

    def parse(self, response):
        a = response.xpath('//*[@class="go_button"]/@href').extract()

        for i in a:
            yield response.follow(i, callback=self.parse_job)

    # using the normal menthord 
    # def parse_job(self, response):
    #     tags = response.xpath('//*[@class="tags clear"]/li/a/text()').extract()
    #     tags = [item.strip() for item in tags]
    #     yield {
    #         "job Title": response.xpath("//h1/text()").extract_first().strip(),
    #         "location": response.xpath("(//span)[5]//text()").extract_first().strip(),
    #         "data of job posted": response.xpath("(//span)[3]//text()").extract()[1].strip(),
    #         "category": response.xpath("(//span)[4]//text()").extract_first().strip(),
    #         "skills": tags,
    #     }

    # using the items 
    def parse_job(self, response):
        items  = Work3Item()
        tags = response.xpath('//*[@class="tags clear"]/li/a/text()').extract()
        tags = [item.strip() for item in tags]
        items['job_Title'] =  response.xpath("//h1/text()").extract_first().strip()
        items['location'] =  response.xpath("(//span)[5]//text()").extract_first().strip()
        items['date'] =  response.xpath("(//span)[3]//text()").extract()[1].strip()
        items['category'] =  response.xpath("(//span)[4]//text()").extract_first().strip()
        items['skills'] =  tags
        yield items