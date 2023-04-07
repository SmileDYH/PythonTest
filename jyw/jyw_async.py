from utils import request_util
import datetime

async def func1(token, url):
    for page in range(1,10):
        params = {"subject":"chemistry2",
                    "tp":"1",
                    "dg":"0",#难度 13
                    "ct":"0",#题型 1,2,9
                    "token":token}
        userKey = request_util.post_new(url, params)
        print(userKey)
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " , " + str(page))


# task = [func1(token, url)]
# # python3.7引入的新特性，不用手动创建事件循环
# asyncio.run(task)