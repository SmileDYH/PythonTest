# coding: utf-8
# jyw_main
from utils import request_util
import jyw_async
import asyncio

"""注册 -- java"""
# url = "http://localhost:8088/jyw/register"
# params = {'apiID': '630ea04a-5dc6-4dd0-9bb9-e9806255dda3',
#             'apiPwd': 'cd7cc8',
#             'school': 'zkhy',
#             'userID': 'tiku50',
#             'userPwd': 'Abc123456',
#             'userName': 'tiku',
#             'userRole': '1',
#             'userSex': '1',
#             'apiKey': 'c6dcfd230231467b86fd8cd5e869a05e'}
# userKey = request_util.post_new(url, params)
# print(userKey)
"""登录 -- java"""
url = "http://localhost:8088/jyw/login"
params = {'apiID': '630ea04a-5dc6-4dd0-9bb9-e9806255dda3',
            'userID': "tiku50",#tiku1、tiku2、tiku3、tiku4、tiku5...tiku50
            'userPwd': 'Abc123456',
            'apiKey': 'c6dcfd230231467b86fd8cd5e869a05e'}
token = "Token " + request_util.post_new(url, params)
print(token)

# token = "Token 3E0E8B7B692C6253FABD00EEC28701509CBF37AFD2647E25B56590869CF1E48A5A440455746316E6EC659E6488BF45C4D1671873316FB9F2825E049EC4F09BE96ABC1EEE1115D7DA802ECF708B5048CB8999B69CE4481D1AC49EF33400ED7E4554C547AC8905001C9C41D66552A303EE07329987949DD4D2271E86A44BAF6A5EAF248276DC5FF8A6C49459EB16FD715A"
"""获取学科"""
# url = "http://api.jyeoo.com/v1/subject"
# print(request_util.get(token, url))
"""获取教材"""
# url = str.format("http://api.jyeoo.com/v1/{subject}/book2", subject = "chemistry2")
# print(request_util.get(token, url))
# fp=open('d:/test.txt','w',encoding='utf-8')
# print(request_util.get(token, url),file=fp)
# fp.close()
"""获取地区"""
# url = "http://api.jyeoo.com/v1/region"
# print(request_util.get(token, url))
"""获取考点"""
# url = str.format("http://api.jyeoo.com/v1/{subject}/point2", subject = "chemistry2")
# fp=open('d:/test.txt','w',encoding='utf-8')
# print(request_util.get(token, url),file=fp)
# fp.close()
"""获取题型"""
# url = str.format("http://api.jyeoo.com/v1/{subject}/common?tp=1", subject = "chemistry2")
# print(request_util.get(token, url))

"""获取试题"""
# url = "http://api.jyeoo.com/v1/{subject}/counter/QuesQuery?tp={tp}&p1={p1}&p2={p2}&p3={p3}&ct={ct}&dg={dg}&sc={sc}&gc={gc}&rc={rc}&yc={yc}&ec={ec}&er={er}&so={so}&yr={yr}&rg={rg}&po={po}&pd={pd}&pi={pi}&ps={ps}&onlyNos={onlyNos}"
# url_str = str.format(url, subject="chemistry2",tp="1",p1="732ab9a0-615a-45ea-a1b1-9a1d3383ff9c",p2="e2678114-6989-4b1e-b03c-869a7d16979d",p3="",
#                      ct="0",dg="0",sc="False",gc="False",rc="False",yc="False",ec="False",er="False",so="0",yr="0",rg="",po="0",pd="1",pi="1",ps="10",onlyNos="0")
# print(request_util.get(token, url_str))
"""获取解析等"""
# url = "http://api.jyeoo.com/v1/{subject}/counter/QuesGet?id={sid}"
# url_str = str.format(url, subject="chemistry2", sid="7m6S7MUNMsGO0dOPMzYGNsNI0ufmuYIWW2SEX8yOtVkWZPZfxvYIWj61PGXzmNGZf2ffagHnmHHPuHDSgTsxPJeI4UI5gitueWhd9VAkl0k-3d")
# print(request_util.get(token, url_str))

"""获取并保存试题 -- java"""
url = "http://localhost:8088/jyw/queryQuestion"
# for语句遍历时遵循左闭右开的原则
# for page in range(1,50):
#     params = {"subject":"chemistry2",
#                 "tp":"1",
#                 "p1":"02834b4a-68fe-4593-8c14-4e6776f86166",
#                 "p2":"472acd3b-f3ae-44d5-8576-80e12a944716",
#                 "dg":"0",#难度 13
#                 "ct":"0",#题型 1,2,9
#                 "pi":page,
#
#                 "book":"02834b4a-68fe-4593-8c14-4e6776f86166",
#                 "bookName":"必修1",
#                 "editionName":"鲁科版",
#                 "gradeName":"高一",
#                 "termName":"上学期",
#                 "typeName":"必修1",
#                 "chapter":"472acd3b-f3ae-44d5-8576-80e12a944716",
#                 "chapterName":"3.1 碳的多样性",
#                 "token":token}
#     userKey = request_util.post_new(url, params)
#     print(userKey)
#     print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " , " + str(page))
"""优化入参"""
# for page in range(1,150):
#     params = {"subject":"chemistry2",
#                 "tp":"1",
#                 "dg":"0",#难度 13
#                 "ct":"0",#题型 1,2,9
#                 "token":token}
#     userKey = request_util.post_new(url, params)
#     print(userKey)
#     print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " , " + str(page))
"""通过异步方式"""
# asyncio.run(jyw_async.func1(token, url))
"""调用消息队列"""
url = "http://localhost:8088/jyw/messageProduction"
asyncio.run(jyw_async.func1(token, url))