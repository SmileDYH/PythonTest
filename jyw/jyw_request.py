from utils import request_util
import jyw_async
import asyncio


"""登录 -- java"""
for i in range(2,4):
    url = "http://localhost:8088/jyw/login"
    params = {'apiID': '630ea04a-5dc6-4dd0-9bb9-e9806255dda3',
                'userID': "tiku" + str(i),
                'userPwd': 'Abc123456',
                'apiKey': 'c6dcfd230231467b86fd8cd5e869a05e'}
    token = "Token " + request_util.post_new(url, params)
    print(token)

    """获取并保存试题 -- java"""
    # 通过异步方式，调用消息队列
    url = "http://localhost:8088/jyw/messageProduction"
    asyncio.run(jyw_async.func1(token, url))