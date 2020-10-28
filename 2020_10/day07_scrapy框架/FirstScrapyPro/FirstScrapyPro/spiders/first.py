import scrapy

class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称：爬虫源文件的唯一标识
    name = 'first'

    # 允许的域名：限定start_urls列表中哪些url可以进行请求发送
    # 一般不用
    allowed_domains = ['www.xxx.com']

    # 起始的url列表：该列表中存放的url会被scrapy自动进行请求发送
    start_urls = ['http://www.baidu.com/', 'http://www.sogou.com/']

    # response参数表示请求成功后对应的响应页面
    # parse的调用次数 = start_urls列表中元素的个数
    def parse(self, response):
        print(response)
