#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/24 19:08
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 1.获取本机IP.py
# @Software : PyCharm

"""
# 代理ip
# https://www.kuaidaili.com/free/inha/6/
客户端网络到代理服务器网络之间的某个网络节点不稳定，会出现连接代理服务器超时。
测试方法：换个网络或者换个代理IP进行测试，如果正常，说明是这个原因。

代理服务器网络不稳定，会出现连接代理服务器超时。
测试方法：换个代理IP进行测试，如果正常，说明是上个代理IP不稳定的原因。

客户端网络不稳定，会出现连接代理服务器超时。
测试方法：换个网络进行测试，如果正常，说明是客户端网络不稳定的原因。

代理服务器网络到目标网站服务器网络之间的某个网络节点不稳定，会出现访问网站超时。
测试方法：换个代理IP或换个网站进行测试，如果正常，说明是这个原因。

使用代理IP发送的请求并发过大，可能会导致连接服务器超时。
测试方法：用浏览器设置代理测试访问网站，如果正常，说明是并发过大，程序访问需要降低并发。

目标网站服务器网络不稳定，会出现访问网站超时。
测试方法：换个网站进行测试，如果正常，说明是目标网站的问题。

程序设置的超时时间太短，时间过了就会访问网站超时。
测试方法：有人将访问网站的超时时间设置为2秒，发现会出现超时，当重新设置超时时间为5秒后，超时没有了。

触发了目标网站的反爬策略，会出现访问网站超时。
测试方法：浏览器设置代理IP访问网站，如果正常，说明程序访问有可能触发了目标网站的反爬策略。

以上是几种会触发超时问题的情况，当出现了超时，可以按照这些测试方法进行判断，到底是哪种情况导致的超时，然后再根据情况针对性的解决问题。
"""
import requests
from lxml import etree
import json
headers = {
     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Mobile Safari/537.36',
}
proxy = '121.235.229.113:9999'
proxies = {
    'http': 'http://'+proxy,
}
if __name__ == "__main__":
    print(proxies)
    url = 'https://www.baidu.com/'
    r = requests.get(url, headers=headers, proxies=proxies, timeout=60)
    print(r.status_code)
