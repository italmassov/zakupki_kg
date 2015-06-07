# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 14:34:18 2015

@author: ALAITALMK
"""

import scrapy
from scrapy.utils.response import open_in_browser


class zakupkiSpider(scrapy.Spider):
    name = "zakupki"
    allowed_domains = ["zakupki.gov.kg"]
    start_urls = ["https://zakupki.gov.kg/popp/"]
                
    def parse(self, response):
        open_in_browser(response)