import scrapy


class MSpider(scrapy.Spider):
    name = "m"
    start_urls = ["https://service-workshopmanual.com/product-category/machine-vehicle-manuals/operation-owners-manuals/page/{}/".format(i) for i in range(1001, 1101)]

    def parse(self, response):
        for d in response.css('div.woocommerce-card__header'):
            url = d.css('a.woocommerce-LoopProduct-link::attr(href)').get()
            yield{
                'url': url
            }
