import scrapy
import json
data = json.load(open('/home/user/scrapyprojects/entrepreneur/fullurls.json', 'r'))

class BusinessSpider(scrapy.Spider):
    name = "business"
    start_urls = [data[i]['url'] for i in range(len(data))]

    def parse(self, response):
        name = response.css('h1.font-black::text').get().replace('\t', '').replace('\n', '')
        url = response.url
        social_links = response.css('dl:contains("Social")').css('dd a::attr(href)').getall()
        units_2022 = response.css('dl:contains("Units as of 2022")').css('dd span::text').get().replace('\t', '').replace('\n', '')
        rank_2023 = eval(response.css('div#franchiseRank::attr(data-chartdata)').get())[-1]['rank']
        try:
           rank_2022 = eval(response.css('div#franchiseRank::attr(data-chartdata)').get())[-2]['rank']
        except:
            rank_2022 = None
        yield{
            'Business Name': name,
            'Home page': url,
            'Social Links': social_links,
            'Units as of 2022': units_2022,
            '2023 Rank': rank_2023,
            '2022 Rank': rank_2022
        }