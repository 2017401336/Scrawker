import scrapy

from SpiderPro.items import YGItem


class YangguangSpider(scrapy.Spider):
    name = 'yangguang'
    # allowed_domains = ['www.iygw.cn/html/chanjing/lvyou/']
    start_urls = ['http://www.iygw.cn/html/chanjing/lvyou//']

    def parse(self, response):
        li_list = response.xpath('//div[@class="let_nrpic"]/ul/li')
        # 分组处理
        for li in li_list:
            item = YGItem()
            item['lv_img_url'] = li.xpath('./div[1]/img/@src').extract_first()
            item['lv_title'] = li.xpath('./div[2]/h2/a/text()').extract_first()
            next_url = li.xpath('./div[2]/p/a/@href').extract_first()
            yield scrapy.Request(
                next_url,
                callback=self.parse_detail,
                meta={'item': item}
            )

    def parse_detail(self, response):
        item = response.meta['item']
        item['lv_content'] = response.xpath('//div[@class="ner_p"]//text()').extract()
        yield item
