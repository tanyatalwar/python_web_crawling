# -*- coding: utf-8 -*-
import scrapy


class AliexpressTabletsSpider(scrapy.Spider):
    name = 'aliexpress_tablets' #name here indicate name of the spider
    allowed_domains = ['https://www.hackerrank.com/'] #allow domains  that are allowed to crawl this indicate the domain of the website
    start_urls = ['https://www.hackerrank.com','https://www.hackerrank.com/?utm_expid=.2u09ecQTSny1HV02SEVoCg.0&utm_referrer=']

    def parse(self, response):
        print("procesing:"+response.url)
        #Extract data using css selectors
        product_name=response.css('.menu-item__description::text').extract()
        #product_name = response.xpath("//li/text()")
        # price_range=response.css('.value::text').extract()
        # #Extract data using xpath
        # orders=response.xpath("//em[@title='Total Orders']/text()").extract()
        # company_name=response.xpath("//a[@class='store $p4pLog']/text()").extract()
        #
        row_data=zip(product_name)
        #
        # #Making extracted data row wise
        for item in row_data:
        #     #create a dictionary to store the scraped info
             scraped_info = {
                 #key:value
                 'page':response.url,
                 'product_name' : item[0], #item[0] means product in the list and so on, index tells what value to assign
        #         'price_range' : item[1],
        #         'orders' : item[2],
        #         'company_name' : item[3],
             }
        #
        #     #yield or give the scraped info to scrapy
             yield scraped_info
