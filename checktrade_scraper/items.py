# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class ChecktradeScraperItem(scrapy.Item):
    company_name = Field()
    unique_name = Field()
    email = Field()
    mobile_phone = Field()
    landline_phone = Field()
    cat_label = Field()
    postal_code = Field()
    response_url = Field()

