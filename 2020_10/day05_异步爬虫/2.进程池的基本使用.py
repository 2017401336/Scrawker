#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/25 20:43
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 2.进程池的基本使用.py
# @Software : PyCharm

import time
from multiprocessing.dummy import Pool
def get_page(str):
    print('正在下载...' + str)
    time.sleep(2)
    print('下载完成...' + str)

name_list = ['IU美图', 'IU演唱会', 'IU的音乐', 'IU影视']

if __name__ == "__main__":
    pool = Pool(4)
    start_time = time.time()
    pool.map(get_page, name_list)
    end_time = time.time()
    print('下载耗时：' + str(end_time - start_time) + 's')