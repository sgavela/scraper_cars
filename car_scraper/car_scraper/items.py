# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarScraperItem(scrapy.Item):
    marca_y_modelo = scrapy.Field()
    precio = scrapy.Field()
    provincia = scrapy.Field()
    combustible = scrapy.Field()
    cambio = scrapy.Field()
    matriculación = scrapy.Field()
    kilometros = scrapy.Field()
    potencia = scrapy.Field()
    pass
