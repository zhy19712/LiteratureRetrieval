from scrapy import Request

from wechat.items import WechatItem
# from wechat.free_ip import get_random_proxy
from wechat.get_cookies import get_new_headers
import scrapy
import time
import random


class SougouSearchSpider(scrapy.Spider):
    name = 'wechat'
    # allowed_domains = ['www.sogou.com']
    start_urls = ['https://weixin.sogou.com/weixin?type=1&s_from=input&query=三峡e家&ie=utf8&_sug_=n&_sug_type_=n']

    # def start_requests(self):
    #     headers = get_new_headers()
    #     for url in self.start_urls:
    #         # 获取代理IP
    #         yield scrapy.Request(url=url,
    #                              callback=self.parse,
    #                              headers=headers)
    def parse(self, response):
        try:
            article_url = response.xpath('//*[@id="sogou_vr_11002301_box_0"]/dl[3]/dd/a/@href').extract()
        except:
            print("error")
        else:
            print(article_url)
            yield Request(article_url, callback=self.parse)  # 递归调用

    # def parse(self, response):
    #     headers_new = get_new_headers()
    #     cookies_new = get_new_cookies()
    #     # 获取当前页码
    #     current_page = int(response.xpath('//div[@id="pagebar_container"]/span/text()').extract_first())
    #     # 解析当前页面
    #     for i, a in enumerate(response.xpath('//div[contains(@class,"vrwrap")]/h3[@class="vrTitle"]/a')):
    #         # 获取标题，去除空格和换行符
    #         title = ''.join(a.xpath('./em/text() | ./text()').extract()).replace(' ', '').replace('\n', '')
    #         if title:
    #             item = WechatItem()
    #             # 获取访问链接（①非跳转链接②跳转链接）、页码、行数、标题
    #             if a.xpath('@href').extract_first().startswith('/link'):
    #                 item['visit_url'] = 'www.sogou.com' + a.xpath('@href').extract_first()  # 提取链接
    #             else:
    #                 item['visit_url'] = a.xpath('@href').extract_first()
    #             item['page'] = current_page
    #             item['rank'] = i + 1
    #             item['title'] = title
    #             yield item
    #     # 控制爬取频率
    #     time.sleep(random.randint(8, 10))
    #     # 获取“下一页”的链接
    #     p = response.xpath('//div[@id="pagebar_container"]/a[@id="sogou_next"]')
    #     if p:
    #         p_url = 'https://www.sogou.com/web' + str(p.xpath('@href').extract_first())
    #         proxy = 'http://' + str(get_random_proxy())
    #         yield scrapy.Request(url=p_url,
    #                              callback=self.parse,
    #                              headers=headers_new,
    #                              cookies=cookies_new,
    #                              meta={'http_proxy': proxy})