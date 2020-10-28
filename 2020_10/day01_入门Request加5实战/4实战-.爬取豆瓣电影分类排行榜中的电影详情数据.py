#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/22 16:59
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 4实战-.爬取豆瓣电影分类排行榜中的电影详情数据.py
# @Software : PyCharm
import requests
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Mobile Safari/537.36',
}
if __name__ == "__main__":
    date_url = 'https://movie.douban.com/j/new_search_subjects'
    param = {
        'sort': 'U',
        'range': '0, 10',
        'tags': '励志',
        'start': 0,
    }
    response = requests.get(date_url, params=param, headers=headers)
    print(response.json())