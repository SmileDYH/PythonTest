# 数据库请求
import mysql.connector
from mysql.connector import Error
# pymysql 或 sqlite3 时，可以设置 cursor 返回字典格式的结果
import pymysql

# 在使用前定义全局变量并赋初始值
result = None
connection = None
cursor = None


# 连接数据库
def get_database_connection(sql, table_name, data, dml):
    global connection, cursor, result
    try:
        print("获取数据库连接")
        # 连接到 MySQL 数据库
        connection = mysql.connector.connect(
            host='rm-8vbb3n2r5a94193wsho.mysql.zhangbei.rds.aliyuncs.com',  # 替换为您的数据库主机
            user='exam',       # 替换为您的用户名
            password='exam123!@#',  # 替换为您的密码
            database='jby_exam'  # 替换为您的数据库名称
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # 获取数据
            execute_sql(sql, table_name, data, dml, cursor)
            # 提交更改
            connection.commit()
            print("数据操作成功。")
    except Error as e:
        print("数据库操作失败：", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return result


# 获取pymysql数据库连接, 可以使用字典等py格式
def get_database_connection_pymysql(sql, table_name, data, dml):
    global connection, cursor, result
    try:
        print("获取数据库连接")
        # 连接到 MySQL 数据库
        connection = pymysql.connect(
            host='rm-8vbb3n2r5a94193wsho.mysql.zhangbei.rds.aliyuncs.com',  # 替换为您的数据库主机
            user='exam',       # 替换为您的用户名
            password='exam123!@#',  # 替换为您的密码
            database='jby_exam'  # 替换为您的数据库名称
        )

        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            # 获取数据
            execute_sql(sql, table_name, data, dml, cursor)
            # 提交更改
            connection.commit()
            print("数据操作成功。")
    except Error as e:
        print("数据库操作失败：", e)
    finally:
        cursor.close()
        connection.close()
    return result


# 执行sql
def execute_sql(sql, table_name, data, dml, cursor):
    global connection, result
    # 获取数据
    if dml == 'select_one':
        result = select_one(sql, table_name, cursor)
    elif dml == 'select_batch':
        result = select_batch(sql, table_name, cursor)
    elif dml == 'insert_one':
        result = insert_one(sql, table_name, data, cursor)
    elif dml == 'update_one':
        update_one(sql, table_name, data, cursor)
    return result


# 单条查询
def select_one(sql, table_name, cursor):
    print('select_one')
    global result
    # 执行查询
    cursor.execute(sql)
    # 获取第一条查询结果
    result = cursor.fetchone()
    if result:
        # 打印第一条查询结果
        # print({result[0]})
        print(list(result.items())[0])
        return result
    else:
        print(table_name + '数据不存在')
        return


# 批量查询
def select_batch(sql, table_name, cursor):
    global result
    # 执行查询
    cursor.execute(sql)
    # 获取查询结果
    result = cursor.fetchall()
    return result


# 批量插入
def insert_one(sql, table_name, data, cursor):
    # 执行插入操作
    cursor.execute(sql, data)
    print(table_name + "保存成功")
    # 这个是之前从 exam_answer_sheet_58 表插入记录后得到的 sheet_id
    return cursor.lastrowid


# 单条更新
def update_one(sql, table_name, data, cursor):
    print('update_one')
    global result
    # 执行查询
    cursor.execute(sql)
    print(table_name + "更新成功")