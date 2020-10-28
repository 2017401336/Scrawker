#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/23 17:15
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 1.爬取58同城二手房信息.py
# @Software : PyCharm


import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 85.0.4181.9Safari / 537.36'
}
if __name__ == "__main__":
    url = 'https://m.58.com/cq/ershoufang/'

    page_text = requests.get(url, headers=headers).text
    # 数据解析，得到etree对象
    # print(page_text)
    tree = etree.HTML(page_text)
    title_name = tree.xpath('//li[@class="list-item-info-title"]/text()')
    print(title_name)