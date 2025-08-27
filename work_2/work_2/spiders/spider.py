import scrapy

class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["remote.co"]
    start_urls = ["https://remote.co/remote-jobs/developer"]

    def parse(self, response):
        # Get all job links
        job_links = response.xpath("//div[@class='card-body']/h2/a/@href").getall()

        for link in job_links:
            yield response.follow(link, callback=self.parse_job)

        # Handle pagination (next page)
        next_page = response.xpath("//a[@class='next page-numbers']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_job(self, response):
        yield {
            "job_title": response.xpath("//h1/text()").get(default="").strip(),
            "company": response.xpath("//div[@class='company-card']//h3/text()").get(default="").strip(),
            "location": response.xpath("//div[@class='location']/text()").get(default="").strip(),
            "posted_date": response.xpath("//div[@class='date-posted']/text()").get(default="").strip(),
            "description": " ".join(response.xpath("//div[@class='job-description']//text()").getall()).strip()
        }