import scrapy
from myscrapy.items import MyscrapyItem


class ProxySpider(scrapy.Spider):
    name = 'ProxySpider'
    start_urls = ['https://www.kuaidaili.com/free/']

    def parse(self, response):
        tr_list = response.xpath('//*[@id="list"]/table/tbody/tr')
        for tr in tr_list:
            ip = tr.xpath('./td[1]/text()').extract_first()
            port = tr.xpath('./td[2]/text()').extract_first()
            typ = tr.xpath('./td[3]/text()').extract_first()
            protocal = tr.xpath('./td[4]/text()').extract_first()
            position = tr.xpath('./td[5]/text()').extract_first()

            item = MyscrapyItem()
            item['ip'] = ip
            item['port'] = port
            item['typ'] = typ
            item['protocal'] = protocal
            item['position'] = position
            # print(item)
            yield item

