import scrapy
from scrapy.crawler import CrawlerProcess


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        #'http://quotes.toscrape.com/tag/humor/',
        'https://www.google.com/search?q=apple']

    def parse(self, response):
        for quote in response.css('div.ellip'):
            yield {
                'author': quote.xpath('span/text()').get()
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})

process.crawl(QuotesSpider)
process.start() # the script will block here until the crawling is finished
