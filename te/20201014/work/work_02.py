#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: work_01.py
# @time: 2020/10/14 8:15 下午

import requests

# 博客园回复操作

session = requests.session()

header_info = {
    "accept":"application/json, text/javascript, */*; q=0.01",
    "x-requested-with":"XMLHttpRequest",
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "content-type":"application/json; charset=UTF-8"
}

post_data = {
	"postId": 13813155,
	"body": "班级实验使用123",
	"parentCommentId": 0
}

session.cookies.set('__gads','ID=ab91525d778877ca:T=1591186309:S=ALNI_MbdG8HG8Q14Fyp-NaQ5c2G2h08oHw',path='/',domain='.cnblogs.com')
session.cookies.set('_ga','GA1.2.59649760.1591186340',path='/',domain='.cnblogs.com')
session.cookies.set('_gid','GA1.2.1861009743.1602470358',path='/',domain='.cnblogs.com')
session.cookies.set('.Cnblogs.AspNetCore.Cookies','CfDJ8AHUmC2ZwXVKl7whpe9_lavJBvOcxzvSvKM-guN31c6b0Ap7SGfzo2vuct30C0L2SYvgheMPudgaO_iPW70AxoqYoQL_uFESOObxtXfOSBRwCXsP8-w8aTzaqL_4M--WnpnMMuxa91nLXcZYDP2LC_ISAZ4w-NtcNSFik4iYb9Hz_MJQy40fDdWLSHpbjStGYgBy3sBZNhNWn9h3CNotFwhg7iANvr581AaFSEiGytVeDnz2dGiCRrlFFtrR5cdBb3_68gfLexNUyTZuBVkOzu48fUiPs46P-axymdKHY0Qe-4O67YSIpHdwvzWcnDHM3_O7lrLz4av-4yeG27UTr9ddKntC78luAX-nKAKvuvSqAZNOcH11nM1jrsgaLSLOorl96bx1_BcGdJoyBc3IRprEtgEbRUZCgBvZr_z4P5lbRPWxB09k9nLo8HsakSV2J7BVJH_OoIRs4akcXaxISx6jCQQZjGwSdC3v-0FUvz5fVomzHT1AL3VrVFR-CN-tSbeRlEpQJ_EsQ4PzlC-hMpGgXufxFmTrwZ-Ats0MoJUznMEd6PSXKZ5pRgBmsQ3BgQ',path='/',domain='.cnblogs.com')
session.cookies.set('.CNBlogsCookie','4E71B8F1F3B5F1E0EE0AC39B8C4D047C699DB88B1E9E186923002D7E545D52F7CCF305EF0B51DA9EC059E49F05198E192305A8548DE36650B26BC7556940F57121B9DBA4C525ADD60F1BE38A37D76AAF0B0CF997',path='/',domain='.cnblogs.com')
session.cookies.set('_gat','1',path='/',domain='.cnblogs.com')

response = session.post(url='https://www.cnblogs.com/dream66/ajax/PostComment/Add.aspx',
                        json=post_data)