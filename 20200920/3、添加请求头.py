import requests

# get模拟请求头信息
# api = https://www.baidu.com/s?wd=newdream

get_param_dict = {
    'wd': 'newdream'
}

headers_info_dict = {  # 模拟真实的头部请求信息
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    "Accept": 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8'
}

response = requests.get(url='https://www.baidu.com/s',
                        params=get_param_dict,
                        headers=headers_info_dict)

print(response.content.decode('utf_8'))  # 内容解码
