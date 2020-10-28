#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/26 9:03
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 8.futures.Futrue对象.py
# @Software : PyCharm

import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor

def func(value):
    time.sleep(1)
    print(value)
    return value
pool = ThreadPoolExecutor(max_workers=5)
if __name__ == "__main__":
    for i in range(10):
        fut = pool.submit(func, i)
        print(fut)