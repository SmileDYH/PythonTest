#1.获取text文件
#2.转成json
#3.多层for循环，count累加，统计总数
from utils import request_util
import urllib.request
import asyncio
import test

url = "https://qc-tiku.zkhyedu.com/wl/tiku-business-serv/tiku/feign/v2/question/getListDetailByNumbers"
# params = {"questionNumbers": [5193801344716800,5193787585302528,5193786360434688,5193801860091904,4931394845904896,5193804303142912,5193791173005312,5193797548216320,5193797550313472,5193787043713024,5193809147301888,4923266302054400,4923266306117632,4923258416238592,5193809148743680,4923243337322496,4931394843152384,5193797549395968]}
# userKey = request_util.post_new(url, params)
# print(userKey)
#
# for page in range(1,100):
#     params1 = {"questionNumbers": "5193813981106176,5193813982547968,5193813984907264,5193816624304128,5193816625352704,5193816627318784,5193816629153792,5193816630988800,5193817379409920,5193817878401024,5193820548206592,5193820549124096,5193820549910528,5193822075719680,5193823534944256,5193825648611328"}
#     data = bytes(urllib.parse.urlencode(params1), encoding='utf8')
#     response = urllib.request.urlopen(url, data=data)
#     print(response.read())


params2 = {"questionNumbers": "5193813981106176,5193813982547968,5193813984907264,5193816624304128,5193816625352704,5193816627318784,5193816629153792,5193816630988800,5193817379409920,5193817878401024,5193820548206592,5193820549124096,5193820549910528,5193822075719680,5193823534944256,5193825648611328"}
for i in range(1,1000):
    asyncio.run(test.func1(url, params2))
