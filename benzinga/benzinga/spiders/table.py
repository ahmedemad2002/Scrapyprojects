import scrapy
import json
from benzinga.items import BenzingaItem

class tableSpider(scrapy.Spider):
    name = "table"
    start_urls = ["https://www.benzinga.com/"]

    headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://www.benzinga.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }

    def parse(self, response):
        url = 'https://api.benzinga.com/api/v2.1/calendar/dividends?token=1c2735820e984715bc4081264135cb90&parameters[date_from]=2023-03-22&parameters[date_to]=2023-03-25&parameters[date_sort]=ex&pagesize=1000'

        request = scrapy.Request(url,
            callback=self.parse_scores,
            headers=self.headers)
        yield request
    
    def parse_scores(self, response):

        raw_data = response.body
        data= json.loads(raw_data)
        data = data['dividends']
        print(type(data))
        #yield{'type': type(data), 'keys': data.keys(), 'items': data.items()}
        for obj in data:
            o = BenzingaItem()
            o['Ex_date'] = obj['ex_dividend_date']
            o['Ticker'] = obj['ticker']
            o['Company'] = obj['name']
            o['Payment_per_year'] = obj['frequency']
            o['Dividend'] = obj['dividend']
            o['Yield'] = obj['dividend_yield']
            o['Announced'] = obj['date']
            o['Record'] = obj['record_date']
            o['Payable'] = obj['payable_date']
            yield o
            


