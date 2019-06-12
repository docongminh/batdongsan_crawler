import scrapy


class QuotesSpider(scrapy.Spider):
    name = "bds"

    def start_requests(self):
        urls = [
            'https://batdongsan.com.vn/nha-dat-ban',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for item in response.css('.search-productItem'):
            yield{
                    'title': item.css('h3 a::attr(title)').extract_first(),
                    'body': item.css('.p-main-text::text').extract_first(),
                    'price': item.css('.product-price::text').extract_first(),
                    'area': item.css('.product-area::text').extract_first(),
                    'city': item.css('.product-city-dist::text').extract_first(),
                    'date': item.css('.mar-right-10::text').extract_first()
                    }
        controller = response.css('.background-pager-controls').css('.background-pager-right-controls').css('a')
        next_page = controller[-2].css('::attr(href)').extract_first()
        button_content = controller[-2].css('::text').extract_first() # it must be ...
        if next_page is not None and button_content == '...':
            yield response.follow(next_page, callback=self.parse)



    def parse_old(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

##    def parse(self, response):
##        for quote in response.css('div.quote'):
##            yield{
##                    'text': quote.css('span.text::text').extract_first(),
##                    'author': quote.css('small.author::text').extract_first()
##                    }
##        next_page = response.css('li.next a::attr(href)').extract_first()
##        if next_page is not None:
##            yield response.follow(next_page, callback=self.parse)	
