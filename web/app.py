from flask import Flask, render_template, request, redirect, url_for
from conn import register_user, authenticate_user, insert_required_and_same_class_courses,get_student_course_schedule

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/select_course', methods=['POST'])
def select_course():
    # 這裡是選課功能的程式碼，你可以保留原來的處理方式
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        student_id = request.form['student_id']
        password = request.form['password']
        print("try to login")
        # 驗證用戶登入
        print(student_id, password,authenticate_user(student_id, password))
        if authenticate_user(student_id, password):
            return redirect(url_for('index'))
        else:
            return "Invalid student ID or password. Please try again."
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        student_name = request.form['student_name']
        student_id = request.form['student_id']
        student_class = request.form['student_class']
        password = request.form['password']
        # 註冊新用戶
        register_user(student_name, student_id, student_class, password)
        # 插入必修及相同班級的課程
        insert_required_and_same_class_courses(student_id, student_name, student_class)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/schedule/<student_id>')
def schedule(student_id):
    # 獲取學生的選課記錄
    student_courses = get_student_course_schedule(student_id)
    select_course = []
    for i in range(14):
        select_course.append([""] * 6)
    select_course[0] = ["08:10-09:00", "", "", "", "", ""]
    select_course[1] = ["09:10-10:00", "", "", "", "", ""]
    select_course[2] = ["10:10-11:00", "", "", "", "", ""]
    select_course[3] = ["11:10-12:00", "", "", "", "", ""]
    select_course[4] = ["12:10-13:00", "", "", "", "", ""]
    select_course[5] = ["13:10-14:00", "", "", "", "", ""]
    select_course[6] = ["14:10-15:00", "", "", "", "", ""]
    select_course[7] = ["15:10-16:00", "", "", "", "", ""]
    select_course[8] = ["16:10-17:00", "", "", "", "", ""]
    select_course[9] = ["17:10-18:00", "", "", "", "", ""]
    select_course[10] = ["18:30-19:20", "", "", "", "", ""]
    select_course[11] = ["19:25-20:15", "", "", "", "", ""]
    select_course[12] = ["20:25-21:15", "", "", "", "", ""]
    select_course[13] = ["21:20-22:10", "", "", "", "", ""]
    for code, course_name, department, day, start_time, end_time in student_courses:
        for i in range(start_time, end_time+1):
            select_course[i - 1][int(day)] = course_name
    return render_template('schedule.html', student_courses=select_course)

if __name__ == "__main__":
    app.run(debug=True)

