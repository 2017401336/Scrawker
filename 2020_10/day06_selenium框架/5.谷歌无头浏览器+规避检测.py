#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/26 21:50
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 5.谷歌无头浏览器+规避检测.py
# @Software : PyCharm
"""
无可视化界面（无头浏览器）
webdriver.phantomJs是selenium里面封装好的无头浏览器
已经停止更新和维护
"""
from selenium import webdriver
# 实现无头界面
from selenium.webdriver.chrome.options import Options
# 实现规避检测
from selenium.webdriver import ChromeOptions
from time import sleep
if __name__ == "__main__":
    # 创建一个参数对象，用来控制chrome以无界面模式打开
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 驱动路径
    path = './chromedriver.exe'
    # chrome_options=chrome_options会飘红，因为chrome_options参数已经弃用
    # 如何实现让selenium规避被检测到的风险
    browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options, options=option)
    url = 'http://www.baidu.com'
    browser.get(url)
    # browser.save_screenshot('baidu.png')
    print(browser.page_source)
    browser.quit()