#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/23 17:52
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 3.爬取全国城市.py
# @Software : PyCharm
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 85.0.4181.9Safari / 537.36'
}
if __name__ == "__main__":
    url = 'https://m.jiajuol.com/designer/citylist'
    page_text = requests.get(url, headers=headers).text
    tree = etree.HTML(page_text)
    citis_name = tree.xpath('//div[@class="shape_info hot"]/a/text() | //div[@class="shape_info citys"]/a/text()')
    print(citis_name, len(citis_name))