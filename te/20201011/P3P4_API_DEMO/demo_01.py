#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_01.py
# @time: 2020/9/21 9:11 下午

import json
import jsonpath

str1 = "{'Date': 'Mon, 21 Sep 2020 13:02:22 GMT', 'Content-Type': 'application/json;charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'A-Token-Header': 'JSxEWVdSVERHTEQMWVRcIBw=', 'R-Token-Header': 'bncfBAwK', 'A-Token-Expired-Header': '1600952542914', 'S-Time-Header': '1600693342924', 'S-F-Time-Header': '20200921210222', 'Expires': 'Thu, 01 Jan 1970 00:00:00 GMT', 'Cache-Control': 'no-cache', 'Content-Encoding': 'gzip', 'Vary': 'Accept-Encoding'}"
dicta = dict(str1)
json_data = json.loads( dicta )

v = jsonpath.jsonpath(json_data,'$.R-Token-Header')
print( v )