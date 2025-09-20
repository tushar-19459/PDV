# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Work1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    job_title = scrapy.Field()
    location = scrapy.Field()
    Skills = scrapy.Field()
    date = scrapy.Field()
    category = scrapy.Field()

    pass