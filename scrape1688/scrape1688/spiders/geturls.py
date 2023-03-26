import scrapy


class GeturlsSpider(scrapy.Spider):
    name = "geturls"
    Base_Url = "https://ukrparts.com.ua"
    def start_requests(self):
        url = "https://ukrparts.com.ua/category/tormoznie-diski/c-25/car/2719/"
        yield scrapy.Request(url, meta={'playwright': True})

    def parse(self, response):
        for offer in response.css('div.part_box'):
            offerurl = offer.css('div.part_name.pointer::attr(onclick)').get()

            offerurl = offerurl.replace("if (!window.__cfRLUnblockHandlers) return false; document.location.href = '", self.Base_Url).replace("'; return false;", "")
            yield {'url': offerurl}
