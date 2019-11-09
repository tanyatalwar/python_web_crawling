# -*- coding: utf-8 -*-
import scrapy


class W3spiderSpider(scrapy.Spider):
    name = 'w3spider'
    allowed_domains = ['https://www.w3schools.com']
    start_urls = ['https://www.w3schools.com/']

    def parse(self, response):
        links = response.xpath("//a/@href").extract()
        row_data=zip(links)
        for item in row_data:
            scraped_info = {
                #key:value
                'page':response.url,
                'links' : item[0],
            }
            yield scraped_info
