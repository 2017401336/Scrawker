import scrapy
import logging
class SpiderSpider(scrapy.Spider):
    # 爬虫的名称，唯一标识
    name = 'spider'

    # 允许爬取的范围，防止爬取到别的网站
    # 默认注释掉，因为用处不大（普通的网站，可能图片的存储位置不在该地址下，就不能爬取）
    allowed_domains = ['www.sogou.com']

    # 开始爬取的地址
    start_urls = ['http://www.sogou.com/']


    # 数据提取方法，接收下载中间件传过来的Response对象
    def parse(self, response):
        logger = logging.getLogger(__name__)
        print(response.url, "_____----------")
        logger.warning("这是一个警告")
        logger.error("这是一个错误信息")
        logger.info("这是一个通知")
        # pass
        # 得到页面源码，可以采用xpath等手段去提取需要的数据
        # print(response.text)
        res = response.xpath('//*[@id="wrap"]/div[1]/div[1]/ul/li')
        # print("xpath结果")
        # print(res)
        # xpath分组提取
        for category in res:
            # cate_name是一个selector对象
            # [<Selector xpath='//*[@id="wrap"]/div[1]/div[1]/ul' data='<ul><li class="cur"><span>网页</span></...'>]
            cate_selector = category.xpath('./span/text() | ./a/text()')
            cate_name = cate_selector.extract_first()
            # cate_neme = category.xpath('./span/text() | ./a/text()').extract_first()
            item = dict(
                name=cate_name,
            )
            yield item
            # 为什么会使用yield？？？
