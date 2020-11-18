# 模拟post请求
import json
import requests

str_dict = {"name": "xiaoming", "age": 18, "sex": "男"}
print(type(str_dict))

str1 = json.dumps(str_dict)  # dumps把字典、json对象转化为字符串
print(type(str1))
print(repr(str1))  # repr() 转化为字符串 方便程序阅读的显示  str() 方便用户阅读的显示

str2 = '{"name": "xiaoming", "age": 18, "sex": "男"}'
str_json = json.loads(str2)  # loads把字符串、json格式数据转化为字典
print(type(str_json))
print(str_json.get('sex'))  # str_json['sex']
