#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/26 21:14
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 3.selenium处理iframe.py
# @Software : PyCharm
"""
定位的标签在iframe标签之中
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
if __name__ == "__main__":
    url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    bro = webdriver.Chrome('./chromedriver.exe')
    bro.get(url)
    bro.switch_to.frame('iframeResult')
    div = bro.find_element_by_id('draggable')
    print(div)
    # 创建一个动作链，传入一个浏览器对象
    action = ActionChains(bro)
    # 长按div
    action.click_and_hold(div)
    # 水平拖动15个px,perform():执行动作链
    for i in range(5):
        action.move_by_offset(17, 0).perform()
    # 释放动作链
    action.release()
    sleep(5)
    bro.quit()