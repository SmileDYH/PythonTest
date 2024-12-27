import sys
from utils import database_util
from exam import scan_assembly_data

# 定义变量
# 1. 查询（链接数据库）
# 2. 拼装数据
# 3. 保存/修改 exam_answer_sheet、exam_answer_sheet_question、 exam_course_relation表

# 扫描识别，各种校验后面再补充，先把主流程跑通
def insert_default_values(exam_id, course_id, school_id):
    # 获取 exam_course_relation, 校验表不为空，且状态为4
    query = """
            SELECT id, state 
            FROM exam_course_relation where exam_id = 
            """ + str(exam_id) + ' and course_id = ' + str(course_id)
    print('1. ' + query)
    exam_course_relation = database_util.get_database_connection_pymysql(query, 'exam_course_relation', None, 'select_one')

    # 获取 exam_paper
    query = """
            SELECT id 
            FROM exam_paper where exam_id = 
            """ + str(exam_id) + ' and course_id = ' + str(course_id)
    print('2. ' + query)
    exam_paper = database_util.get_database_connection_pymysql(query, 'exam_paper', None, 'select_one')

    # 获取 exam_student_
    table_name = "exam_student_" + str(exam_id % 64)
    query = """
            SELECT class_id, class_name, course_id, course_name, student_id, exam_code 
            FROM 
            """ + table_name + ' where exam_id =' + str(exam_id) + ' and paper_id = ' + str(exam_course_relation['id']) \
            + ' and school_id = ' + str(school_id)
    print('3. ' + query)
    exam_student_list = database_util.get_database_connection_pymysql(query, 'exam_paper', None, 'select_batch')
    print(exam_student_list)
    # 元组改字典
    # for row in exam_student_list:
    #     print(row['class_id'])
        # print(row[0])
    # 校验，学生数不大于10，防止跑死数据库（10 * 题目数）
    if len(exam_student_list) > 15:
        print("学生数量大于10")
        return

    # 获取 exam_paper_question
    query = """
            SELECT id, question_id, question_number, question_order, is_subjective, type_detail_id 
            FROM exam_paper_question
            """ + ' where paper_id = ' + str(exam_paper['id'])
    print('4. ' + query)
    exam_paper_question_list = database_util.get_database_connection_pymysql(query, 'exam_paper_question', None, 'select_batch')

    # 循环保存题卡，小题题卡， paper_id 是 exam_course_relation_id ！！！
    for row in exam_student_list:
        # 插入题卡
        print(row)
        primary_id = scan_assembly_data.insert_exam_answer_sheet(exam_id, exam_course_relation['id'], school_id,
                                                                 row['class_id'],  row['class_name'], row['course_id'],
                                                                 row['course_name'], row['student_id'], row['exam_code'], True)
        print("primary_id" + str(primary_id))
        # 插入小题 template_question_id = paperQuestionId
        for row1 in exam_paper_question_list:
            print(row1)
            scan_assembly_data.insert_exam_answer_sheet_question(primary_id, exam_id, exam_course_relation['id'],
                                                                 course_id, school_id, row['student_id'], row1['id'], row1['question_id'],
                                                                 row1['question_number'], row1['question_order'],
                                                                 row1['is_subjective'], row1['type_detail_id'])
    print('5. ')

    # exam_student_ 表状态更新 paper_id 是 exam_course_relation_id ！！！
    table_name = "exam_student_" + str(exam_id % 64)
    update_query = 'update ' + table_name + """ set scan_status = 1 where paper_id = """ + str(exam_course_relation['id'])
    print('6. ' + update_query)
    database_util.get_database_connection(update_query, table_name, None, 'update_one')

    # 更新exam_student_statistics_info应考统计数据 paper_id 是 exam_course_relation_id ！！！
    update_query = """
            update exam_student_statistics_info set reality_number =
            """ + str(len(exam_student_list)) + ', unknown_number = 0 where paper_id = ' + str(exam_course_relation['id'])
    print('7. ' + update_query)
    database_util.get_database_connection(update_query, 'exam_student_statistics_info', None, 'update_one')
    # exam_course_relation，更新扫描完成状态 【7.扫描完成】
    update_query = """
            update exam_course_relation set state = 7 where paper_id =
            """ + str(exam_paper['id'])
    print('8. ' + update_query)
    database_util.get_database_connection(update_query, 'exam_course_relation', None, 'update_one')


def test():
    update_query = """
            update exam_student_statistics_info set reality_number = 
            """ + str(11) + ', unknown_number = 0 where paper_id = ' + str(24715)
    database_util.get_database_connection(update_query, 'exam_student_statistics_info', None, 'update_one')


# main方法需要放到最后，要不然调用不到其他方法
if __name__ == "__main__":
    # insert_default_values(sys.argv[0], sys.argv[1])
    insert_default_values(12453, 10010, 182769)
    # test()
    # todo 调用任务分配接口, 怎么自动分配的; 暂不支持拆分题、选做题等

# 脚本
# 1、安装解释器 xxx, 配置环境变量
# 2、安装mysql xxx（pip/python）
# 3、执行脚本 python script.py arg1 arg2（考试id,科目id）

