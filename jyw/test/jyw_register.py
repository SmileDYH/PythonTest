import urllib.request
import json

url = 'http://localhost:8088/jyw/register'
params = {'apiID': '630ea04a-5dc6-4dd0-9bb9-e9806255dda3',
            'apiPwd': 'cd7cc8',
            'school': 'zkhy',
            'userID': 'tiku1',
            'userPwd': 'Abc123456',
            'userName': 'tiku',
            'userRole': '1',
            'userSex': '1',
            'apiKey': 'c6dcfd230231467b86fd8cd5e869a05e'}

params = json.dumps(params)
headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}
# 用bytes函数转换为字节
params = bytes(params, 'utf8')

req = urllib.request.Request(url=url, data=params, headers=headers, method='POST')
response = urllib.request.urlopen(req).read()
print(response.decode('utf-8'))
