import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["pythonjobs.github.io"]
    start_urls = ["https://pythonjobs.github.io/"]

    def parse(self, response):
        print("###########")
        joblist = response.xpath('//*[@class="job"]')
        for i in joblist:
            print("-------")
            span = i.xpath('.//span/text()').extract()
            yield{
                'job Title':i.xpath('.//h1/a/text()').extract()[0],
                'location':span[0],
            #     'skill set required':,
                'data of job posted':span[1],
                'category':span[2],
            }
            # print(i.xpath('.//h1/a/text()').extract())
            # print(spans)