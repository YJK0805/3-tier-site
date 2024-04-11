from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from conn import register_user, authenticate_user, insert_required_and_same_class_courses, get_student_course_schedule, get_student_department, update_student_credit

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

@app.route('/select_course', methods=['POST'])
def select_course():
    # Your course selection logic here
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        student_id = request.form['student_id']
        password = request.form['password']
        if authenticate_user(student_id, password):
            # User authentication successful, log in the user
            user = User(student_id)
            login_user(user)
            print(current_user.id)
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
        return redirect(url_for('login'))
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

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)

