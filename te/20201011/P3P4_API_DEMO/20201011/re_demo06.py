#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_01.py
# @time: 2020/9/23 8:45 下午

# 利用正则表达式 改成随机发帖

import re
from collections import OrderedDict
import random

import requests

hosts = '47.107.178.45'
ses = requests.session()  # requests保持会话链接、保持缓存的一个对象

response = ses.get(url='http://%s/phpwind/'%hosts)
body = response.content.decode('utf-8')
token_id = re.findall('name="csrf_token" value="(.+?)"',body)[0]
fids = re.findall('<p><a class="" href="http://47.107.178.45/phpwind/index.php\?c=thread&fid=(.+?)">',body)

random_fid = fids[random.randint(0,len(fids)-1)]


header_info = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
}

post_data = {
    "username":"xiaoliusir001",
    "password":"123456",
    "csrf_token":token_id,
    "csrf_token":token_id
}

response = ses.post(url='http://%s/phpwind/index.php?m=u&c=login&a=dologin'%hosts,
                         data=post_data,
                         headers=header_info)
body = response.text
loginid = re.findall('_statu=(.+?)"',body)[0]

# http://47.107.178.45/phpwind/index.php?m=u&c=login&a=welcome&_statu=eGZBM2EybExhcTc0Q3c0YVhHY094TUZhMUVLSG85VVlMR3pMQkMlMkZ4V1U0aW5xekY3aXYxTTdiU09Xa0VSN2NQc1kwS0pnJTNEJTNEfGh0dHA6Ly80Ny4xMDcuMTc4LjQ1L3BocHdpbmQvfA

get_data_dict={
    "m":"u",
    "c":"login",
    "a":"welcome",
    "_statu":loginid
}

response = ses.get(url='http://%s/phpwind/index.php'%hosts,
                   params=get_data_dict)

print( response.content.decode('utf-8') )

# 发帖
form_data = OrderedDict(
    [
        ("atc_title",(None,'P3344dffgg11')),
       ("atc_content",(None,'P3344ffeeee111')),
        ("pid",(None,'')),
        ("tid",(None,'')),
        ("special",(None,'default')),
        ("reply_notice",(None,'1')),
        ("csrf_token",(None,token_id))
    ]
)

response = ses.post(url="http://%s/phpwind/index.php?c=post&a=doadd&_json=1&fid=%s"%(hosts,random_fid),
                    files=form_data)
print( response.content.decode('utf-8') )










