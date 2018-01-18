#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-3 下午5:39
# @Author  : CarryHJR
# @File    : main.py
"""
idea is :
class:
    pwd
    name
    header 常用头
    url 登录的url
    def encrypt 用于加密

    def login 登录




"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import base64
import requests
import time
import uuid
import socket
import platform
import os


class whut_wifi():
    url = "http://172.30.16.34/srun_portal_pc.php"
    pwd = '*****'
    username = '*****'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    data = {'action':'login',
            'ac_id':'26',
            'save_me':'1'}

    # 加密pwd
    def encrypt(self, s):
        return '{B}' + base64.b64encode(s)

    # 增加windows适配
    def get_mac_address(self):

        if platform.system() == 'Linux':
            mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
            return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
        
        if platform.system() == 'Windows':
            # refer: https://gist.github.com/mike-zhang/4240150
            var = os.popen("wmic nicconfig get MACAddress").read()
            macList = []
            for x in var.split(" \r\n"):
                if len(x.strip()) > 0 and x.find("MACAddress"): 
                    if x not in macList:macList.append(x)
            return macList[0]



    def get_host_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()

        return ip

    def login(self):
        self.data['user_ip'] = self.get_host_ip()
        # self.data['user_ip'] = "10.139.52.208"
        self.data['user_mac'] = self.get_mac_address()
        # self.data['user_mac'] = "98:5f:d3:35:ca:b7"
        self.data['username'] = self.username
        self.data['password'] = self.encrypt(self.pwd)
        r = requests.post(url=self.url, headers=self.headers, data=self.data)
        return r

r = whut_wifi().login()
print(r.status_code)
content = r.text

if content.find(u'网络已连接') != -1:
    time.sleep(2)
    print('login successfully')
else:
    print('login failed')

# f = open('result.html', 'w')
# f.write(r.text.encode('utf-8'))
# f.close()
