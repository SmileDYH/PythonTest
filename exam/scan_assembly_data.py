# 组装数据
from utils import database_util


# 插入题卡表，返回主键id；paper_id 是 exam_course_relation_id
def insert_exam_answer_sheet(exam_id, paper_id, school_id, class_id, class_name, course_id, course_name, student_id,
                             exam_code, abnormal_flag):
    print('insert_exam_answer_sheet')
    # 定义变量
    table_name = 'exam_answer_sheet_' + str(exam_id % 64)  # 分表取余
    # 正常题卡，identify_status=1 and risk_level=0；异常题卡，identify_status=0，risk_level=非0
    if abnormal_flag:
        risk_level = '0'  # 异常状态：0正常
        identify_status = 1  # 识别状态:0-未识别；1-已识别
    else:
        risk_level = '3'  # 异常状态：0正常
        identify_status = 0  # 识别状态:0-未识别；1-已识别
    # 默认值
    student_code_photo = None  # 答题卡所属学生学号上传图片
    exam_code2 = None  # 考号2
    student_code_photo2 = None  # 答题卡所属学生学号上传图片2
    student_name_photo = 'https://oss.xinjiaoyu.com/exam/test/182769/23266/041A24192329AZ_20241015124012_0631/student_name.jpg'  # 题卡姓名区域图片路径
    raw_scan = 'https://oss.xinjiaoyu.com/exam/test/182769/23266/041A24192329AZ_20241015124012_0631/041A24192329AZ_20241015124012_0631_page_041A24192329AZ_20241015124012_0631_page.jpg,https://oss.xinjiaoyu.com/exam/test/182769/23266/041A24192329AZ_20241015124012_0631/041A24192329AZ_20241015124012_0631_page_041A24192329AZ_20241015124012_0632_page.jpg'  # 原始答题卡扫描文件
    recycle = 0  # 是否是回收站 1是
    missing_status = 0  # 是否为缺考：0未缺考，1缺考
    gray_zone = 'https://oss.xinjiaoyu.com/exam/test/182769/23266/041A24192329AZ_20241015124012_0633/001_page_grayZone.jpg'  # 遮盖学号图片路径
    resolve_scan = 'https://oss.xinjiaoyu.com/exam/test/182769/23266/041A24192329AZ_20241015124012_0633/001_page_min.jpg,https://oss.xinjiaoyu.com/exam/test/182769/23266/041A24192329AZ_20241015124012_0633/002_page_min.jpg'  # 识别调整后的图片
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


# 插入考试答题记录 paper_id 是 exam_course_relation_id
def insert_exam_answer_sheet_question(sheet_id, exam_id, paper_id, course_id, school_id, student_id, template_question_id,
                                      question_id, question_number, question_order, is_subjective, type_detail_id):
    # 定义变量
    table_name = 'exam_answer_sheet_question_' + str(exam_id % 256)
    # 默认值
    raw_scan = None  # 原始*题目区域*扫描文件
    is_white = 1  # 主观题是否未答:1已答题，0未答题
    status = 0  # 是否批改完成 (0: False, 1: True)
    risk_level = '0'  # 异常类型
    choose_quest = 0  # 选考题学生是否选做：0选考题学生没选或非选考题，1选考题学生选
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