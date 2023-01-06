# coding: utf-8
from jyw import jyw_request
import xlsxwriter

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
# print(jyw_request.post(None, url, postdata))

'''创建工作簿、工作表'''
# 创建工作簿
workbook = xlsxwriter.Workbook('测试文件.xlsx')  # 创建一个excel文件
# 创建工作表
worksheet = workbook.add_worksheet('这是sheet1')  # 在文件中创建一个名为这是sheet1的sheet,不加名字默认为sheet1
# 写入数据
worksheet.write(0, 0, '写点什么好')  # 第1行第1列（即A1）写入
workbook.close()
