from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', courses=courses, selected_courses=selected_courses)

@app.route('/select_course', methods=['POST'])
def select_course():
    course_id = int(request.form['course_id'])
    selected_course = next((course for course in courses if course['id'] == course_id), None)
    if selected_course:
        selected_courses.append(selected_course)
    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('index'))
        else:
            return "Invalid username or password. Please try again."
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        students_id = request.form['students_id']
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')
