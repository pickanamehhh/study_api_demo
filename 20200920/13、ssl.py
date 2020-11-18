import requests
import warnings
import urllib3

# response = requests.get('https://www.12306.cn')
# print(response.content.decode('utf-8'))

# https 必须带证书操作 处理方式一： 不验证证书,报警告,返回200
# 解决方案一：（废弃）
# from requests.packages import urllib3   # 老版本 request 2.6.0
# urllib3.disable_warnings()

# 解决方案二： 新版本
# requests.packages.urllib3.disable_warnings()  # 关闭警告
# warnings.filterwarnings("ignore")
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# response = requests.get('https://www.12306.cn', verify=False)  # verify为false时不校验证书，为true时默认校验
# print(response.content.decode('utf-8'))

# 方式二：安装pyopenssl模块 安装之后就不会报错
# pip install -U requests[security]
# response = requests.get('https://www.12306.cn')

# 方式三：加上证书  公司内部 开发同事要  ****.crt
response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
