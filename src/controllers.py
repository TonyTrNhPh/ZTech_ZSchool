from flask import render_template, request, redirect, url_for, session
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
        if user and user.status == 1:
            login_user(user)
            session["permission"]= user.usertype
            return redirect(url_for('index'))
        else:
            return render_template('login.html')
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for("index"))


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


@app.route('/student-management', methods=['GET','POST'])
def student_management():
    students = dal.get_all_students()
    if request.method == 'POST':
        action = request.form['action1']
        print(action)
        match action:
            case 'add':
                userid = request.form['userid']
                fullname = request.form['fullname']
                dateofbirth = request.form['dateofbirth']
                gender = request.form['gender']
                dal.add_student(userid,fullname,dateofbirth,gender)
            case 'delete':
                studentid = request.form['studentid']
                dal.delete_student(studentid)
            case 'update':
                studentid = request.form['studentid']
                new_userid = request.form['userid']
                new_fullname = request.form['fullname']
                new_dateofbirth = request.form['dateofbirth']
                new_gender = request.form['gender']
                dal.update_student(studentid,new_userid,new_fullname,new_dateofbirth,new_gender)
        return render_template('student-management.html', students=students)

    return render_template('student-management.html', students=students)


@app.route('/teacher-management')
def render_template_teacher_management():
    return render_template('teacher-management.html')


@app.route('/course-management', methods=['GET','POST'])
def course_management():
    courses = dal.get_all_courses()
    if request.method == 'POST':
        action = request.form['action1']
        print(action)
        match action:
            case 'add':
                coursename = request.form['coursename']
                teacherid = request.form['teacherid']
                dal.add_course(coursename, teacherid)
            case 'delete':
                courseid = request.form['courseid']
                dal.delete_course(courseid)
            case 'update':
                courseid = request.form['courseid']
                new_coursename = request.form['coursename']
                new_teacherid = request.form['teacherid']
                dal.update_course(courseid, new_coursename, new_teacherid)
        return render_template('course-management.html', courses=courses)

    return render_template('course-management.html', courses=courses)


@app.route('/grade-management', methods=['GET','POST'])
def grade_management():
    grades = dal.get_all_grades()
    if request.method == 'POST':
        action = request.form['action1']
        print(action)
        match action:
            case 'add':
                studentid = request.form['studentid']
                courseid = request.form['courseid']
                grade = request.form['grade']
                dal.add_grade(studentid,courseid, grade)
            case 'delete':
                gradeid = request.form['gradeid']
                dal.delete_grade(gradeid)
            case 'update':
                gradeid = request.form['gradeid']
                new_studentid = request.form['studentid']
                new_courseid = request.form['courseid']
                new_grade = request.form['grade']
                dal.update_grade(gradeid,new_studentid,new_courseid,new_grade)
        return render_template('grade-management.html', grades=grades)

    return render_template('grade-management.html', grades=grades)


@app.route('/announcements')
def announcements():
    return render_template('announcements.html')


@app.route('/accounts', methods=['GET', 'POST'])
def accounts():
    users = dal.get_active_users()
    message = None
    if request.method == 'POST':
        action = request.form['hanhdong']
        print(action)
        
        match action:
            case 'create':
                username = request.form['usernameCreate']
                if not dal.get_user(username):
                    password = 123456
                    usertype = request.form['usertypeCreate']
                    if usertype != None:
                        dal.add_user(username, password, usertype)
                    else:
                        session['message'] = "Empty role"
                else:
                    session['message'] = "Username already exists"
            case 'delete':
                userid = request.form['useridUpdate']
                dal.delete_user(userid)
            case 'update':
                userid = request.form['useridUpdate']
                password = request.form['passwordUpdate']
                usertype = request.form['usertypeUpdate']
                dal.update_user(userid, password, usertype)
        
        return redirect(url_for('accounts'))
    if session.get('message'):
        message = session['message']
        session['message'] = None
    else:
        message = None
    return render_template('accounts.html', users=users, message=message)


@app.route('/teacher-profile')
def render_template_teacher_profile():
    return render_template('teacher-profile.html')
