# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SpiderproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    catename = scrapy.Field()
    request_time = scrapy.Field(serializer=str)

class MyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    job_label = scrapy.Field()
    addr = scrapy.Field()
    time = scrapy.Field()
    info = scrapy.Field()

class YGItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    lv_title = scrapy.Field()
    lv_img_url = scrapy.Field()
    lv_content = scrapy.Field()