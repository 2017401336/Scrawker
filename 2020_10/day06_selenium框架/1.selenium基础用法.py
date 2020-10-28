#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/26 20:21
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 1.selenium基础用法.py
# @Software : PyCharm
'''
chrome浏览器驱动各个版本下载及安装：https://blog.csdn.net/n123456uo/article/details/91412740
'''
from selenium import webdriver
from lxml import etree
if __name__ == "__main__":
    # 实例化一个浏览器对象
    bro = webdriver.Chrome(executable_path='./chromedriver.exe')
    # 访问网址
    bro.get('http://scxk.nmpa.gov.cn:81/xk/')
    # 获取浏览器当前页面的源码数据
    page_text = bro.page_source
    # 解析企业名称
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="gzlist"]/li/dl/a')
    for li in li_list:
        title = li.xpath('./text()')[0]
        href = li.xpath('./@href')[0]
        print(title, href)
    bro.quit()