#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/26 20:42
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 2.selenium其他自动化操作.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep
if __name__ == "__main__":
    # 实例化一个浏览器对象
    bro = webdriver.Chrome(executable_path='./chromedriver.exe')
    # 向网址发起请求
    bro.get('http://www.baidu.com')
    # 定位标签
    search_input = bro.find_element_by_id('kw')
    # 传递值
    search_input.send_keys('IU')

    # bro.find_element_by_css_selector('#su')
    btn = bro.find_element_by_id('su')
    btn.click()
    sleep(2)
    js_scroll_bottom = 'window.scrollTo(0, document.body.scrollHeight)'
    # #第一个0表示左边控制横向滚动条位置，第二个0表示控制纵向滚动条位置。可修改
    js_scroll_top = 'window.scrollTo(0,0)'
    #执行一组js程序
    bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    sleep(5)

    # 回退
    # bro.back()
    bro.find_element_by_id('kw').clear()
    bro.find_element_by_id('kw').send_keys('b站')
    bro.find_element_by_id('su').click()
    sleep(3)
    bro.back()
    sleep(3)

    bro.quit()