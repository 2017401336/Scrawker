# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json
class SpiderproPipeline(object):
    # 这个方法将会在Spider打开时调用
    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        """
        每一个Item Pipeline都会调用这个方法，用来处理Item，返回值为item或dict。
        这个方法还可以抛出一个DropItem异常，这样将会不再继续调用接下来的Item Pipeline。
        :param item: 是parse方法传来的
        :param spider: 抓取这个Item的Spider
        :return: item
        """
        return item

    # 这个方法将会在Spider关闭时调用
    def close_spider(self, spider):
        pass

class Job_tenxun_Pipeline(object):

    def open_spider(self, spider):
        self.fp = open('./job.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(json.dumps(dict(item), ensure_ascii=False))
        self.fp.write('\n')
        return item

    def close_spider(self, spider):
        self.fp.close()

import re

class YG_Pipeline(object):
    def open_spider(self, spider):
        self.fp = open('./yangguang.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        item['lv_content'] = self.process_content(item['lv_content'])
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.fp.write(content)
        return item

    def process_content(self, content):
        content = [re.sub(r'\u3000\u3000|\s|r|n', '', i) for i in content]
        content = [i for i in content if len(i) > 0]
        content = ''.join(content)
        return content

    def close_spider(self, spider):
        print("{}:爬虫数据处理完毕！".format(spider.name))
        self.fp.close()
