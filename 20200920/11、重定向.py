# 重定向 请求和响应的时候 响应状态码为 3**

import requests
response = requests.get('http://www.360buy.com')
print(response.history)  # 显示请求的重定向信息
print(response.url)  # 显示请求的链接
print(response.content.decode('utf-8'))

# requests 在发送请求的时候，会进行自动重定向处理  不需要你干预
print('**********************************')

response1 = requests.get('http://www.360buy.com', allow_redirects=False)  # allow_redirects默认为ture，为false时即为关闭重定向
print(response1.history)  # 显示请求的重定向信息
print(response1.url)  # 显示请求的链接
print(response1.content.decode('utf-8'))
