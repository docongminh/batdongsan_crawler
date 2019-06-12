
import scrapy
from bs4 import BeautifulSoup


class BdsDetailSpider(scrapy.Spider):
    name = "bdsdetail"

    def start_requests(self):
        urls = [
            #'https://batdongsan.com.vn/nha-dat-ban',
            'https://batdongsan.com.vn/ban-can-ho-chung-cu',
            'https://batdongsan.com.vn/ban-nha-rieng',
            'https://batdongsan.com.vn/ban-nha-biet-thu-lien-ke',
            'https://batdongsan.com.vn/ban-nha-mat-pho',
            'https://batdongsan.com.vn/ban-dat-nen-du-an',
            'https://batdongsan.com.vn/ban-dat-nen-du-an',
            'https://batdongsan.com.vn/ban-dat',
            'https://batdongsan.com.vn/ban-trang-trai-khu-nghi-duong',
            'https://batdongsan.com.vn/ban-kho-nha-xuong',
            'https://batdongsan.com.vn/ban-loai-bat-dong-san-khac',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse_detail(self, response):
        body_detail = response.css('.pm-content').css('.pm-desc').extract_first()
        body_detail = BeautifulSoup(body_detail, 'lxml').text
        customerInfo = response.css('#divCustomerInfo')
        name = customerInfo.css('#LeftMainContent__productDetail_contactName').css('.right::text').extract_first()
        address = customerInfo.css('#LeftMainContent__productDetail_contactAddress').css('.right::text').extract_first()
        phone = customerInfo.css('#LeftMainContent__productDetail_contactPhone').css('.right::text').extract_first()
        mobile = customerInfo.css('#LeftMainContent__productDetail_contactMobile').css('.right::text').extract_first()
        
        feature = response.css('.div-table').css('.table-detail').css('.row').css('.right::text').extract()
        type_of_ads = feature[0]

        #javascript protected 
        email = customerInfo.css('#contactEmail').css('.right::text').extract_first()

        item = response.request.meta['item']
        item['bodyDetail'] = body_detail.strip()
        item['type'] = type_of_ads.strip()
        if name is not None:
            item['contactName'] = name.strip()
        if address is not None:
            item['address'] = address.strip()
        if phone is not None:
            item['phone'] = phone.strip()
        if mobile is not None:
            item['mobile'] = mobile.strip()
        if mobile is not None:
            item['email'] = email

        yield item # full item


    def parse(self, response):
        for item in response.css('.search-productItem'):
            link = item.css('h3 a::attr(href)').extract_first()
            itemCrawl = {
                    'title': item.css('h3 a::attr(title)').extract_first(),
                    'link': link,    
                    'body': item.css('.p-main-text::text').extract_first(),
                    'price': item.css('.product-price::text').extract_first(),
                    'area': item.css('.product-area::text').extract_first(),
                    'city': item.css('.product-city-dist::text').extract_first(),
                    'date': item.css('.mar-right-10::text').extract_first()
                    }

            yield response.follow(link, callback=self.parse_detail,
                    meta={'item':itemCrawl}) # pass itemCrawl here to get more detail

        controller = response.css('.background-pager-controls').css('.background-pager-right-controls').css('a')
        next_page = controller[-2].css('::attr(href)').extract_first()
        button_content = controller[-2].css('::text').extract_first() # it must be ...
        if next_page is not None and button_content == '...':
            yield response.follow(next_page, callback=self.parse)


