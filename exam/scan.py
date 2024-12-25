import sys
from utils import database_util


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
    print(query)
    exam_course_relation = database_util.get_database_connection(query, 'exam_course_relation', None, 'select_one')

    # 获取 exam_paper
    query = """
            SELECT id 
            FROM exam_paper where exam_id = 
            """ + str(exam_id) + ' and course_id = ' + str(course_id)
    print(query)
    exam_paper = database_util.get_database_connection(query, 'exam_paper', None, 'select_one')

    # 获取 exam_student_
    table_name = "exam_student_" + str(exam_id % 64)
    query = """
            SELECT class_id, class_name, course_id, course_name, student_id, exam_code 
            FROM 
            """ + table_name + ' where exam_id =' + str(exam_id) + ' and paper_id = ' + str(exam_course_relation[0]) \
            + ' and school_id = ' + str(school_id)
    print(query)
    exam_student_list = database_util.get_database_connection(query, 'exam_paper', None, 'select_batch')
    print(exam_student_list)
    # 校验，学生数不大于10，防止跑死数据库（10 * 题目数）
    if len(exam_student_list) > 15:
        print("学生数量大于10")
        return

    # 打印查询结果, paper_id 是 exam_course_relation_id
    for row in exam_student_list:
        print(row)
        insert_exam_answer_sheet(exam_id, {exam_paper[0]}, school_id, {row[0]}, {row[1]}, {row[2]}, {row[3]},
                                 {row[4]}, {row[5]})


# 插入题卡表
def insert_exam_answer_sheet(exam_id, paper_id, school_id, class_id, class_name, course_id, course_name, student_id,
                             exam_code):
    print('insert_exam_answer_sheet')
    # todo 先把这里都赋值，大概就知道工作量，默认的赋默认值，需要上传图片等都写死，后期优化
    # 定义变量
    table_name = 'exam_answer_sheet_' + str(exam_id % 64)  # 分表取余
    # 默认值
    student_code_photo = None  # 答题卡所属学生学号上传图片
    exam_code2 = None  # 考号2
    student_code_photo2 = None  # 答题卡所属学生学号上传图片2
    student_name_photo = 'https://oss.xinjiaoyu.com/exam/test/182769/23266/041A24192329AZ_20241015124012_0631/student_name.jpg'  # 题卡姓名区域图片路径
    raw_scan = 'https://oss.xinjiaoyu.com/exam/test/182769/23266/041A24192329AZ_20241015124012_0631/041A24192329AZ_20241015124012_0631_page_041A24192329AZ_20241015124012_0631_page.jpg,https://oss.xinjiaoyu.com/exam/test/182769/23266/041A24192329AZ_20241015124012_0631/041A24192329AZ_20241015124012_0631_page_041A24192329AZ_20241015124012_0632_page.jpg'  # 原始答题卡扫描文件
    identify_status = 1  # 识别状态:0-未识别；1-已识别
    recycle = 0  # 是否是回收站 1是
    missing_status = 1  # 是否为缺考：0未缺考，1缺考
    gray_zone = 'https://oss.xinjiaoyu.com/exam/test/182769/23266/041A24192329AZ_20241015124012_0633/001_page_grayZone.jpg'  # 遮盖学号图片路径
    resolve_scan = 'https://oss.xinjiaoyu.com/exam/test/182769/23266/041A24192329AZ_20241015124012_0633/001_page_min.jpg,https://oss.xinjiaoyu.com/exam/test/182769/23266/041A24192329AZ_20241015124012_0633/002_page_min.jpg'  # 识别调整后的图片
    risk_level = '0'  # 异常状态：0正常
    subject_score = None  # 手工输入：主观得分
    object_score = None  # 手工输入：客观题得分
    collect_status = 0  # 是否补录。0否，1是
    cheat_status = 0  # 是否作弊0 否 1 是
    collect_small_question = 0  # 补录是否有小题：0没有，1有
    unknown_type = 0  # 题卡状态，0正常
    create_by = 1

    # 向 exam_answer_sheet_* 插入默认值
    insert_exam_answer_sheet_query = 'INSERT INTO ' + table_name + """ 
     (
        exam_id, paper_id, school_id, class_id, class_name,
        course_id, course_name, student_id, exam_code, student_code_photo,
        exam_code2, student_code_photo2, student_name_photo, raw_scan,
        identify_status, recycle, missing_status, gray_zone, resolve_scan,
        risk_level, subject_score, object_score, collect_status, cheat_status,
        collect_small_question, unknown_type, create_by
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    # 数据元组
    data = (
        exam_id, paper_id, school_id, class_id, class_name,
        course_id, course_name, student_id, exam_code, student_code_photo,
        exam_code2, student_code_photo2, student_name_photo, raw_scan,
        identify_status, recycle, missing_status, gray_zone, resolve_scan,
        risk_level, subject_score, object_score, collect_status, cheat_status,
        collect_small_question, unknown_type, create_by
    )
    print(insert_exam_answer_sheet_query)
    # 执行插入操作
    database_util.get_database_connection(insert_exam_answer_sheet_query, table_name, data, 'insert_batch')


# 插入考试答题记录
def insert_exam_answer_sheet_question(exam_id, course_id, cursor):
    # 获取新插入记录的 ID
    sheet_id = cursor.lastrowid  # 这个是之前从 exam_answer_sheet_58 表插入记录后得到的 sheet_id
    table_name = 'exam_answer_sheet_question_' + ''
    # 向 exam_answer_sheet_question_* 插入默认值
    # 定义插入数据所需的变量
    exam_id = 1
    paper_id = 1
    course_id = 1
    school_id = 1
    student_id = None  # 如果没有学生 ID，可以设置为 None
    raw_scan = 'default_question_scan_path'
    template_question_id = None  # 如果没有模板题目 ID，设置为 None
    question_id = 1
    question_number = 'Q1'
    is_white = 1
    question_order = 1
    total_score = 10.0
    status = 0  # 0 表示未批改
    risk_level = '0'
    choose_quest = 1
    is_subjective = 0
    type_detail_id = 0
    total_math_score = 0.0
    split_status = 0
    create_by = 1
    # 定义 SQL 插入查询语句
    insert_exam_answer_sheet_question_query = """
    INSERT INTO exam_answer_sheet_question_2 (
        sheet_id, exam_id, paper_id, course_id, school_id, student_id,
        raw_scan, template_question_id, question_id, question_number,
        is_white, question_order, total_score, status, risk_level,
        choose_quest, is_subjective, type_detail_id, total_math_score,
        split_status, create_by
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    # 创建数据元组
    data = (
        sheet_id, exam_id, paper_id, course_id, school_id, student_id,
        raw_scan, template_question_id, question_id, question_number,
        is_white, question_order, total_score, status, risk_level,
        choose_quest, is_subjective, type_detail_id, total_math_score,
        split_status, create_by
    )
    # 执行插入操作
    database_util.get_database_connection(insert_exam_answer_sheet_question_query, table_name, data, 'insert_batch')


if __name__ == "__main__":
    # insert_default_values(sys.argv[0], sys.argv[1])
    insert_default_values(12494, 10007, 100001)

# 脚本
# 1、安装解释器 xxx, 配置环境变量
# 2、安装mysql xxx（pip/python）
# 3、执行脚本 python script.py arg1 arg2（考试id,科目id）

