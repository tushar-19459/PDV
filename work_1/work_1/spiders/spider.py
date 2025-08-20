import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["python.org"]
    start_urls = ["https://python.org/jobs/"]

    def parse(self, response):
        ol = response.xpath('//ol/li')
        for i in ol:
            print("------")
            yield{
                'job Title':i.xpath('.//*[@class="listing-company-name"]/a/text()').extract()[0],
                'location':i.xpath('.//*[@class="listing-location"]/a/text()').extract()[0],
                'skill set required':i.xpath('.//*[@class="listing-job-type"]/a/text()').extract(),
                'data of job posted':i.xpath('.//*[@class="listing-posted"]/time/text()').extract()[0],
                'category':i.xpath('.//*[@class="listing-company-category"]/a/text()').extract()[0],
            }
            # print(i.xpath('.//*[@class="listing-company-name"]/a/text()').extract())
            # print(i.xpath('.//*[@class="listing-location"]/a/text()').extract())
            # print(i.xpath('.//*[@class="listing-job-type"]/a/text()').extract())
            # print(i.xpath('.//*[@class="listing-posted"]/time/text()').extract())
            # print(i.xpath('.//*[@class="listing-company-category"]/a/text()').extract())
            # title = i.xpath('.//h2/span/a/text()').extract()
            # span = i.xpath('.//span').getall()
            # print("title :"+title[0])
            # print("location :"+title[1])
            # print("span :"+span)
            print("------")