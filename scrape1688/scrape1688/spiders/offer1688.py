import scrapy


class Offer1688Spider(scrapy.Spider):
    name = "offer1688"
    def start_requests(self):
        url = "https://detail.1688.com/offer/650638064452.html?tracelog=p4p&spm=a26352.13672862.offerlist.26.5a741e62fzH8oM&clickid=a2ad2e47d1a341648b903f08aab45f7e&sessionid=ac80d7f38467e3e930befe989ec863c7&_p_isad=1"
        yield scrapy.Request(url, meta={'playwright': True})

    def parse(self, response):
        name = response.css('div.title-text::text').get()
        yield {'name': name}
