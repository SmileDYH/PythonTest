# coding: utf-8
import warnings
warnings.filterwarnings('ignore')
from urllib import request
import urllib.request
import json

def get(token, url):
            """请求头"""
            herders = {'authorization': token}
            """请求"""
            req = request.Request(url, None, herders)
            """响应"""
            res = request.urlopen(req)
            html = res.read()
            print(res.getcode())

            return html.decode("utf-8")

def post(token, url, data):
            """请求头"""
            herders = {'authorization': token}
            """请求"""
            if (token != None):
                req = request.Request(url, data, herders)
            else:
                req = request.Request(url, data)
            """响应"""
            res = request.urlopen(req)
            html = res.read()
            print(res.getcode())

            return html.decode("utf-8")


def post_new(url, params):
    params = json.dumps(params)
    headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}
    # 用bytes函数转换为字节
    params = bytes(params, 'utf8')

    req = urllib.request.Request(url=url, data=params, headers=headers, method='POST')
    response = urllib.request.urlopen(req).read()
    return response.decode('utf-8')
