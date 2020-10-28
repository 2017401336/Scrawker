#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/22 14:36
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 3.实战-破解百度翻译.py
# @Software : PyCharm
import requests
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Mobile Safari/537.36',
}
if __name__ == "__main__":
    base_url = 'https://fanyi.baidu.com/sug'
    kw = input('请输入需要翻译的中文：')
    data = {
        'kw': kw,
    }
    res = requests.post(base_url, data=data, headers=headers)
    # content-type: application/json
    dic_obj = res.json()
    # 持久化存储
    fileName = kw + '.json'
    with open(fileName, 'w', encoding='utf-8') as fp:
        json.dump(dic_obj, fp=fp)
    print('Write succeeded...')

