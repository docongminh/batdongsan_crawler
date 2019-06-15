
import scrapy
from bs4 import BeautifulSoup
from scrapy_splash import SplashRequest
import re

class BdsDetailSpider(scrapy.Spider):
    name = "bdsdetail"

    def start_requests(self):
        urls = [
            #'https://batdongsan.com.vn/nha-dat-ban',
            'https://batdongsan.com.vn/ban-can-ho-chung-cu',
            # 'https://batdongsan.com.vn/ban-nha-rieng',
            # 'https://batdongsan.com.vn/ban-nha-biet-thu-lien-ke',
            # 'https://batdongsan.com.vn/ban-nha-mat-pho',
            # 'https://batdongsan.com.vn/ban-dat-nen-du-an',
            # 'https://batdongsan.com.vn/ban-dat-nen-du-an',
            # 'https://batdongsan.com.vn/ban-dat',
            # 'https://batdongsan.com.vn/ban-trang-trai-khu-nghi-duong',
            # 'https://batdongsan.com.vn/ban-kho-nha-xuong',
            # 'https://batdongsan.com.vn/ban-loai-bat-dong-san-khac',

        ]
        script = """
        function main(splash)
            local url = splash.args.url
            assert(splash:go(url))
            assert(splash:wait(0.5))
            assert(splash:runjs("$('.next')[0].click();"))
            return {
                html = splash:html(),
                url = splash:url(),
            }
        end
        """
        for url in urls:
            yield SplashRequest(url=url, endpoint = "render.html", callback=self.parse)
    
    def parse_detail(self, response):
        """
            parse detail in each item
        """

        body_detail = response.css('.pm-content').css('.pm-desc').extract_first()
        body_detail = BeautifulSoup(body_detail, 'lxml').text
        customerInfo = response.css('#divCustomerInfo')
        name = customerInfo.css('#LeftMainContent__productDetail_contactName').css('.right::text').extract_first()
        address = customerInfo.css('#LeftMainContent__productDetail_contactAddress').css('.right::text').extract_first()
        phone = customerInfo.css('#LeftMainContent__productDetail_contactPhone').css('.right::text').extract_first()
        mobile = customerInfo.css('#LeftMainContent__productDetail_contactMobile').css('.right::text').extract_first()
        
        feature = response.css('.div-table').css('.table-detail').css('.row').css('.right::text').extract()
        type_of_ads = feature[0]

        date_post = response.xpath('//*[@id="product-detail"]/div[9]/div[3]/text()').extract()
        # print(date_post, "date_post")
        date_expiration = response.xpath('//*[@id="product-detail"]/div[9]/div[4]/text()').extract()
        # print(date_expiration, "date_expiration")
       
        count_persion_post = response.xpath('//*[@id="LeftMainContent__productDetail_footer"]/div[2]/div/div[2]/div[2]/a/text()').extract()
        
        if not count_persion_post:
            number_persion = '0'
        else:
            first_idx = count_persion_post[0].find('(')
            last_idx = count_persion_post[0].find(')')
            number_persion = count_persion_post[0][first_idx+1:last_idx]
        # print(number_persion, "====================")

        #javascript protected 
        # email = customerInfo.xpath('//*[@id="contactEmail"]/div[2]/a/text()').extract()
        email = response.css('.divCustomerInfo').css('.right').css('a::attr(href)').extract_first()
        # print(email, "===========")

        item = response.request.meta['item']
        item['bodyDetail'] = body_detail.strip()
        item['type'] = type_of_ads.strip()

        if date_post :
            item['date_post'] = " ".join(re.findall(r"[a-zA-Z0-9]+", date_post[1]))

        elif not date_post :
            item['date_post'] = "No Date Post"

        if date_expiration:
            item['date_expiration'] = " ".join(re.findall(r"[a-zA-Z0-9]+", date_expiration[1]))
        elif  not date_expiration:
            item['date_expiration'] = "No Date Expiration"
        # item['more_info'] = date_post_expiration

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

        if number_persion:
            item['persion_post'] = number_persion




        yield item # full item


    def parse(self, response):
        """
        
        """    
        link_duplicate = []
        for item in response.css('.search-productItem'):
            
            link = item.css('h3 a::attr(href)').extract_first()
            if link not in link_duplicate:
                link_duplicate.append(link)
                itemCrawl = {
                        'title': item.css('h3 a::attr(title)').extract_first(),
                        'link': 'https://batdongsan.com.vn' + link,    
                        'body': item.css('.p-main-text::text').extract_first(),
                        'price': item.css('.product-price::text').extract_first(),
                        'area': item.css('.product-area::text').extract_first(),
                        'city': re.sub(r"(\r\n+)", '', item.css('.product-city-dist::text').extract_first()),
                        # 'date': item.css('.mar-right-10::text').extract_first()
                        }

                yield response.follow(link, callback=self.parse_detail,
                        meta={'item':itemCrawl}) # pass itemCrawl here to get more detail

        controller = response.css('.background-pager-right-controls').css('a')
        #print(controller, "controller")
        next_page = controller[-2].css('::attr(href)').extract_first()
        # print(next_page, "next_page")
        button_content = controller[-2].css('::text').extract_first() # it must be ...
        # print(button_content, "button_content")
        if next_page is not None and button_content == '...':
            yield response.follow(next_page, callback=self.parse)


