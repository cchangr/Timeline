# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from ScrapySpider.items import InvestingCryptoItem
from scrapy_splash import SplashRequest

script =  '''
function main(splash, args)
  splash.images_enabled = false
  splash: set_viewport_size(1028, 2000)
  assert(splash:go(args.url))
  splash:evaljs("$('.candlesIcon').click(); $('#js_instrument_chart_wrapper > div.chartBarWrap > ul.float_lang_base_1.fchart-switches.fchart-switches-timeframes.round-items > li:nth-child(1) > a').click(); document.documentElement.scrollTop=800")
  splash.scroll_position = {613, 347}
  splash:wait(5)
  splash:mouse_hover(612, 613)
  splash:wait(5)
  return splash:html()
end
'''



class InvestingSpider(scrapy.Spider):
    name = 'investing'
    # allowed_domains = ['https://www.investing.com/']
    start_urls = ['https://www.investing.com/crypto/bitcoin/btc-usd/']

    def start_requests(self):
        for url in self.start_urls:
            # 通过SplashRequest请求等待1秒
            yield SplashRequest(url, callback=self.parse, endpoint='execute', args={'lua_source': script, 'wait': 1})

    def parse(self, response):
        crypto_name = 'BTC-USD'
        price_list = response.css('.candle-value::text').extract()
        # print(response.css('#js_instrument_chart_wrapper').extract())
        print(response.css('.candle-heading').extract())
        print(response.css('.candle-title').extract())
        # print(response.css('.candlesIcon').extract())
        print(price_list)
        # with open("imageToSave.png", "wb") as fh:
        #     fh.write(response.body)
        #
        # print(response.body)
