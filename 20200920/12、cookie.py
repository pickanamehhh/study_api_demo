import requests

# 在请求中添加cookie
# # 方式一：
# cookie_dict = {"company_name": "new_dream"}
# response = requests.get(url='http://www.hnxmxit.com/',
#                         cookies=cookie_dict)

# 方式二：
header_info_dict = {"company_name": "new_dream"}
response = requests.get(url='http://www.hnxmxit.com/',
                        cookies=header_info_dict)

