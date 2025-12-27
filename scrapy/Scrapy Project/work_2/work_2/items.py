# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Work2Item(scrapy.Item):
    # define the fields for your item here like:
    job_role = scrapy.Field()
    company = scrapy.Field()
    posted_on = scrapy.Field()
    salary = scrapy.Field()
    location = scrapy.Field()
    pass
