import sys
from utils import database_util

# 定义变量
# 1. 查询（链接数据库）
# 2. 拼装数据
# 3. 保存/修改 exam_answer_sheet、exam_answer_sheet_question、 exam_course_relation表

# 扫描识别，各种校验后面再补充，先把主流程跑通
def insert_default_values(exam_id, course_id, school_id):
    # todo exam_course_relation，更新扫描完成状态；student表状态更新；exam_student_statistics_info应考统计数据更新
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

    # 获取 exam_paper_question
    query = """
            SELECT id, question_id, question_number, question_order, is_subjective, type_detail_id 
            FROM exam_paper_question
            """ + ' where paper_id = ' + str(exam_paper[0])
    print(query)
    exam_paper_question_list = database_util.get_database_connection(query, 'exam_paper_question', None, 'select_batch')

    # 循环保存题卡，小题题卡， paper_id 是 exam_course_relation_id
    for row in exam_student_list:
        print(row)
        primary_id = insert_exam_answer_sheet(exam_id, exam_paper[0], school_id, row[0], row[1], row[2], row[3], row[4], row[5])
        print("primary_id" + str(primary_id))
        # template_question_id = paperQuestionId
        for row1 in exam_paper_question_list:
            print(row1)
            insert_exam_answer_sheet_question(primary_id, exam_id, exam_paper[0], course_id, school_id, row[5],
                                              row1[0], row1[1], row1[2], row1[3], row1[4], row1[5])

# 插入题卡表，返回主键id
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
    missing_status = 0  # 是否为缺考：0未缺考，1缺考
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
    # 打印数据类型
    # for index, value in enumerate(data):
    #     print(f"Index {index}: Value {value}, Type {type(value)}")
    print(insert_exam_answer_sheet_query)
    # 执行插入操作
    primary_id = database_util.get_database_connection(insert_exam_answer_sheet_query, table_name, data, 'insert_one')
    return primary_id


# 插入考试答题记录
def insert_exam_answer_sheet_question(sheet_id, exam_id, paper_id, course_id, school_id, student_id, template_question_id,
                                      question_id, question_number, question_order, is_subjective, type_detail_id):
    # 定义变量
    table_name = 'exam_answer_sheet_question_' + str(exam_id % 256)
    # 默认值
    raw_scan = None  # 原始*题目区域*扫描文件
    is_white = 1  # 主观题是否未答:1已答题，0未答题
    status = 0  # 是否批改完成 (0: False, 1: True)
    risk_level = '0'  # 异常类型
    choose_quest = 1  # 选考题学生是否选做：0选考题学生没选或非选考题，1选考题学生选
    total_math_score = 0.0  # 数学-填空题批阅总分
    split_status = 0  # 拆分状态:0默认拆分成功，1不成功
    create_by = 1

    # 定义 SQL 插入查询语句
    insert_exam_answer_sheet_question_query = 'INSERT INTO ' + table_name + """ 
     (
        sheet_id, exam_id, paper_id, course_id, school_id, student_id,
        raw_scan, template_question_id, question_id, question_number,
        is_white, question_order, status, risk_level,
        choose_quest, is_subjective, type_detail_id, total_math_score,
        split_status, create_by
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    print(insert_exam_answer_sheet_question_query)

    # 创建数据元组
    data = (
        sheet_id, exam_id, paper_id, course_id, school_id, student_id,
        raw_scan, template_question_id, question_id, question_number,
        is_white, question_order, status, risk_level,
        choose_quest, is_subjective, type_detail_id, total_math_score,
        split_status, create_by
    )
    print(data)
    # 执行插入操作
    database_util.get_database_connection(insert_exam_answer_sheet_question_query, table_name, data, 'insert_one')

# main方法需要放到最后，要不然调用不到其他方法
if __name__ == "__main__":
    # insert_default_values(sys.argv[0], sys.argv[1])
    insert_default_values(12453, 10007, 182769)

# 脚本
# 1、安装解释器 xxx, 配置环境变量
# 2、安装mysql xxx（pip/python）
# 3、执行脚本 python script.py arg1 arg2（考试id,科目id）

