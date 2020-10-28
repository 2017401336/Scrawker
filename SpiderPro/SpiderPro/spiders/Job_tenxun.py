import scrapy

from SpiderPro.items import MyItem

from selenium import webdriver
class JobTenxunSpider(scrapy.Spider):
    name = 'Job_tenxun'
    # allowed_domains = ['https://careers.tencent.com/search.html?keyword=python']
    start_urls = ['https://careers.tencent.com/search.html?keyword=python/']
    # bro = webdriver.Chrome('./chromedriver.exe')
    def parse(self, response):
        item = MyItem()
        print(response.text)
        res = response.xpath('//html/body/div/div[4]/div[3]/div[2]/div[2]/div/a')
        print(res)
        for job_a in res:
            item['job_name'] = job_a.xpath('./h4/text()').extract_first()
            item['job_label'] = job_a.xpath("./p/span[1]/text()").extract_first()
            item['addr'] = job_a.xpath("./p/span[2]/text()").extract_first()
            item['time'] = job_a.xpath("./p/span[4]/text()").extract_first()
            item['info'] = job_a.xpath("./p/span[5]/text()").extract_first()
            yield item
