#!/usr/bin/env python3

import scrapy


class CIKSpider(scrapy.Spider):
    name = "get_cik"

    def start_requests(self):
        urls = ['https://www.sec.gov/Archives/edgar/cik-lookup-data.txt']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'cik-lookup-data.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

