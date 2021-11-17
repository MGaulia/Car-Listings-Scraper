# -*- coding: utf-8 -*-
import scrapy


class AutopliusSpider(scrapy.Spider):
    name = 'autoplius'
    allowed_domains = ['autoplius.lt']
    start_urls = ['https://autoplius.lt/skelbimai/naudoti-automobiliai?page_nr=' + str(i) for i in range(1, 3)]
    # USE THIS FOR ALL PAGES start_urls = ['https://autoplius.lt/skelbimai/naudoti-automobiliai?page_nr=' + str(i) for i in range(1, 201)]

    def parse(self, response):
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

        #yield scrapy.Request("https://autoplius.lt/skelbimai/audi-a8-3-0-l-sedanas-2020-dyzelinas-17591653.html", callback=self.parsecar, meta={'download_timeout': 2}, headers = headers)
        for carlink in response.xpath('//a[@class="announcement-item"]/@href').extract():
            yield scrapy.Request(carlink, callback=self.parsecar, meta={'download_timeout': 2}, headers = headers)

    def parsecar(self, response):
        labels = [i.strip() for i in response.xpath('//div[@class="parameter-label"]//text()').extract()]
        values = [i.strip() for i in response.xpath('//div[@class="parameter-value "]//text()').extract()]


        cardict = {
            "link":response.url,
            "Pagaminimo data": "",
            "Rida": "",
            "Variklis": "",
            "Kuro tipas": "",
            "Kėbulo tipas": "",
            "Durų skaičius": "",
            "Varantieji ratai": "",
            "Pavarų dėžė": "",
            "Klimato valdymas": "",
            "Spalva": "",
            "Vairo padėtis": "",
            "Ratlankių skersmuo": "",
            "Nuosava masė, kg": "",
            "Sėdimų vietų skaičius": "",
            "Pirmosios registracijos šalis": "",
            "Kėbulo numeris (VIN)": "",
            "SDK": "",
            "Euro standartas": "",
            "CO₂ emisija, g/km": "",
            "Taršos mokestis": ""
        }
        for  label, value in zip(labels, values):
            cardict[label] = value
        yield cardict
