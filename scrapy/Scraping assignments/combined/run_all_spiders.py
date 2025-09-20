
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Import spiders by their file names
from combined.spiders.spiderOne import SpideroneSpider
from combined.spiders.spiderTwo import SpidertwoSpider
from combined.spiders.spiderThree import SpiderthreeSpider

def run_all():
    process = CrawlerProcess(get_project_settings())

    # Add all three spiders to run in parallel
    process.crawl(SpideroneSpider)
    process.crawl(SpidertwoSpider)
    process.crawl(SpiderthreeSpider)

    process.start()

if __name__ == "__main__":
    run_all()
