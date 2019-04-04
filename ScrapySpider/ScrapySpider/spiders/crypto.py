# # -*- coding: utf-8 -*-
# import scrapy
# from selenium import webdriver
# from scrapy.xlib.pydispatch import dispatcher
# from scrapy import signals
#
# class CryptoSpider(scrapy.Spider):
#     name = 'crypto'
#     allowed_domains = ['https://www.investing.com/crypto/bitcoin/btc-usd']
#     start_urls = ['https://www.investing.com/crypto/bitcoin/btc-usd/']
#
#
#
#     def __init__(self):
#         # from pyvirtualdisplay import Display
#         # display = Display(visible=0, size=(800, 600))
#         # display.start()
#         self.browser = webdriver.Chrome(
#             executable_path='/Users/changrongchen/Desktop/practice/scrapy/first-project/ScrapySpider/ScrapySpider/other/chromedriver')
#         super(CryptoSpider, self).__init__()
#         dispatcher.connect(self.spider_closed, signals.spider_closed)
#
#     def spider_closed(self, spider):
#         self.browser.quit()
#
#     def parse(self, response):
#         print(response.css('.candle-tooltip-container::text'))
#         print(response.css('.candle-heading::text').extract())
#         print(response.css('.candle-title::text').extract())
#         print(response.css('.candle-value::text').extract())
