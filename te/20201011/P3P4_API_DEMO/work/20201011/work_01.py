#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: work_01.py
# @time: 2020/10/11 8:41 上午

#  charles+requests 完成论坛的注册
#  1、charles抓包  2、requests根据抓包信息编写脚本  3、调试脚本 == 》 关联

import requests
import re

hosts = '47.107.178.45'
session_seq = requests.session()  #创建session对象

response01 = session_seq.get(url='http://%s/phpwind/'%hosts) # 打开主页

url_params={
    "m":"u",
    "c":"register"
}
response02 = session_seq.get(url='http://%s/phpwind/index.php'%hosts,
                             params=url_params) # 打开注册页面
# name="csrf_token" value="75afe7d22b7af0ce"/>
body = response02.content.decode('utf-8')
token = re.findall('name="csrf_token" value="(.+?)"',body)[0]
print(token)


url_params1={
    "m":"u",
    "c":"register",
    "a":"dorun"
}

regedit_data={
    "username":"P3P4002",
    "password":"123456",
    "repassword":"123456",
    "email":"P3P4002@qq.com",
    "csrf_token":token
}
response03 = session_seq.post(url='http://%s/phpwind/index.php'%hosts,  # 注册
                              params=url_params1,
                              data=regedit_data
                              )

print( response03.content.decode('utf-8') )




