import os
import requests
import httpx  # 性能比requests更好，支持多线程，可以自学一下

current_path = os.path.dirname(__file__)
print(current_path)
excel_path = os.path.join(current_path, '..', 'data', 'test.xlsx')
#  excel_path = current_path + '/../data/test.xlsx'
excel_file = {'file': open(excel_path, 'rb')}
response = requests.post(
    url='http://httpbin.org/post',
    files=excel_file
)
print(response.content.decode('utf-8'))
