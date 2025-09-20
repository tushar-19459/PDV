# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Work3Item(scrapy.Item):
    # define the fields for your item here like:
    job_Title = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
    category = scrapy.Field()
    skills = scrapy.Field()
    pass
