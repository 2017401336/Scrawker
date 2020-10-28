#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/22 15:55
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 5.实战-爬取肯德基餐厅查询中指定地点的餐厅.py
# @Software : PyCharm
import requests
import ast
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Mobile Safari/537.36',
}
if __name__ == "__main__":
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    kw = input('请输入查询地址:')
    data = {
        'cname': '',
        'pid': '',
        'keyword': kw,
        'pageIndex': 1,
        'pageSize': 10,
    }
    response = requests.get(base_url, data, headers=headers)
    # res_dict = ast.literal_eval(response.text)
    # print(res_dict['Table1'])
    fileName = kw + '.json'
    with open(fileName, 'w', encoding='utf-8') as fp:
        json.dump(response.text, fp)
    print('Writ succeeded...')
