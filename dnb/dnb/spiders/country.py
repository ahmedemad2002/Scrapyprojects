import scrapy
from scrapy_playwright.page import PageMethod


class CountriesSpider(scrapy.Spider):
    name = "country"

    start_urls = ["https://www.google.com/"]
    headers = {
        'authority': 'www.dnb.com',
        'method': 'GET',
        'path': '/business-directory/industry-analysis.public_administration.html',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
        "Connection": "keep-alive"
        }


    def parse(self, response):
        url = 'https://www.dnb.com/business-directory/company-information.public_administration.us.html?page=1'

        request = scrapy.Request(url,
            callback=self.parse_urls,
            headers=self.headers,
            meta=dict(
            playwright = True,
            playwright_include_page = True, 
            playwright_page_methods =[
                PageMethod('wait_for_selector', 'div.col-md-2')
                ],
            )
        )
        yield request
    
    
    
    def parse_urls(self, response):
        if response is not None:
            yield{'res': 'not null',
                  'body': response}
        else:
            yield{'res': None}
        for d in response.css('div.col-md-6'):
            c_name = d.css('a::text').get().replace('\n', '').strip()
            url = d.css('a::attr(href)').get()
            yield{
                "name": c_name,
                "url": url
            }

