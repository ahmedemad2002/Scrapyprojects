import scrapy


class GetItemsSpider(scrapy.Spider):
    name = "get_items"
    BASE_URL = 'https://www.entrepreneur.com'
    start_urls = ["https://www.entrepreneur.com/franchises/directory/franchise500-ranking/page-{}".format(i) for i in range(1, 11)]

    def parse(self, response):
        items = response.css('tr.border-b')
        for item in items:
            url = item.css('a::attr(href)').get()
            yield {'url': self.BASE_URL + url}
