from flask import render_template, request, redirect, url_for
from src import app, lm
from src.models import Users, Announcements, Teachers, Courses, Grades, Students
from flask_login import login_user, logout_user, login_required, current_user
from src import dal


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(
            username=username, password=password).first()
        print(user)
        if user:
            login_user(user)
            return redirect(url_for('index'))
        else:
            return render_template('login.html')
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/news')
def render_template_news():
    return render_template('news.html')


@app.route('/grades')
def render_template_grades():
    return render_template('grades.html')


@app.route('/student-profile')
def render_template_student_profile():
    return render_template('student-profile.html')


@app.route('/student-management')
def render_template_student_management():
    return render_template('student-management.html')


@app.route('/teacher-management')
def render_template_teacher_management():
    return render_template('teacher-management.html')


@app.route('/course-management')
def render_template_course_management():
    return render_template('course-management.html')


@app.route('/grade-management')
def render_template_grade_management():
    return render_template('grade-management.html')


@app.route('/announcement-management')
def render_template_announcement_management():
    return render_template('announcement-management.html')


@app.route('/accounts', methods=['GET', 'POST'])
def accounts():
    users = dal.get_all_users()
    if request.method == 'POST':
        action = request.form['action2']
        print(action)
        match action:
            case 'add':
                username = request.form['username']
                password = request.form['password']
                usertype = request.form['usertype']
                dal.add_user(username, password, usertype)
            case 'delete':
                pass
            case 'update':
                pass

        return render_template('user-management.html', users=users)

    return render_template('user-management.html', users=users)


@app.route('/teacher-profile')
def render_template_teacher_profile():
    return render_template('teacher-profile.html')
