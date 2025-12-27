# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Work1Item(scrapy.Item):
    job_title = scrapy.Field()
    location = scrapy.Field()
    Skills = scrapy.Field()
    date = scrapy.Field()
    category = scrapy.Field()

class Work2Item(scrapy.Item):
    job_role = scrapy.Field()
    company = scrapy.Field()
    posted_on = scrapy.Field()
    salary = scrapy.Field()
    location = scrapy.Field()

class Work3Item(scrapy.Item):
    job_Title = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
    category = scrapy.Field()
    skills = scrapy.Field()
