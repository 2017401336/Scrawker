#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/22 22:14
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 1.爬取三国演义小说的所有的章节标题和章节内容.py
# @Software : PyCharm

import requests
from bs4 import BeautifulSoup
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Mobile Safari/537.36',
}
if __name__ == "__main__":
    # 1.对首页的页面数据进行爬取
    # 2.在首页中解析出章节的标题和详情页面的url
    # 2.1：实例化BeautifulSoup,将网页源码加载到该对象
    base_url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(base_url, headers=headers).text
    soup = BeautifulSoup(page_text, 'lxml')
    mulu_tag_a = soup.select('.book-mulu a')
    mulu_link = []
    mulu_text = []
    fp = open('sanguoyanyi.txt', 'w', encoding='utf-8')
    for tag_a in mulu_tag_a:
        title = tag_a.text
        detail_url = 'https://m.shicimingju.com' + tag_a['href']
        page_detail = requests.get(detail_url, headers=headers).text
        detail_soup = BeautifulSoup(page_detail, 'lxml')
        tag_div = detail_soup.find('div', class_='chapter_content')
        content = tag_div.text
        fp.write(title + content + '\n')
        print(title + '爬取成功')
    fp.close()

