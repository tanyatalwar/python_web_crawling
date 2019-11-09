# -*- coding: utf-8 -*-
import scrapy


class BiomentorsSpider(scrapy.Spider):
    name = 'biomentors'
    allowed_domains = ['https://www.biomentors.online']
    start_urls = ['https://www.biomentors.online']

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
