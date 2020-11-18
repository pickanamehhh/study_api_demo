import requests
# https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
# https:   协议类型  api.weixin.qq.com：主机地址   /cgi-bin/token 请求地址
# grant_type=client_credential&appid=APPID&secret=APPSECRET  参数  参数之间用&分割的

# 方式1
# response = requests.get(url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx8708f96abc9abaf3&secret=5be760a8fac19282515d47d326ab108b')
# print(response.content.decode('utf-8'))


# 方式2
get_param_dict = {
    "grant_type": "client_credential",
    "appid": "wx8708f96abc9abaf3",
    "secret": "5be760a8fac19282515d47d326ab108b"
}


response = requests.get(url='https://api.weixin.qq.com/cgi-bin/token',
                        params=get_param_dict, verify=False)  # 为了避免ssl认证，可以将verify=False
print(response.content.decode('utf-8'))
