#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/25 21:10
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 5.协程_01.py
# @Software : PyCharm

'''
协程：一个线程多个任务，当其中一个任务需要IO操作等待时，将去执行其他的任务
asyncio模块
'''

import time
import asyncio
# 协程方法
async def get_page(str):
    print('正在下载...' + str)
    # time.sleep(2)
    await time.sleep(2)
    print('下载完成...' + str)

name_list = ['IU美图', 'IU演唱会', 'IU的音乐', 'IU影视']

if __name__ == "__main__":
    start_time = time.time()

    # 1.将协程对象放入一个列表
    aio_list = []
    for name in name_list:
        aio_list.append(get_page(name))
    # 2.asyncio.wait(aio_list)：将aio_list中的每一个协程对象ensure_future，封装为Task对象返回（t）
    # 3.asyncio.run(t): 调用asyncio.runs实现执行两个协程
    asyncio.run(asyncio.wait(aio_list))
    end_time = time.time()
    print('下载耗时：' + str(end_time - start_time) + 's')
