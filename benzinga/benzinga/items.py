# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BenzingaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Ex_date = scrapy.Field()
    Ticker = scrapy.Field()
    Company = scrapy.Field()
    Payment_per_year = scrapy.Field()
    Dividend = scrapy.Field()
    Yield = scrapy.Field()
    Announced = scrapy.Field()
    Record = scrapy.Field()
    Payable = scrapy.Field()
