#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/24 17:37
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 2_对1的优化.py
# @Software : PyCharm
from multiprocessing import Process
from time import time

def spawn_n_processes(n, target):
    threads = []
    for _ in range(n):
        thread = Process(target=target)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

def test(target, number=10, spawner=spawn_n_processes):
    """
    分别启动 1, 2, 3, 4 个控制流，重复 number 次，计算运行耗时
    """
    for n in (1, 2, 3, 4, ):
        start_time = time()
        for _ in range(number):  # 执行 number 次以减少偶然误差
            spawner(n, target)
        end_time = time()
        print('Time elapsed with {} branch(es): {:.6f} sec(s)'.format(n, end_time - start_time))

def fib():
    a = b = 1
    for i in range(100000):
        a, b = b, a + b
if __name__ == "__main__":
    test(fib)