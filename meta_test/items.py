import scrapy

class MyItem(scrapy.Item):
    main_url = scrapy.Field()
    other_url = scrapy.Field()

