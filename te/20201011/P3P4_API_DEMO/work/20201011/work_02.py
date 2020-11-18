#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: work_02.py
# @time: 2020/10/11 9:16 上午

import re
from collections import OrderedDict

import requests

hosts = '47.107.178.45'
ses = requests.session()  # requests保持会话链接、保持缓存的一个对象

response = ses.get(url='http://%s/phpwind/'%hosts)
body = response.content.decode('utf-8')
token_id = re.findall('name="csrf_token" value="(.+?)"',body)[0]
# print( token_id )


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
#  --  登录  --
url_params={
    "c":"post",
    "a":"doreply",
    "_getHtml":	"1"
}
post_data={
    "csrf_token":token_id,
    "atc_content":"hello,P3P4001",
    "tid":"92511"
}
response02 = ses.post(url='http://%s/phpwind/index.php'%hosts,
                      params=url_params,
                      data=post_data)
