#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/24 17:21
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 1_测速函数.py
# @Software : PyCharm

from time import time
from threading import Thread

def spawn_n_threads(n, target):
    """
    启动 n 个线程并执行target函数
    """

    threads = []
    for _ in range(n):
        thread = Thread(target=target)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def fib():
    a = b = 1
    for i in range(100000):
        a, b = b, a + b

def test(target, number=10, spawner=spawn_n_threads):
    """
    分别启动 1, 2, 3, 4 个控制流，重复 number 次，计算运行耗时
    """
    for n in (1, 2, 3, 4, ):
        start_time = time()
        for _ in range(number):  # 执行 number 次以减少偶然误差
            spawner(n, target)
        end_time = time()
        print('Time elapsed with {} branch(es): {:.6f} sec(s)'.format(n, end_time - start_time))
if __name__ == "__main__":
    test(fib)