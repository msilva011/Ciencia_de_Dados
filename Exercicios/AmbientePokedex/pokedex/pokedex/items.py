import scrapy

class PokemonItem(scrapy.Item):
    number = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    types = scrapy.Field()
    abilities = scrapy.Field()
    evolutions = scrapy.Field()
