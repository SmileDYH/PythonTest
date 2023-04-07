# coding: utf-8
import warnings

warnings.filterwarnings('ignore')
from urllib import request

subject_url = "http://api.jyeoo.com/v1/subject"
question_url = "http://api.jyeoo.com/v1/{subject}/counter/QuesQuery?tp={tp}&p1={p1}&p2={p2}&p3={p3}&ct={ct}&dg={dg}&sc={sc}&gc={gc}&rc={rc}&yc={yc}&ec={ec}&er={er}&so={so}&yr={yr}&rg={rg}&po={po}&pd={pd}&pi={pi}&ps={ps}&onlyNos={onlyNos}"
analysis_url = "http://api.jyeoo.com/v1/{subject}/counter/QuesGet?id={sid}"
token = "Token 3E0E8B7B692C6253FABD00EEC28701509CBF37AFD2647E25B56590869CF1E48A8C56D5CA21DF94CFF87B1676F06D9BB48FB5BB802E3AF99210C0B24AE1D4719F19C705D012D5BE3308E0A6E9DE07A1CDB38E92AFDED2C09B3BE29E1C79A1B033DA495D7EE41958E8C6F44912D3442A8ED53ED2E52F457F8B4692BACF6696A8B4DB4AE648F069105B54D030990B8B0EC536400BAF6DD409FB"

# url_str = str.format(question_url, subject="chemistry2",tp="1",p1="732ab9a0-615a-45ea-a1b1-9a1d3383ff9c",p2="e2678114-6989-4b1e-b03c-869a7d16979d",p3="",
#                      ct="0",dg="0",sc="False",gc="False",rc="False",yc="False",ec="False",er="False",so="0",yr="0",rg="",po="0",pd="1",pi="1",ps="10",onlyNos="0")
url_str = str.format(question_url, subject="chemistry2",tp="1",p1="732ab9a0-615a-45ea-a1b1-9a1d3383ff9c",p2="e2678114-6989-4b1e-b03c-869a7d16979d",p3="",
                     ct="9",dg="0",sc="False",gc="False",rc="False",yc="False",ec="False",er="False",so="0",yr="0",rg="",po="0",pd="1",pi="100",ps="10",onlyNos="0")
# url_str = str.format(analysis_url, subject="chemistry2", sid="7m6S7MUNMsGO0dOPMzYGNsNI0ufmuYIWW2SEX8yOtVnrrlTQt8g8i9CnFFc2qEn9FmaBzq4URQvuRaPgdajLS4DWIw6k8jxn-2bx4fNmlv9D8-3d")
"""请求头"""
herders = {'authorization': token}
"""请求"""
req = request.Request(url_str, None, herders)
"""响应"""
res = request.urlopen(req)
html = res.read()
print(res.getcode())
print(html.decode("utf-8"))
# print(html[2:len(html) -2])
# json_str = json.dumps(html.decode("utf-8"), ensure_ascii=False)
# print(json_str)
