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
            "Pagaminimo data": None,
            "Rida": None,
            "Variklis": None,
            "Kuro tipas": None,
            "Kėbulo tipas": None,
            "Durų skaičius": None,
            "Varantieji ratai": None,
            "Pavarų dėžė": None,
            "Klimato valdymas": None,
            "Spalva": None,
            "Vairo padėtis": None,
            "Ratlankių skersmuo": None,
            "Nuosava masė, kg": None,
            "Sėdimų vietų skaičius": None,
            "Pirmosios registracijos šalis": None,
            "Kėbulo numeris (VIN)": None,
            "SDK": None,
            "Euro standartas": None,
            "CO₂ emisija, g/km": None,
            "Taršos mokestis": None
        }
        for  label, value in zip(labels, values):
            cardict[label] = value
        yield cardict
