#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/25 20:36
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 1.同步运行-阻塞.py
# @Software : PyCharm

import time
def get_page(str):
    print('正在下载...' + str)
    time.sleep(2)
    print('下载完成...' + str)

name_list = ['IU美图', 'IU演唱会', 'IU的音乐', 'IU影视']

if __name__ == "__main__":
    start_time = time.time()
    for name in name_list:
        get_page(name)
    end_time = time.time()
    print(type(end_time))
    print('下载耗时：' + str(end_time - start_time) + 's')