# -*- coding: utf-8 -*-2

import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.http.request import Request
from scrapy.http import FormRequest
from zakupki_gov_kg.items import orderItem
import re

class zakupkiSpider(scrapy.Spider):
    name = "zakupki"
    allowed_domains = ["zakupki.gov.kg"]
    start_urls = ["https://zakupki.gov.kg/popp/"]
                
    def parse(self, response):
        
        # launch orders spider
        yield Request("https://zakupki.gov.kg/popp/view/order/list.xhtml", 
                      callback=self.launchOrdersSpider)
        
    def launchOrdersSpider(self, response):
        # extract data for eache row
        items = []
    
        rows = response.xpath('//table[@role="grid"]/tbody/tr')
        for i in range(len(rows)):
            item = orderItem()
            item['internalId'] = rows[i].xpath('@data-rk').extract()
            
            orderId = ''.join(rows[i].xpath('//table[@role="grid"]/tbody/tr[%s]/td[1]/text()' % i).extract())
            orderId =  re.sub('[\n ]', '', orderId)
            item['orderId'] = orderId.strip()
            
            organization = ''.join(rows[i].xpath('//table[@role="grid"]/tbody/tr[%s]/td[2]/a/text()' % i).extract())
            organization =  re.sub('[\n ]', '', organization)
            item['organization'] = organization.strip()
            
            orderType = ''.join(rows[i].xpath('//table[@role="grid"]/tbody/tr[%s]/td[3]/text()' % i).extract())
            orderType =  re.sub('[\n ]', '', orderType)
            item['orderType'] = orderType.strip()

            orderName = ''.join(rows[i].xpath('//table[@role="grid"]/tbody/tr[%s]/td[4]/text()' % i).extract())
            orderName =  re.sub('[\n ]', '', orderName)
            item['orderName'] = orderName.strip()

            orderMethod = ''.join(rows[i].xpath('//table[@role="grid"]/tbody/tr[%s]/td[5]/text()' % i).extract())
            orderMethod =  re.sub('[\n ]', '', orderMethod)
            item['orderMethod'] = orderMethod.strip()
            
            orderPubDate = ''.join(rows[i].xpath('//table[@role="grid"]/tbody/tr[%s]/td[6]/text()' % i).extract())
            orderPubDate =  re.sub('[\n ]', '', orderPubDate)
            item['orderPubDate'] = orderPubDate.strip()

            claimsDeadline = ''.join(rows[i].xpath('//table[@role="grid"]/tbody/tr[%s]/td[7]/text()' % i).extract())
            claimsDeadline =  re.sub('[\n ]', '', claimsDeadline)
            item['claimsDeadline'] = claimsDeadline.strip()
            
            # go into details of page
            detailsLink = 'https://zakupki.gov.kg/popp/view/order/view.xhtml?id=' +  ''.join(item['internalId']).strip()
            
            item = Request(detailsLink, 
                      callback=self.extractOrder, meta={'item':item})

            items.append(item)
        
        return items
        
    def extractOrder(self, response):
        item = response.meta['item']
        
        address = ''.join(response.xpath("//td[text()='%s']/following-sibling::td/text()"  % u"Фактический адрес".encode('windows-1251')).extract())
        address = re.sub('[\n ]', '', address)
        item['address'] = address.strip()
        
        phone = ''.join(response.xpath("//td/span[text()='%s']/sibling::td/text()" % u"Рабочий телефон").extract())
        phone = re.sub('[\n ]', '', phone)
        item['phone'] = phone.strip()

        orderFormat = ''.join(response.xpath("//td/span[text()='%s']/sibling::td/text()" % u"Формат закупок").extract())
        orderFormat = re.sub('[\n ]', '', orderFormat)
        item['orderFormat'] = orderFormat.strip()

        claimsValidity = ''.join(response.xpath("//td/span[text()='%s']/sibling::td/text()" % u"Срок действия конкурсных заявок").extract())
        claimsValidity = re.sub('[\n ]', '', claimsValidity)
        item['claimsValidity'] = claimsValidity.strip()

        automaticProlongation = ''.join(response.xpath("//td/span[text()='%s']/sibling::td/text()" % u"Автоматическое продление").extract())
        automaticProlongation = re.sub('[\n ]', '', automaticProlongation)
        item['automaticProlongation'] = automaticProlongation.strip()

        guarantee = ''.join(response.xpath("//td/span[text()='%s']/sibling::td/text()" % u"Гарантийное обеспечение").extract())
        guarantee = re.sub('[\n ]', '', guarantee)
        item['guarantee'] = guarantee.strip()
        
        guaranteePercent = ''.join(response.xpath("//td/span[text()='%s']/sibling::td/text()" % u"Гарантийное обеспечение исполнения договора").extract())
        guaranteePercent = re.sub('[\n ]', '', guaranteePercent)
        item['guaranteePercent'] = guaranteePercent.strip()
        
        package = ''.join(response.xpath("//td/span[text()='%s']/sibling::td/text()" % u"Упаковка").extract())
        package = re.sub('[\n ]', '', package)
        item['package'] = package.strip()

        insurance = ''.join(response.xpath("//td/span[text()='%s']/sibling::td/text()" % u"Страхование товара").extract())
        insurance = re.sub('[\n ]', '', insurance)
        item['insurance'] = insurance.strip()

        auxilaryServices = ''.join(response.xpath("//td/span[text()='%s']/sibling::td/text()" % u"Сопутствующие услуги").extract())
        auxilaryServices = re.sub('[\n ]', '', auxilaryServices)
        item['auxilaryServices'] = auxilaryServices.strip()

        advancePayment = ''.join(response.xpath("//td/span[text()='%s']/sibling::td/text()" % u"Авансовый платеж").extract())
        advancePayment = re.sub('[\n ]', '', advancePayment)
        item['advancePayment'] = advancePayment.strip()

        postShipment = ''.join(response.xpath("//td/span[text()='%s']/sibling::td/text()" % u"После отгрузки").extract())
        postShipment = re.sub('[\n ]', '', postShipment)
        item['postShipment'] = postShipment.strip()
        
        postAcceptance = ''.join(response.xpath("//td/span[text()='%s']/sibling::td/text()" % u"После приемки").extract())
        postAcceptance = re.sub('[\n ]', '', postAcceptance)
        item['postAcceptance'] = postAcceptance.strip()
        
        addConditions = ''.join(response.xpath("//td/span[text()='%s']/sibling::td/text()" % u"Дополнительные условия оплаты").extract())
        addConditions = re.sub('[\n ]', '', addConditions)
        item['addConditions'] = addConditions.strip()

        paymentTerms = ''.join(response.xpath("//td/span[text()='%s']/sibling::td/text()" % u"Срок оплаты").extract())
        paymentTerms = re.sub('[\n ]', '', paymentTerms)
        item['paymentTerms'] = paymentTerms.strip()

        return item