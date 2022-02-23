import scrapy
from scrapy_splash import SplashRequest

class QuotesPySpider(scrapy.Spider):
    name = 'quotes.py'
    allowed_domains = ['quotes.toscrape.com/js/']
    start_urls = ['http://quotes.toscrape.com/js/'] #'http://quotes.toscrape.com/js//'

    # Recommended template from Zyte's scrapy_splash tutorial. The reason is parse should be called with 
    # The HTML-rendered page. Calling 'start_requests' with that objective solves the problem
    def start_requests(self):
        yield SplashRequest(url=self.start_urls[0], callback=self.parse)

    
    def parse(self, response):
        quotes = response.css("div.quote")
        for quote in quotes:
            yield {
                'text': quote.css("span.text::text").extract_first(),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags a.tag::text").extract()
            }
