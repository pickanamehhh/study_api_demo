#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: cookie_demo_01.py
# @time: 2020/10/11 9:30 上午

import requests

session = requests.session()

#方式一
# session.cookies['company_name']='newdream'
# response = session.get(url='http://www.hnxmxit.com/')

# 方式二(推荐)
session.cookies.set('company_name','newdream',path='/',domain='47.107.178.45')
response = session.get(url='http://www.hnxmxit.com/')

#方式三
# cookie_dict = {"company_name":"newdream"}
# requests.utils.add_dict_to_cookiejar(session.cookies,cookie_dict)
# response = session.get(url='http://www.hnxmxit.com/')

# #方式四
# cookie_object = requests.cookies.RequestsCookieJar()
# cookie_object.set('company_name','newdream')
# session.cookies.update(cookie_object)
# response = session.get(url='http://www.hnxmxit.com/')