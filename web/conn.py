import pymysql

# 資料庫連接設定
db_settings = {
    "host": "localhost",
    "port": 3306,
    "user": "admin",
    "password": "passwd",
    "db": "testdb",
    "charset": "utf8mb4",
}

# 註冊新用戶
def register_user(student_name, student_id, student_class, password):
    conn = pymysql.connect(**db_settings)
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO students (student_name, student_id, student_class, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (student_name, student_id, student_class, password))
        conn.commit()
    finally:
        conn.close()

# 驗證用戶登入
def authenticate_user(student_id, password):
    conn = pymysql.connect(**db_settings)
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM students WHERE student_id = %s AND password = %s"
            cursor.execute(sql, (student_id, password))
            result = cursor.fetchone()
            if result:
                return True
            else:
                return False
    finally:
        conn.close()

def insert_required_and_same_class_courses(student_id, student_name, student_class):
    conn = pymysql.connect(**db_settings)
    try:
        with conn.cursor() as cursor:
            # 選擇必修及相同班級的課程的 SQL 語句
            sql = "SELECT course_code, credits FROM course WHERE compulsory = 'R' AND class_name = %s"
            cursor.execute(sql, (student_class),)
            courses = cursor.fetchall()
            print(courses)
            # 插入選課記錄的 SQL 語句
            insert_sql = "INSERT INTO selected_course (student_id, student_name, student_class, credits_selected, selected_course_code) VALUES (%s, %s, %s, %s, %s)"
            # 插入每門課程
            for course in courses:
                cursor.execute(insert_sql, (student_id, student_name, student_class, course[1], course[0]))
        conn.commit()
    finally:
        conn.close()

# 從資料庫中獲取學生的選課記錄
def get_student_courses(student_id):
    conn = pymysql.connect(**db_settings)
    try:
        with conn.cursor() as cursor:
            # 查詢學生的選課記錄的 SQL 語句
            sql = "SELECT * FROM selected_course WHERE student_id = %s"
            cursor.execute(sql, (student_id,))
            student_courses = cursor.fetchall()
    finally:
        conn.close()
    return student_courses

