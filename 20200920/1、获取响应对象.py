import requests

# response 响应对象 （响应行、响应头、响应正文）
response = requests.get(url='')  # get()方法模拟发送get请求

# 获取响应正文有两种方式
# 方式1
print(response.content.decode('utf-8'))  # decode 解码

# 方式2
response.encoding = 'utf-8'
print(response.text)
