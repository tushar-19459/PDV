# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesSpider1Item(scrapy.Item):
    # define the fields for your item here like:
    h1 = scrapy.Field()
    tags = scrapy.Field()
    pass
