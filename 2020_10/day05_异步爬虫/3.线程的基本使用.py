#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/25 20:51
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 3.线程的基本使用.py
# @Software : PyCharm
import time
import threading
"""
https://www.cnblogs.com/luyuze95/p/11289143.html
"""
def get_page(str):
    print('正在下载...' + str)
    time.sleep(2)
    print('下载完成...' + str)

name_list = ['IU美图', 'IU演唱会', 'IU的音乐', 'IU影视']

if __name__ == "__main__":
    start_time = time.time()
    thread_list = []
    for name in name_list:
        t = threading.Thread(target=get_page, args=(name, ))
        thread_list.append(t)
    for t in thread_list:
        t.setDaemon(True)
        t.start()
    for t in thread_list:
        t.join()
    end_time = time.time()
    print('下载耗时：' + str(end_time - start_time) + 's')