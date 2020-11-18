import requests

proxy_server = {'http': 'http://127.0.0.1:8888',
                'https': 'http://127.0.0.1:8888'}  # Charles配置

proxy_username_password = {'https': 'http//username:password@127.0.0.1:8888'}  # 假如公司需要vpn的话，对应单词里填写对应vpn的账号和密码

response = requests.get(url='http://www.hnxmxit.com/',
                        proxies=proxy_server)  # 代理配置
print(response.status_code)
