import xlsxwriter

'''创建工作簿、工作表'''
# 创建工作簿
workbook = xlsxwriter.Workbook('测试文件.xlsx')  # 创建一个excel文件
# 创建工作表
worksheet = workbook.add_worksheet('这是sheet1')  # 在文件中创建一个名为这是sheet1的sheet,不加名字默认为sheet1
# 写入数据
worksheet.write(0, 0, '写点什么好')  # 第1行第1列（即A1）写入
workbook.close()