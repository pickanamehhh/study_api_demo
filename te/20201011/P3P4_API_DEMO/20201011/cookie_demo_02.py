#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_01.py
# @time: 2020/9/23 8:45 下午


import re
from collections import OrderedDict

import requests

hosts = '47.107.178.45'
ses = requests.session()  # requests保持会话链接、保持缓存的一个对象

response = ses.get(url='http://%s/phpwind/'%hosts)
body = response.content.decode('utf-8')
token_id = re.findall('name="csrf_token" value="(.+?)"',body)[0]

header_info = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
}

ses.cookies.set('zFb_winduser','Pvi55R1gVKSwAM%2FUXo1SpBZQkwqudcGMYbl67RRG5nPLi%2B2Fdic%2FGX5Xaqw%3D',path='/',domain='47.107.178.45')
ses.cookies.set('zFb_lastvisit','9250%091602380592%09%2Fphpwind%2F',path='/',domain='47.107.178.45')

# 发帖
form_data = OrderedDict(
    [
        ("atc_title",(None,'P3344dfdf34')),
       ("atc_content",(None,'P3344ffdfdf34')),
        ("pid",(None,'')),
        ("tid",(None,'')),
        ("special",(None,'default')),
        ("reply_notice",(None,'1')),
        ("csrf_token",(None,token_id))
    ]
)

response = ses.post(url="http://%s/phpwind/index.php?c=post&a=doadd&_json=1&fid=81"%hosts,
                    files=form_data)
print( response.content.decode('utf-8') )










