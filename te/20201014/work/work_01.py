#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: work_01.py
# @time: 2020/10/14 8:15 下午

import requests
import re
import random

response = requests.get(url='https://www.baidu.com/')

body = response.content.decode('utf-8')

value = re.findall(r'class=mnav>(.+?)</a>',body)
print( value )
print( value[random.randint(0,len(value)-1)] )