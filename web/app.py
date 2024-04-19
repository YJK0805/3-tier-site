from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from conn import *

app = Flask(__name__)
app.secret_key = 'secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id):
        self.id = id
    def get_id(self):
        return str(self.id)

@login_manager.user_loader
def load_user(user_id):
    # Return the User object for the given user_id
    return User(user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        student_id = request.form['student_id']
        password = request.form['password']
        if authenticate_user(student_id, password):
            # User authentication successful, log in the user
            user = User(student_id)
            login_user(user)
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
        student_department = get_student_department(student_class)
        register_user(student_name, student_id, student_department, student_class, password)
        insert_required_and_same_class_courses(student_id, student_name, student_class)
        update_student_credit(student_id)
        authenticate_user(student_id, password)
        user = User(student_id)
        login_user(user)
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/schedule/<student_id>')
@login_required
def schedule(student_id):
    if current_user.id != student_id:
        return "You are not authorized to view this page."
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

def time_beautify(time):
    time = list(time)
    time[0] = {
        1: '(一)',
        2: '(二)',
        3: '(三)',
        4: '(四)',
        5: '(五)',
    }.get(time[0], '未知')
    if time[1] == time[2]:
        return f"{time[0]}{time[1]}"
    return f"{time[0]}{time[1]}-{time[2]}"

@app.route('/search_course', methods=['GET', 'POST'])
@login_required
def search_course():
    if request.method == 'POST':
        course_code = request.form.get('course_code', '')
        course_name = request.form.get('course_name', '')
        day = request.form.get('course_day', '')
        period = request.form.get('course_period', '')
        instructor = request.form.get('instructor', '')
        search_results = search_courses(course_code, course_name, day, period, instructor)
        modified_search_results = []
        for result in search_results:
            result_list = list(result)
            result_list[4] = '必修' if result_list[4] == 'R' else '選修'
            course_time = get_course_time(result_list[0])
            modified_time = ""
            for time in course_time:
                current_time = time_beautify(time)
                if modified_time == "":
                    modified_time += current_time
                else:
                    modified_time += f", {current_time}"
            result_list[5] = modified_time
            modified_search_results.append(result_list)
        return render_template('search_course.html', search_results=modified_search_results)
    return render_template('search_course.html')

@app.route('/focus_course/<course_code>', methods=['POST'])
@login_required
def focus_course(course_code):
    if request.method == 'POST':
        student_id = current_user.id
        success, message = add_focus_course(student_id, course_code)
        if success:
            return render_template('success.html', message='關注課程成功', destination=url_for('focus_list'))
        else:
            return render_template('error.html', message=message), 400

@app.route('/focus_list')
@login_required
def focus_list():
    # 從資料庫中獲取學生的關注課程列表
    focus_courses = get_student_focus_courses(current_user.id)
    if not focus_courses:
        return render_template('error.html', message='您尚未關注任何課程')
    modified_focus_courses = []
    for course in focus_courses:
        course_list = list(course)
        course_time = get_course_time(course_list[0])
        course_list[4] = '必修' if course_list[4] == 'R' else '選修'
        modified_time = ""
        for time in course_time:
            current_time = time_beautify(time)
            if modified_time == "":
                modified_time += current_time
            else:
                modified_time += f", {current_time}"
        course_list.append(modified_time)
        modified_focus_courses.append(course_list)
    return render_template('course.html', focus_courses=modified_focus_courses)

@app.route('/add_course/<course_code>', methods=['POST'])
@login_required
def add_course(course_code):
    if request.method == 'POST':
        student_id = current_user.id
        success, message = add_course_in(student_id, course_code)
        if success:
            return render_template('success.html', message='選課成功', destination=url_for('schedule', student_id=student_id))
        else:
            return render_template('error.html', message=message), 400

@app.route('/delete_focus_course/<course_code>', methods=['POST'])
@login_required
def delete_focus_course(course_code):
    if request.method == 'POST':
        student_id = current_user.id
        # 從資料庫中刪除學生的關注課程
        success, message = delete_focus(student_id, course_code)
        if success:
            return render_template('success.html', message='刪除關注課程成功', destination=url_for('focus_list'))
        else:
            return render_template('error.html', message=message), 400

@app.route('/course', methods=['GET'])
@login_required
def course():
    all_courses = get_student_selected_courses(current_user.id)
    modified_all_courses = []
    for course in all_courses:
        course_list = list(course)
        course_time = get_course_time(course_list[0])
        course_list[4] = '必修' if course_list[4] == 'R' else '選修'
        modified_time = ""
        for time in course_time:
            current_time = time_beautify(time)
            if modified_time == "":
                modified_time += current_time
            else:
                modified_time += f", {current_time}"
        course_list.append(modified_time)
        modified_all_courses.append(course_list)
    return render_template('course.html', select_course=modified_all_courses)

@app.route('/withdraw_course/<course_code>', methods=['POST'])
@login_required
def withdraw_course(course_code):
    if request.method == 'POST':
        student_id = current_user.id
        success, message = withdraw_course_in(student_id, course_code, 1)
        if success:
            return render_template('success.html', message='退選成功', destination=url_for('schedule', student_id=student_id))
        else:
            if message == 'This is a required course for your class':
                course_info = get_course_info(course_code)
                return render_template('check_withdraw.html', course_info=course_info)
            return render_template('error.html', message=message), 400

@app.route('/check_withdraw/<course_code>', methods=['POST'])
@login_required
def withdraw_course_confirm(course_code):
    if request.method == 'POST':
        confirm = request.form['confirm']
        if confirm == 'yes':
            student_id = current_user.id
            success, message = withdraw_course_in(student_id, course_code, 0)
            if success:
                return render_template('success.html', message='退選成功', destination=url_for('schedule', student_id=student_id))
            else:
                return render_template('error.html', message=message), 400
        else:
            return render_template('success.html', message='已取消退選', destination=url_for('course'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)

