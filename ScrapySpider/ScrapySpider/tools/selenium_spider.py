from selenium import webdriver
from scrapy.selector import Selector
import os


browser = webdriver.Chrome(executable_path='/Users/changrongchen/Desktop/practice/scrapy/first-project/ScrapySpider/ScrapySpider/other/chromedriver')

url = """
        https://finance.yahoo.com/quote/BTC-USD/chart?p=BTC-USD#eyJpbnRlcnZhbCI6MSwicGVyaW9kaWNpdHkiOjEsInRpbWVVbml0IjoibWludXRlIiwiY2FuZGxlV2lkdGgiOjUuNTExMzYzNjM2MzYzNjM3LCJ2b2x1bWVVbmRlcmxheSI6dHJ1ZSwiYWRqIjp0cnVlLCJjcm9zc2hhaXIiOnRydWUsImNoYXJ0VHlwZSI6ImxpbmUiLCJleHRlbmRlZCI6ZmFsc2UsIm1hcmtldFNlc3Npb25zIjp7fSwiYWdncmVnYXRpb25UeXBlIjoib2hsYyIsImNoYXJ0U2NhbGUiOiJsaW5lYXIiLCJwYW5lbHMiOnsiY2hhcnQiOnsicGVyY2VudCI6MSwiZGlzcGxheSI6IkJUQy1VU0QiLCJjaGFydE5hbWUiOiJjaGFydCIsInRvcCI6MH19LCJzZXRTcGFuIjp7fSwibGluZVdpZHRoIjoyLCJzdHJpcGVkQmFja2dyb3VkIjp0cnVlLCJldmVudHMiOnRydWUsImNvbG9yIjoiIzAwODFmMiIsImV2ZW50TWFwIjp7ImNvcnBvcmF0ZSI6eyJkaXZzIjp0cnVlLCJzcGxpdHMiOnRydWV9LCJzaWdEZXYiOnt9fSwic3ltYm9scyI6W3sic3ltYm9sIjoiQlRDLVVTRCIsInN5bWJvbE9iamVjdCI6eyJzeW1ib2wiOiJCVEMtVVNEIn0sInBlcmlvZGljaXR5IjoxLCJpbnRlcnZhbCI6MSwidGltZVVuaXQiOiJtaW51dGUiLCJzZXRTcGFuIjp7fX1dLCJzdHVkaWVzIjp7InZvbCB1bmRyIjp7InR5cGUiOiJ2b2wgdW5kciIsImlucHV0cyI6eyJpZCI6InZvbCB1bmRyIiwiZGlzcGxheSI6InZvbCB1bmRyIn0sIm91dHB1dHMiOnsiVXAgVm9sdW1lIjoiIzAwYjA2MSIsIkRvd24gVm9sdW1lIjoiI0ZGMzMzQSJ9LCJwYW5lbCI6ImNoYXJ0IiwicGFyYW1ldGVycyI6eyJ3aWR0aEZhY3RvciI6MC40NSwiY2hhcnROYW1lIjoiY2hhcnQifX19LCJjdXN0b21SYW5nZSI6bnVsbCwicmFuZ2UiOnt9fQ%3D%3D
     """

url1 = 'https://www.investing.com/crypto/bitcoin/btc-usd'

browser.get(url1)
while True:

    # print(browser.page_source)
    t_selector = Selector(text=browser.page_source)

    # print(t_selector.css("#Open"))
    # print(t_selector.css('#High'))
    # print(t_selector.css('#Low'))
    # print(t_selector.css('#Close'))
    # print(t_selector.css('#Volume'))
    # print(t_selector.css('#Percent'))
    print(t_selector.css('.candle-tooltip-container::text'))
    print(t_selector.css('.candle-heading::text').extract())
    print(t_selector.css('.candle-title::text').extract())
    print(t_selector.css('.candle-value::text').extract())

    # print(t_selector.css('.stx-field-value::text').extract() )
    # print(t_selector.css('.stx-float-date::text').extract())
    # print(t_selector.css('#floatDate::text').extract())