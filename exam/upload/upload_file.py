import time
import requests
import os
import threading
from concurrent.futures import ThreadPoolExecutor


# 模拟分发（请求分发）
def upload_files_to_schools(file_folder):
    # 定义多个学校的参数
    # schoolID<---------
    # 100001,100002,100008,100137,100143,179942,179945
    # 182769,184222,184833,184840,185419,186480,186731
    # 185455,185665,185749,185771,186441,186477--------->
    # examID  <------语文：78078   数学：78079    英语：78080   物理：78081 ---->


    schools = [
        {
           'schoolId': '182769',
            'examId': '78080'
        },
        {
           'schoolId': '184222',
            'examId': '78080'
        },
        {
           'schoolId': '184833',
            'examId': '78080'
        },
        {
           'schoolId': '184840',
            'examId': '78080'
        },
        {
           'schoolId': '185419',
            'examId': '78080'
        },
        {
           'schoolId': '186480',
            'examId': '78080'
        },
        {
           'schoolId': '186731',
            'examId': '78080'
        }
        # 可以继续添加更多学校的参数
    ]

    url = 'http://aliyun.dispatch.xinjiaoyu.com/server_exam/exam/upload'
    headers = {
        'Authorization': 'JBY eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ7XCJhY2Nlc3NUb2tlblwiOlwiZDQ5ODEwNzQyMTc1NDE3YTk1MDJmYWE4YjEwZmZlOTZcIixcImlkXCI6NDYyMDY4MyxcInVzZXJuYW1lXCI6XCJva2R5engwMjR0XCIsXCJyZWFsTmFtZVwiOlwi6KKB5rW35rabXCIsXCJtb2JpbGVcIjpudWxsLFwidHlwZUluZm9cIjoxLFwidXNlclR5cGVcIjoxLFwicm9sZUlkXCI6NTYxMDc4LFwicm9sZVR5cGVJZFwiOjUsXCJyb2xlTmFtZVwiOlwi5qCh6ZW_XCIsXCJzY2hvb2xcIjp7XCJzY2hvb2xJZFwiOjE4Mjc2OSxcInNjaG9vbE5hbWVcIjpcIuWMl-S6rOmHkeamnOiLkeiAg-ivleWtpuagoVwiLFwiaXNSZWdpc3RlcmVkXCI6ZmFsc2UsXCJ0ZWFjaGVySWRcIjozMzcxOTYsXCJzdHVkZW50SWRcIjpudWxsLFwic3R1ZGVudENvZGVcIjpudWxsLFwicGhhc2VJZFwiOjEwMDAwLFwicGhhc2VOYW1lXCI6XCLpq5jkuK1cIixcImNvdXJzZUlkXCI6bnVsbCxcImNvdXJzZU5hbWVcIjpudWxsLFwiZ3JhZGVJZFwiOm51bGwsXCJncmFkZU5hbWVcIjpudWxsLFwiY2xhc3NJZFwiOm51bGwsXCJjbGFzc05hbWVcIjpudWxsLFwicmVsYXRpb25cIjpudWxsLFwicHJvdmluY2VOYW1lXCI6XCLljJfkuqzluIJcIixcInByb3ZpbmNlSWRcIjoxLFwic2Nob29sWWVhck5hbWVcIjpudWxsLFwic3VwcG9ydERvdE1hdHJpeExlc3NvblwiOmZhbHNlfX0iLCJleHAiOjE3Mzg0MjI0MzV9.X4rpXymDS532dHFY7PeVyXO0Wq01KeHNfPF1wnpLCj4',
        'accessToken': 'd49810742175417a9502faa8b10ffe96',
        'client': 'front',
        'clientSession': '1697461103030sjZNpc61FE',
        'encrypt': '839c19536e6b6076f9636f03ea524cae',
        't': '1735830453522'
    }

    def upload_file(file_path, school_params):
        time.sleep(1)
        file_name = os.path.basename(file_path)
        dir_name = file_name[:-4]
        data = {
            'schoolId': school_params['schoolId'],
            'examId': school_params['examId'],
            'stuId': dir_name,
            'envFlag': 'pre',
            'is_check': '0',
            'thirdExam': '1',
            'cutImage': '1',
            'scanBatch': '20241206093723',
            'scanTime': '1733362649659',
            'equipmentCode': '177A22370390A2',
            'scanNumber': '1',
        }
        try:
            with open(file_path, 'rb') as f:
                files = {
                    'file': (file_name, f)
                }
                count = 1
                while True:
                    response = requests.post(url, headers=headers, files=files, data=data)
                    if response.status_code == 200:
                        print(f'学校 {school_params["schoolId"]} 的ZIP文件 {file_name} 上传成功')
                        print('服务器响应内容:', response.text)
                        break
                    if count == 10:
                        print(f'学校 {school_params["schoolId"]} 的ZIP文件 {file_name} 尝试10次仍上传失败')
                        break
                    else:
                        count += 1
                        print(f"重试{count}次")
                        # 睡眠指定的毫秒数
                        time.sleep(0.5)
                        continue
        except requests.RequestException as e:
            print(f'学校 {school_params["schoolId"]} 上传文件 {file_name} 时发生网络请求错误: {str(e)}')
        except Exception as e:
            print(f'学校 {school_params["schoolId"]} 上传文件 {file_name} 时发生其他错误: {str(e)}')

    def process_school(school):
        file_paths = []
        for root, dirs, files in os.walk(file_folder):
            for file in files:
                file_path = os.path.join(root, file)
                file_paths.append(file_path)

        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.map(lambda p: upload_file(p, school), file_paths)

    # 创建并启动线程
    threads = []
    for school in schools:
        thread = threading.Thread(target=process_school, args=(school,))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    file_folder = "C:\\Users\\yibo_\\Desktop\\模拟分发上传\\英语zip\\174231\\45753"
    upload_files_to_schools(file_folder)