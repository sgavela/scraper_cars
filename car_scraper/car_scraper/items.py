# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarScraperItem(scrapy.Item):
    brand_and_model = scrapy.Field()
    price = scrapy.Field()
    province = scrapy.Field()
    fuel = scrapy.Field()
    gear = scrapy.Field()
    matriculation = scrapy.Field()
    kilometres = scrapy.Field()
    power = scrapy.Field()
    pass
