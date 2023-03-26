import scrapy
import json
import time
from league.items import MatchItem
from scrapy_playwright.page import PageMethod


class RecordsSpider(scrapy.Spider):
    name = "records"


    def start_requests(self):
        url = "https://league.winloseortie.com/NYHL/schedule"
        # storage_state = {
        #     'schedStandDateFrom': '2023-1-1'
        # }
        # storage_state_json = json.dumps(storage_state)
        # headers = {
        #     'Content-Type': 'application/json'
        # }
        # cookies = {
        #     '_gid': 'GA1.2.1640709671.1678645736',
        #     '_ga': 'GA1.2.1005267715.1678645736',
        #     'JSESSIONID': 'E2061721EE0C2DDC8D32B081DB8557D0'
        # }

        yield scrapy.Request(url, meta=dict(
                playwright = True,
                playwright_include_page = True,
                # headers=headers,
                # cookies=cookies,
                # storage_state=storage_state_json,
                playwright_page_methods =[
                    PageMethod('wait_for_selector', 'tr.ng-scope'),
                    PageMethod('select_option', selector='select#season-opt', value="501"),
                    PageMethod('fill', 'div#fromDate input.form-control', ''),
                    PageMethod('click', 'div#fromDate input.form-control'),
                    PageMethod('type', 'div#fromDate input.form-control', '01 January 2023'),
                    
                    # PageMethod('screenshot', path='SH1.png', full_page=True),
                    #PageMethod('press', 'div#fromDate input.form-control', "Escape"),
                    # PageMethod('screenshot', path='SH2.png', full_page=True),
                    # PageMethod('fill', 'div#toDate input.form-control', ''),
                    # PageMethod('click', 'div#toDate input.form-control'),
                    # PageMethod('type', 'div#toDate input.form-control', '01 April 2023'),
                    PageMethod('wait_for_timeout', 3000)
                    #PageMethod('press', 'div#fromDate input', "Enter")
                ],
                errback=self.errback,
            ))

    # def parse(self, response):
    #     for record in response.css('tr.ng-scope'):
    #         name = record.css('td.ng-binding::text').get()
    #         yield record

    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.close()

        # await page.locator('#season-opt').select_option(label="Winter Season 2023")
        # await page.locator('#fromDate input').fill('')
        # await page.locator('#fromDate input').type('01 January 2023')
        # await page.locator('#fromDate input').blur()
        # time.sleep(4)
        # screenshot = await page.screenshot(path='SH1.png', full_page=True)
        # await page.get_by_text('Next').click()
        # time.sleep(2)

        # for i in range(5):
        for record in response.css('tr.ng-scope'):
            recorditem = MatchItem()
            recorditem['date'] = record.css('td.ng-binding::text').getall()[0]
            recorditem['time'] = record.css('td.ng-binding::text').getall()[1]
            recorditem['away'] = record.css('a.ng-binding::text').getall()[1].replace("\n", "").strip()
            recorditem['score'] = record.css('td.ng-binding::text').getall()[3].replace("\n", "").strip()
            # recorditem['home'] = record.css('a.ng-binding::text').getall()[3].replace("\n", "").strip()
            # recorditem['home'] = record.xpath('//a[@ng-click="clickTeamName(gameWebModel.home)"]/text()').getall()
            recorditem['home'] = record.css('a.ng-binding::text').getall()[4].replace("\n", "").strip()
            recorditem['division'] = record.css('td.ng-binding::text').getall()[4].replace("\n", "").strip()
            recorditem['tier'] = record.css('td.ng-binding span.ng-binding::text').get().replace("\n", "").strip()
            recorditem['venue'] = record.css('td a.ng-binding::text').getall()[1].replace("\n", "").strip()
            yield recorditem
        # await page.get_by_text('Next').click()
        # time.sleep(2)
        
        
        # screenshot = await page.screenshot(path='SH3.png', full_page=True)
        
        
  
    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()