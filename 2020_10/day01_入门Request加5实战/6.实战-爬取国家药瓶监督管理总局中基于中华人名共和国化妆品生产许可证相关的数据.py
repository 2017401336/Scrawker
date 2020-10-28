#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/22 17:08
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 6.实战-爬取国家药瓶监督管理总局中基于中华人名共和国化妆品生产许可证相关的数据.py
# @Software : PyCharm
import requests
import time
import ast
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Mobile Safari/537.36',
}
if __name__ == "__main__":
    startTime = time.time()
    base_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    ids = []
    for page in range(1, 6):
        data = {
            'on': True,
            'page': page,
            'pageSize': 15,
            'productName': '',
            'conditionType': 1,
            'applyname': '',
            'applysn': '',
        }
        response = requests.post(base_url, data=data, headers=headers)
        json_dict =response.json()
        # 存储企业ID
        if ids is None:
            ids = [d['ID'] for d in json_dict['list']]
        else:
            ids.extend([d['ID'] for d in json_dict['list']])

    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    all_data_list = []
    counts = 0
    print(len(ids))
    for id in ids:
        data = {
            'id': id,
        }
        detail_json = requests.post(post_url, data=data, headers=headers).json()
        counts += 1
        all_data_list.append(detail_json)
    endTime = time.time()
    print(all_data_list)
    print('查询到生产许可证个数：' + str(counts))
    print('用时：' + str(int(endTime-startTime)) + 's')
