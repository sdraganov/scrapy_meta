import scrapy
from meta_test.items import MyItem

class QuotesSpider(scrapy.Spider):
    name = "meta"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        item = MyItem()
        print("----------------------------------PARSE----------------------------------")
        item['main_url'] = response.url
        print('----------------------------------PARSE > MY ITEM: %s ----------------------------------' %item['main_url'])

        my_request = scrapy.Request("http://quotes.toscrape.com/page/2/", callback=self.parse_page2)
        my_request.meta['item'] = item
        yield my_request

    def parse_page2(self,response):
        print("----------------------------------PARSE PAGE2----------------------------------")
        item = response.meta['item']
        item['other_url'] = response.url
        print('----------------------------------PARSE PAGE2:MY ITEM: %s ----------------------------------' % item['main_url'])
        print('----------------------------------PARSE PAGE2:MY OTHER ITEM: %s ----------------------------------' % item['other_url'])
        yield item