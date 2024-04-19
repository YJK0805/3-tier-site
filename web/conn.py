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
def register_user(student_name, student_id, student_department, student_class, password):
    conn = pymysql.connect(**db_settings)
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO students (student_name, student_id, department, student_class, password) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (student_name, student_id, student_department, student_class, password))
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

# 獲取學生所選課程及上課時間
def get_student_course_schedule(student_id):
    conn = pymysql.connect(**db_settings)
    try:
        with conn.cursor() as cursor:
            sql = """
                SELECT 
                    course.course_code, course.course_name, course.department, 
                    coursetime.day_of_week, coursetime.start_period, coursetime.end_period
                FROM 
                    selected_course
                JOIN 
                    course ON selected_course.selected_course_code = course.course_code
                JOIN 
                    coursetime ON course.course_code = coursetime.course_code
                WHERE 
                    selected_course.student_id = %s
            """
            cursor.execute(sql, (student_id,))
            student_schedule = cursor.fetchall()
    finally:
        conn.close()
    return student_schedule

# 獲取學生科系
def get_student_department(student_class):
    conn = pymysql.connect(**db_settings)
    try:
        with conn.cursor() as cursor:
            sql = "SELECT department FROM course WHERE class_name = %s LIMIT 1"
            cursor.execute(sql, (student_class,))
            department = cursor.fetchone()
    finally:
        conn.close()
    return department[0]

# 更新學生學分數
def update_student_credit(student_id):
    conn = pymysql.connect(**db_settings)
    try:
        with conn.cursor() as cursor:
            sql = """
                SELECT 
                    SUM(credits_selected) 
                FROM 
                    selected_course 
                WHERE 
                    student_id = %s
            """
            cursor.execute(sql, (student_id,))
            total_credit = cursor.fetchone()
            sql = "UPDATE students SET credits_selected = %s WHERE student_id = %s"
            cursor.execute(sql, (total_credit[0], student_id))
        conn.commit()
    finally:
        conn.close()

def search_courses(course_code, course_name, day, period, instructor):
    conn = pymysql.connect(**db_settings)
    try:
        with conn.cursor() as cursor:
            sql = """
                SELECT 
                    course.course_code, course.course_name, course.credits, course.compulsory, 
                    course.class_name, coursetime.day_of_week, 
                    CONCAT(coursetime.start_period, '-', coursetime.end_period) AS course_time, 
                    course.instructor, 
                    course.enrolled_students,
                    course.total_students
                FROM 
                    course 
                LEFT JOIN 
                    coursetime ON course.course_code = coursetime.course_code
                LEFT JOIN 
                    selected_course ON course.course_code = selected_course.selected_course_code
                WHERE 
                    (%s = '' OR course.course_code = %s)
                    AND (%s = '' OR course.course_name LIKE %s)
                    AND (%s = '' OR coursetime.day_of_week = %s)
                    AND (%s = '' OR coursetime.start_period <= %s AND coursetime.end_period >= %s)
                    AND (%s = '' OR course.instructor = %s)
                GROUP BY 
                    course.course_code
            """
            cursor.execute(sql, (course_code, course_code, course_name, f'%{course_name}%', day, day, period, period, period, instructor, instructor))
            search_results = cursor.fetchall()
    finally:
        conn.close()
    return search_results

def add_focus_course(student_id, course_code):
    conn = pymysql.connect(**db_settings)
    try:
        with conn.cursor() as cursor:
            # 檢查學生是否存在
            cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
            student = cursor.fetchone()
            if not student:
                return False, "Student not found"
            # 檢查課程是否存在
            cursor.execute("SELECT * FROM course WHERE course_code = %s", (course_code,))
            course = cursor.fetchone()
            if not course:
                return False, "Course not found"
            # 檢查學生是否已經選過該課程
            cursor.execute("""
                SELECT * FROM selected_course WHERE student_id = %s AND selected_course_code = %s
            """, (student_id, course_code))
            existing_selected_course = cursor.fetchone()
            if existing_selected_course:
                return False, "Student has already selected this course"
            # 檢查學生是否已經關注過該課程
            cursor.execute("""
                SELECT * FROM focus WHERE student_id = %s AND focused_course_code = %s
            """, (student_id, course_code))
            existing_focus = cursor.fetchone()
            if existing_focus:
                return False, "Student has already focused on this course"
            # 將課程添加到 focus 資料表中
            cursor.execute("""
                INSERT INTO focus (student_id, student_class, student_name, focused_course_code)
                VALUES (%s, %s, %s, %s)
            """, (student_id, student[3], student[0], course_code))
            conn.commit()
            return True, "Course added to focus successfully"
    except pymysql.Error as e:
        return False, str(e)
    finally:
        conn.close()

