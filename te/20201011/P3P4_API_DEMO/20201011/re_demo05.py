#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: re_demo05.py
# @time: 2020/10/11 11:39 上午

import requests
import re
import random

#应用一：截取字符串应用
response = requests.get(url='http://www.hnxmxit.com/')
body = response.content.decode('utf-8')
# print( body )
value = re.search('<title>(.+)</title>',body)
print( value.group(1) )

value = re.findall('<title>(.+?)</title>',body)
print( value )

#应用二：利用正则截取字符串需要的数据  http://47.107.178.45/phpwind/
response = requests.get(url='http://47.107.178.45/phpwind/')
body = response.content.decode('utf-8')
value1 = re.findall('<p><a class="" href="http://47.107.178.45/phpwind/index.php\?c=thread&fid=(.+?)">',body)
print(value1)
print(len(value1))
print( value1[random.randint(0,len(value1)-1)] )










# value = re.findall('<p><a class="" href="http://47.107.178.45/phpwind/index.php\?c=thread&fid=(.+?)">',body)
# print( value )
# print( len(value) )
# fid = random.randint(0,len(value)-1)
# print( value[fid] )





