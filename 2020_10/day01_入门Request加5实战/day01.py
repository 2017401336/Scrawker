#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/21 17:21
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : day01.py
# @Software : PyCharm
import requests

'''
需求：获取搜狗首页内容
'''
if __name__ == "__main__":
    url = "http://www.sogou.com"
    response = requests.get(url=url)
    page_txt = response.text
    with open('./sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_txt)
    print('爬取数据结束！！！')
