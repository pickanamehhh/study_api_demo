import json
import requests

url_param_dict = {
    "access_token": '37_FSo1xXleTG56w5C9PH-vmkoFMt7avZvTKztRZECgRVXHxFzSTm8VbMLJCVINjzLwgPdwBw3jt2iU4KisugR-mv6bbV4wsYL6ughiNwQAP56E0TxyjQ3wgQaVgF-C_B_2mGIKC6Nkgb8w-i92IRAjAFAYHQ'
}
post_param_data = {"tag": {"name": 'one'}}

response = requests.post(url='https://api.weixin.qq.com/cgi-bin/tags/create',
                         params=url_param_dict,
                         # json=post_param_data
                         data=json.dumps(post_param_data))
print(response.content.decode('utf-8'))
