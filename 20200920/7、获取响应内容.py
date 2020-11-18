import requests

response = requests.get(url='http://www.hnxmxit.com/')

# 响应行、响应状态码、响应信息、协议版本
print(response.status_code)  # 200
print(response.reason)  # ok

# 响应头
print(response.headers)  # 所有的响应头 {...}
print(response.headers['Server'])  # 单独取出Server的内容
print(response.headers['Content-Encoding'])

# 响应正文
# # 方式1
# # print(response.encoding)
# response.encoding = response.apparent_encoding  # 'utf-8'
# print(response.text)

# 方式2  二进制响应内容
print(response.content.decode('utf-8'))

# 方式3：json方式
print(response.json())

# 方式4 原始方式 raw
r = requests.get(url='http://www.hnxmxit.com/', stream=True)
print(r.raw.read(1))

