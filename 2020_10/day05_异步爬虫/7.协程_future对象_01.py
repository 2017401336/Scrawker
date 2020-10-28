#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/26 1:14
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 7.协程_future对象_01.py
# @Software : PyCharm
import asyncio
async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()

    # # 创建一个任务（Future对象），这个任务什么都不干。
    fut = loop.create_future()

    # 等待任务最终结果（Future对象），没有结果则会一直等下去。
    await fut

if __name__ == "__main__":
    asyncio.run(main())