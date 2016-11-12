# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BlogScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # create a class that models what it is what we want to  capture
    #in scrapy create a model of data to be scraped
    title = scrapy.Field()
    link = scrapy.Field()