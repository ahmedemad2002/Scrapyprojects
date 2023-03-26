import scrapy
import json
from league.items import MatchItem

class ScoresapiSpider(scrapy.Spider):
    name = "scoresapi"
    start_urls = ["https://league.winloseortie.com/NYHL/schedule"]

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': '_ga=GA1.2.1005267715.1678645736; JSESSIONID=AEF4ECFBA5E150760B4753636736EA17',
        'Host': 'league.winloseortie.com',
        'Pragma': 'no-cache',
        'Referer': 'https://league.winloseortie.com/NYHL/schedule',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
        'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows"
    }

    def parse(self, response):
        url = 'https://league.winloseortie.com/json/schedule-game-list-date-range?dateFrom=2022-1-1&dateTo=2023-4-1&leagueId=127&seasonId=489&divisionId=-2&tierId=-1&teamName=&venueName=&offset=0&limit=2500'

        request = scrapy.Request(url,
            callback=self.parse_scores,
            headers=self.headers)
        yield request
    
    def parse_scores(self, response):

        raw_data = response.body
        data= json.loads(raw_data)
        matches = data["tierGameWebModels"]["gameWebModels"]
        n_matches = len(matches)
        for match in matches:
            m = MatchItem()
            m['Date'] = match['date']
            m['time'] = match['time']
            m['Away'] = match['away']
            
            m['Home'] = match['home']
            m['Division'] = match['divisionName']
            m['Tier'] = match['tierName']
            m['Venue'] = match['arena']['name']
            m['Address'] = match['arena']['streetAddress']
            yield m
            


