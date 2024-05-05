from flask import render_template, request, redirect, url_for, session
from src import app, lm
from src.models import Users, Announcements, Teachers, Courses, Grades, Students
from flask_login import login_user, logout_user, login_required, current_user
from src import dal
from datetime import datetime

def limit_words(s, n):
    words = s.split()
    return ' '.join(words[:n])

app.jinja_env.filters['limit_words'] = limit_words

@app.route('/changepassword', methods=['POST'])
def change_password():
    print("dong 16")
    userid = current_user.userid
    my_password = current_user.password
    old_password = request.form['old_password']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']
    if my_password != old_password:
        session['message'] = "Passwords do not match"
    else:
        if new_password != confirm_password:
            session['message'] = "Confirm your password again"
        else:
            dal.change_password(userid, new_password)
            session['message'] = "Your password has been changed"
    return redirect(request.referrer)


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
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
            session['message'] = "Invalid username or password"
    if session.get('message'):
        message = session['message']
        session['message'] = None
    else:
        message = None
    return render_template('login.html', message=message)


@app.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for("index"))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/news', methods=['GET'])
def news():
    announcements = dal.get_active_announcements()
    return render_template('news.html', announcements=announcements)

@app.route('/announcements/<int:announcement_id>')
def announcement_details(announcement_id):
    announcement = dal.get_announcement_details(announcement_id)  
    return render_template('new_details.html', announcement=announcement)


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
                pass
            case 'update':
                pass
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
                pass
            case 'update':
                pass
        return render_template('grade-management.html', grades=grades)

    return render_template('grade-management.html', grades=grades)


@app.route('/announcements', methods=['GET', 'POST'])
def announcements():
    announcements = dal.get_active_announcements()
    message = None
    if request.method == 'POST':
        action = request.form['hanhdong']
        match action:
            case 'create':
                userid = current_user.userid
                title = request.form['titleCreate']
                description = request.form['descriptionCreate']
                who = request.form['whoCreate']
                date = datetime.now()
                print(userid, title, description, who, date)
                dal.add_announcement(userid,title, description,who,date)
            case 'delete':
                announcementid = request.form['announcementidUpdate']
                dal.delete_announcement(announcementid)
            case 'update':
                announcementid = request.form['announcementidUpdate']
                userid = current_user.userid
                new_title = request.form['titleUpdate']
                new_description = request.form['descriptionUpdate']
                who = request.form['whoUpdate']
                published = int(request.form['publishedUpdate'])
                date = request.form['dateUpdate']
                dal.update_announcement(announcementid,userid,new_title, new_description,who,date,published)
        return redirect(url_for('announcements'))
    return render_template('announcements.html', announcements=announcements, message=message)

# @app.route('/announcements/editor')
# def edit_announcement():
#     content = None
#     if content == None:
#         return render_template('editor.html')
#     else:
#         return announcements(content=content)

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