def get_student_focus_courses(student_id):
    conn = pymysql.connect(**db_settings)
    try:
        with conn.cursor() as cursor:
            sql = """
                SELECT course.course_code, course.course_name, course.department, course.grade,
                       course.class_name, course.credits, course.compulsory,
                       course.total_students, course.enrolled_students, course.instructor
                FROM focus
                JOIN course ON focus.focused_course_code = course.course_code
                WHERE focus.student_id = %s
            """
            cursor.execute(sql, (student_id,))
            focus_courses = cursor.fetchall()
    finally:
        conn.close()
    return focus_courses

def add_course_in(student_id, course_code):
    conn = pymysql.connect(**db_settings)
    try:
        with conn.cursor() as cursor:
            # 檢查學生是否存在
            cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
            student = cursor.fetchone()
            if not student:
                return False, "Student not found"
            # 檢查課程是否存在
            cursor.execute("SELECT * FROM course WHERE course_code = %s", (course_code,))
            course = cursor.fetchone()
            if not course:
                return False, "Course not found"
            # 檢查學生是否已經選過該課程或是有相同名稱之課程
            cursor.execute("""
            SELECT * FROM selected_course WHERE student_id = %s AND selected_course_code = %s OR student_id = %s AND selected_course_code IN (SELECT course_code FROM course WHERE course_name = %s)
            """, (student_id, course_code, student_id, course[1]))
            existing_selected_course = cursor.fetchone()
            if existing_selected_course:
                return False, "Student has already selected this course"
            # 將課程添加到 selected_course 資料表中
            cursor.execute("""
                INSERT INTO selected_course (student_id, student_name, student_class, credits_selected, selected_course_code)
                VALUES (%s, %s, %s, %s, %s)
            """, (student_id, student[0], student[3], course[5], course_code))
            conn.commit()
            cursor.execute("""
                UPDATE course SET enrolled_students = enrolled_students + 1 WHERE course_code = %s
            """, (course_code,))
            conn.commit()
            cursor.execute("""
                UPDATE students SET credits_selected = credits_selected + %s WHERE student_id = %s
            """, (course[5], student_id))
            conn.commit()
            cursor.execute("""
                DELETE FROM focus WHERE student_id = %s AND focused_course_code = %s
            """, (student_id, course_code))
            conn.commit()
            return True, "Course added to selected_course successfully"
    except pymysql.Error as e:
        return False, str(e)
    finally:
        conn.close()

def delete_focus(student_id, course_code):
    conn = pymysql.connect(**db_settings)
    try:
        with conn.cursor() as cursor:
            # 檢查學生是否存在
            cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
            student = cursor.fetchone()
            if not student:
                return False, "Student not found"
            # 檢查課程是否存在
            cursor.execute("SELECT * FROM course WHERE course_code = %s", (course_code,))
            course = cursor.fetchone()
            if not course:
                return False, "Course not found"
            # 檢查學生是否已經關注過該課程
            cursor.execute("""
                SELECT * FROM focus WHERE student_id = %s AND focused_course_code = %s
            """, (student_id, course_code))
            existing_focus = cursor.fetchone()
            if not existing_focus:
                return False, "Student has not focused on this course"
            # 刪除 focus 資料表中的課程
            cursor.execute("""
                DELETE FROM focus WHERE student_id = %s AND focused_course_code = %s
            """, (student_id, course_code))
            conn.commit()
            return True, "Course deleted from focus successfully"
    except pymysql.Error as e:
        return False, str(e)
    finally:
        conn.close()
