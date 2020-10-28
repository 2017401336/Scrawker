#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/22 14:17
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 2.实战：爬取搜狗指定词条对应的搜索结果页面.py
# @Software : PyCharm
import requests
'''
反爬虫：UA检测
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Mobile Safari/537.36',
}
if __name__ == "__main__":
    base_url = 'https://www.sogou.com/web?query='
    kw = input('输入需要查询的信息：')
    param = {
        'query': kw
    }
    response = requests.get(base_url, params=param, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('写入数据成功...')
