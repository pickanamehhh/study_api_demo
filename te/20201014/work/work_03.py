#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: work_03.py
# @time: 2020/10/14 8:41 上午

import requests

session = requests.session()

data_params_dict = {
	"postId": 13382888,
	"body": "test！！",
	"parentCommentId": 0
}
header_info = {
    "accept":"application/json, text/javascript, */*; q=0.01",
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "content-type":"application/json; charset=UTF-8"
}
session.cookies.set('__gads','ID=ab91525d778877ca:T=1591186309:S=ALNI_MbdG8HG8Q14Fyp-NaQ5c2G2h08oHw',path='/',domain='.cnblogs.com')
session.cookies.set('_ga','GA1.2.59649760.1591186340',path='/',domain='.cnblogs.com')
session.cookies.set('pgv_pvi','7273943040',path='/',domain='.cnblogs.com')
session.cookies.set('UM_distinctid','1732795b37c21b-04edebbc2dcd32-31617402-fa000-1732795b37d80e',path='/',domain='.cnblogs.com')
session.cookies.set('.CNBlogsCookie','E371ED2B5AEF1B8F0C227035D1A3C4A69B2EDB3B2E25C9C3849FA09BADA9E74482191571CFCC95ADA5331610961FE47D23760C32E8973EE0662114BE5F0D6793D2250E3FA75A22E468E426AE32FBDFA4719D5FF5',path='/',domain='.cnblogs.com')
session.cookies.set('.Cnblogs.AspNetCore.Cookies','CfDJ8K5MrGQfPjpFvRyctF-QEQe4rOJmGWqT_BhYkTxWgFlG-J-Wy6XFTJLadGfSxtxRtER-x1dxE6IMUSr4jdKEX3uOoGiC19V5gW63DBAyvJiGFLk8_5WvvEQ7AeC1ZLkaIuQ2CmcoRYtZIcdy77cAazGKZAJcwoHEbHL2T5xEOccIDG3LwaYf2qsYCalndUy2TiAAjiiJOpVx4R__pQiw8095TLizVqBznWCp8u-I4OksvjHjNsiKK_6WJUPVWxTG4M11wTGpfbXlHx3A965WArR3IUXrDCfRKqFITTXf9xJiFC5EQVM1I7-t4Z9Uis9J8FYwE5e5XQ8HPqMuAAAayOsIjFrKeGA_jX2ikoFGD6N8xz0gMF6JdnKYql4dTIX0NM4kCvLuBzgo2atjIUEYPmheKNEZemb350N2sLzC8Hwn5lLIZo9uZTkvZ3ZYwFADgVi_jrBTAKKTe8rgAJUArqryBk2IKAiZpHB4_VIDrcpnx6iLnVZVHR-xuze5s3-GdcE0AD58xZ81REAqzUenIbQhOEy3flbMzw06TFM8ig1V5-EHEjo0RIIrqQbaDXwWnQ',path='/',domain='.cnblogs.com')
session.cookies.set('_gid','GA1.2.1861009743.1602470358',path='/',domain='.cnblogs.com')
session.cookies.set('_gat','1',path='/',domain='.cnblogs.com')
# session.cookies.set('__gads','ID=ab91525d778877ca:T=1591186309:S=ALNI_MbdG8HG8Q14Fyp-NaQ5c2G2h08oHw',path='/',domain='.cnblogs.com')
# session.cookies.set('__gads','ID=ab91525d778877ca:T=1591186309:S=ALNI_MbdG8HG8Q14Fyp-NaQ5c2G2h08oHw',path='/',domain='.cnblogs.com')
# session.cookies.set('__gads','ID=ab91525d778877ca:T=1591186309:S=ALNI_MbdG8HG8Q14Fyp-NaQ5c2G2h08oHw',path='/',domain='.cnblogs.com')

response = session.post(url='https://www.cnblogs.com/dream66/ajax/PostComment/Add.aspx',
                        json=data_params_dict,
                        headers = header_info)
