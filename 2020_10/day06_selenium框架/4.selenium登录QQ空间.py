#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/26 21:39
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 4.selenium登录QQ空间.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep
if __name__ == "__main__":
    browser = webdriver.Chrome('./chromedriver.exe')
    # 1.对qq空间网址发起请求
    browser.get('https://qzone.qq.com/')
    # 2.选中iframe
    browser.switch_to.frame('login_frame')
    login_a = browser.find_element_by_id('switcher_plogin')
    login_a.click()
    browser.find_element_by_id('u').send_keys('账号')
    browser.find_element_by_id('p').send_keys('密码')
    sleep(3)
    browser.find_element_by_id('login_button').click()
    browser.switch_to.frame()
    sleep(5)
    browser.quit()