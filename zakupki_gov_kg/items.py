# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class orderItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    
    internalId = scrapy.Field()
    orderId = scrapy.Field()
    organization = scrapy.Field()
    orderType = scrapy.Field()
    orderName = scrapy.Field()
    orderMethod = scrapy.Field()
    orderPubDate = scrapy.Field()
    claimsDeadline = scrapy.Field()
    
    address = scrapy.Field()
    phone = scrapy.Field()
    orderFormat = scrapy.Field()
    claimsValidity = scrapy.Field()
    automaticProlongation = scrapy.Field()
    guarantee = scrapy.Field()
    
    guaranteePercent = scrapy.Field()
    package = scrapy.Field()
    insurance = scrapy.Field()
    auxilaryServices = scrapy.Field()
    
    advancePayment = scrapy.Field()
    postShipment = scrapy.Field()
    postAcceptance = scrapy.Field()
    addConditions = scrapy.Field()
    paymentTerms = scrapy.Field()

class lotItem(scrapy.Item):
    orderId = scrapy.Field()
    
    lotId = scrapy.Field()
    lotName = scrapy.Field()
    lotSum = scrapy.Field()
    lotAddress = scrapy.Field()
    lotOKGZ = scrapy.Field()
    lotMeasure = scrapy.Field()
    lotUnits = scrapy.Field()
    lotSpecs = scrapy.Field()
    