# -*- coding: utf-8 -*-
import scrapy


class AutopliusSpider(scrapy.Spider):
    name = 'autoplius'
    allowed_domains = ['autoplius.lt']
    start_urls = ['https://autoplius.lt/skelbimai/naudoti-automobiliai?page_nr=' + str(i) for i in range(1, 3)]
    # USE THIS FOR ALL PAGES start_urls = ['https://autoplius.lt/skelbimai/naudoti-automobiliai?page_nr=' + str(i) for i in range(1, 201)]

    def parse(self, response):
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for carlink in response.xpath('//a[@class="announcement-item"]/@href').extract():
            yield scrapy.Request(carlink, callback=self.parsecar, meta={'download_timeout': 2}, headers = headers)

    def parsecar(self, response):
        labels = [i.strip() for i in response.xpath('//div[@class="parameter-label"]//text()').extract()]
        values = [i.strip() for i in response.xpath('//div[@class="parameter-value "]//text()').extract()]
        cardict = {}
        for  label, value in zip(labels, values):
            cardict[label] = value
        yield cardict
