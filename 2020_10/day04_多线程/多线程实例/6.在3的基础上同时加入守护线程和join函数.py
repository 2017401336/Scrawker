#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/24 17:46
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 3.python多线程的默认情况.py
# @Software : PyCharm
import threading
import time
from datetime import datetime

class MyThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        time.sleep(5)
        print("子线程动作", threading.current_thread().name, datetime.now())

if __name__ == "__main__":
    t1 = MyThread(999)
    print(datetime.now())
    t1.setDaemon(True)      # 添加守护线程
    t1.start()
    t1.join()               # 添加join函数
    for i in range(5):
        print("主线程动作", threading.current_thread().name, datetime.now())
