# coding: utf-8
# jyw_main
import jyw_request
import datetime

"""注册 -- java"""
# url = "http://localhost:8088/jyw/register"
# params = {'apiID': '630ea04a-5dc6-4dd0-9bb9-e9806255dda3',
#             'apiPwd': 'cd7cc8',
#             'school': 'zkhy',
#             'userID': 'tiku4',
#             'userPwd': 'Abc123456',
#             'userName': 'tiku',
#             'userRole': '1',
#             'userSex': '1',
#             'apiKey': 'c6dcfd230231467b86fd8cd5e869a05e'}
# userKey = jyw_request.post_new(url, params)
# print(userKey)
"""登录 -- java"""
# url = "http://localhost:8088/jyw/login"
# params = {'apiID': '630ea04a-5dc6-4dd0-9bb9-e9806255dda3',
#             'userID': "tiku4",#tiku1、tiku2、tiku3
#             'userPwd': 'Abc123456',
#             'apiKey': 'c6dcfd230231467b86fd8cd5e869a05e'}
# token = "Token " + jyw_request.post_new(url, params)
# print(token)

token = "Token 3E0E8B7B692C6253FABD00EEC28701509CBF37AFD2647E25B56590869CF1E48A1183A9D830793745FC72E6F9C41AAA734398041608A4EA7D9E43999C506CDA79C0E7E0FDEDB312A6BC305B32818AF6A385B18717947E1BA33471A9F79F8255E74509BBB64B9D85CC3A268704F69270360324BB5F267B2350DCD059F88F4D7F41C1AF58551241950B0F8FF51E0C810A44"
"""获取学科"""
# url = "http://api.jyeoo.com/v1/subject"
# print(jyw_request.get(token, url))
"""获取教材"""
# url = str.format("http://api.jyeoo.com/v1/{subject}/book2", subject = "chemistry2")
# print(jyw_request.get(token, url))
# fp=open('d:/test.txt','w',encoding='utf-8')
# print(jyw_request.get(token, url),file=fp)
# fp.close()
"""获取地区"""
# url = "http://api.jyeoo.com/v1/region"
# print(jyw_request.get(token, url))
"""获取考点"""
# url = str.format("http://api.jyeoo.com/v1/{subject}/point2", subject = "chemistry2")
# fp=open('d:/test.txt','w',encoding='utf-8')
# print(jyw_request.get(token, url),file=fp)
# fp.close()
"""获取题型"""
# url = str.format("http://api.jyeoo.com/v1/{subject}/common?tp=1", subject = "chemistry2")
# print(jyw_request.get(token, url))

"""获取试题"""
# url = "http://api.jyeoo.com/v1/{subject}/counter/QuesQuery?tp={tp}&p1={p1}&p2={p2}&p3={p3}&ct={ct}&dg={dg}&sc={sc}&gc={gc}&rc={rc}&yc={yc}&ec={ec}&er={er}&so={so}&yr={yr}&rg={rg}&po={po}&pd={pd}&pi={pi}&ps={ps}&onlyNos={onlyNos}"
# url_str = str.format(url, subject="chemistry2",tp="1",p1="732ab9a0-615a-45ea-a1b1-9a1d3383ff9c",p2="e2678114-6989-4b1e-b03c-869a7d16979d",p3="",
#                      ct="0",dg="0",sc="False",gc="False",rc="False",yc="False",ec="False",er="False",so="0",yr="0",rg="",po="0",pd="1",pi="1",ps="10",onlyNos="0")
# print(jyw_request.get(token, url_str))
"""获取解析等"""
# url = "http://api.jyeoo.com/v1/{subject}/counter/QuesGet?id={sid}"
# url_str = str.format(url, subject="chemistry2", sid="7m6S7MUNMsGO0dOPMzYGNsNI0ufmuYIWW2SEX8yOtVkWZPZfxvYIWj61PGXzmNGZf2ffagHnmHHPuHDSgTsxPJeI4UI5gitueWhd9VAkl0k-3d")
# print(jyw_request.get(token, url_str))

"""获取并保存试题 -- java"""
url = "http://localhost:8088/jyw/queryQuestion"
# for语句遍历时遵循左闭右开的原则
for page in range(55,60):
    params = {"subject":"chemistry2",
                "tp":"1",
                "p1":"732ab9a0-615a-45ea-a1b1-9a1d3383ff9c",
                "p2":"e2678114-6989-4b1e-b03c-869a7d16979d",
                "dg":"13",#难度
                "ct":"1,2,9",#题型
                "pi":page,

                "book":"732ab9a0-615a-45ea-a1b1-9a1d3383ff9c",
                "bookName":"必修1",
                "editionName":"新人教版",
                "gradeName":"高一",
                "termName":"上学期",
                "typeName":"必修1",
                "chapter":"fdcde4b7-febf-495a-b2c7-960a3c38650f",
                "chapterName":"1.1 化学实验基本方法",
                "token":token}
    userKey = jyw_request.post_new(url, params)
    print(userKey)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))