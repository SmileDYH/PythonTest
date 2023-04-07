# coding: utf-8
from utils import request_util

"""注册"""
# url = "http://localhost:8088/jyw/register"
# postdata = {b'apiID': b'630ea04a-5dc6-4dd0-9bb9-e9806255dda3',
#             b'apiPwd': b'cd7cc8',
#             b'school': b'zkhy',
#             b'userID': b'tiku1',
#             b'userPwd': b'123456',
#             b'userName': b'tiku',
#             b'userRole': b'1',
#             b'userSex': b'1',
#             b'apiKey': b'c6dcfd230231467b86fd8cd5e869a05e'}
# print(request_util.post(None, url, postdata))



async def func1(url, params):
    request_util.post_form_data(url, params)