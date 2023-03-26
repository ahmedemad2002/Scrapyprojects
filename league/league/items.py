# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LeagueItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class MatchItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Date = scrapy.Field()
    time = scrapy.Field()
    Away = scrapy.Field()
    Home = scrapy.Field()
    Division = scrapy.Field()
    Tier = scrapy.Field()
    Venue = scrapy.Field()
    Address = scrapy.Field()
    