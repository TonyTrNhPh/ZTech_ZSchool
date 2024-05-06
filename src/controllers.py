import re
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


@app.route('/grades', methods=['GET','POST'])
def grades():
    grades = dal.get_all_grades()
    return render_template('grades.html', grades=grades)


@app.route('/student-profile', methods=['GET','POST'])
def student():
    students = dal.get_student()
    if request.method == 'POST':
        action = request.form['action1']
        print(action)
        match action:
            case 'update':
                studentid = request.form['studentid']
                new_fullname = request.form['fullname']
                new_dateofbirth = request.form['dateofbirth']
                new_gender = request.form['gender']
                dal.update_student1(studentid,new_fullname,new_dateofbirth,new_gender)
        return redirect(url_for('student'))
    return render_template('student-profile.html', students=students)


@app.route('/student-management', methods=['GET','POST'])
def student_management():
    students = dal.get_all_students()
    if request.method == 'POST':
        action = request.form['action1']
        print(action)
        match action:
            case 'add':
                fullname = request.form['fullname']
                dateofbirth = request.form['dateofbirth']
                gender = request.form['gender']
                dal.add_student(fullname,dateofbirth,gender)
            case 'delete':
                studentid = request.form['studentid']
                dal.delete_student(studentid)
            case 'update':
                studentid = request.form['studentid']
                new_fullname = request.form['fullname']
                new_dateofbirth = request.form['dateofbirth']
                new_gender = request.form['gender']
                dal.update_student(studentid,new_fullname,new_dateofbirth,new_gender)
        return redirect(url_for('student_management'))

    return render_template('student-management.html', students=students)


@app.route('/teacher-management', methods=['GET','POST'])
def teacher_management():
    teachers = dal.get_all_teachers()
    if request.method == 'POST':
        action = request.form['action1']
        print(action)
        match action:
            case 'add':
                fullname = request.form['fullname']
                department = request.form['department']
                dal.add_teacher(fullname,department)
            case 'delete':
                teacherid = request.form['teacherid']
                dal.delete_teacher(teacherid)
            case 'update':
                teacherid = request.form['teacherid']
                new_userid = request.form['userid']
                new_fullname = request.form['fullname']
                new_department = request.form['department']
                dal.update_teacher(teacherid,new_userid,new_fullname,new_department)
        return redirect(url_for('teacher_management'))
    
    return render_template('teacher-management.html', teachers=teachers)

@app.route('/course-management', methods=['GET','POST'])
def course_management():
    courses = dal.get_all_courses()
    print(courses)
    if request.method == 'POST':
        action = request.form['action1']
        print(action)
        match action:  # Removed colon here
            case 'add':  # Removed colon here
                coursename = request.form['coursename']
                teacherid = request.form['teacherid']
                dal.add_course(coursename, teacherid)
            case 'delete':  # Removed colon here
                courseid = request.form['courseid']
                dal.delete_course(courseid)
            case 'update':  # Removed colon here
                courseid = request.form['courseid']
                new_coursename = request.form['coursename']
                new_teacherid = request.form['teacherid']
                dal.update_course(courseid, new_coursename, new_teacherid)

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


@app.route('/teacher-profile', methods=['GET', 'POST'])
def teacher():
    teachers = dal.get_teacher()
    if request.method == 'POST':
        action = request.form['action1']
        print(action)
        match action:
            case 'update':
                teacherid = request.form['teacherid']
                new_fullname = request.form['fullname']
                new_department = request.form['department']
                dal.update_teacher1(teacherid,new_fullname,new_department)
        return redirect(url_for('teacher'))
    
    return render_template('teacher-profile.html', teachers=teachers)

@app.route('/course_documents', methods=['GET','POST'])
def course_documents():
    documents = dal.get_all_document()
    if request.method == 'POST':
        action = request.form['action1']
        print(action)
        match action:
            case 'add':
                docname = request.form['documentname']
                supplier = request.form['supplier']
                year = request.form['year']
                courseid = request.form['courseid']

                if not courseid or not supplier or not docname or not year:
                    session['message'] = "Empty role"
                elif len(year) != 4 or not year.isdigit():
                    session['message'] = "Year must be a 4-digit number"
                else:
                    if dal.get_courseid(courseid):    
                        dal.add_doc(docname, supplier, year, courseid)
                    else:
                        session['message'] = "Course ID does not exist"  
            case 'delete':
                docid = request.form['documentid']
                dal.delete_doc(docid)
            case 'update':
                docid = request.form['documentid']
                new_docname = request.form['documentname']
                new_supplier = request.form['supplier']
                new_year = request.form['year']
                new_courseid = request.form['courseid']
                if not new_docname or not new_year or not new_courseid or not new_supplier:
                    session['message'] = "Empty role"
                elif len(new_year) != 4 or not new_year.isdigit():
                    session['message'] = "Year must be a 4-digit number"
                else:
                    if dal.get_courseid(courseid):    
                        dal.update_doc(docid, new_docname,new_supplier, new_year, new_courseid)
                    else:
                        session['message'] = "Course ID does not exist" 
                
        return redirect(url_for('course_documents'))
    if session.get('message'):
        message = session['message']
        session['message'] = None
    else:
        message = None
    return render_template('course_documents.html', documents=documents, message=message)

@app.route('/course_feedback', methods=['GET','POST'])
def course_feedback():
    feedbacks = dal.get_all_feedback()
    if request.method == 'POST':
        action = request.form['action1']
        print(action)
        match action:
            case 'add':
                courseid = request.form['courseid']
                rating = request.form['rating']
                comment = request.form['comment'] 
                if not courseid or not rating or not comment:
                    session['message'] = "Empty role"
                elif int(rating) > 5:
                    session['message'] = "Rating must be less than 5"
                else:
                    if dal.get_courseid(courseid):    
                        dal.add_feedback(courseid, rating, comment)
                    else:
                        session['message'] = "Course ID does not exist"    
            case 'delete':
                feedbackid = request.form['feedbackid']
                dal.delete_feedback(feedbackid)
            case 'update':
                feedbackid = request.form['feedbackid']
                new_courseid = request.form['courseid']
                new_rating = request.form['rating']
                new_comment = request.form['comment']
                if not new_courseid.strip() or not new_rating.strip() or not new_comment.strip():
                    session['message'] = "Empty role"
                elif int(new_rating) > 5:
                    session['message'] = "Rating must be less than 5"
                else:
                    if dal.get_courseid(new_courseid):
                        dal.update_feedback(feedbackid, new_courseid, new_rating, new_comment)
                    else:
                        session['message'] = "Course ID does not exist"    
        return redirect(url_for('course_feedback'))
    if session.get('message'):
        message = session['message']
        session['message'] = None
    else:
        message = None
    return render_template('course_feedback.html', feedbacks=feedbacks, message=message)

@app.route('/attendance', methods=['GET','POST'])
def attendance():
    attendances = dal.get_all_attendance()
    if request.method == 'POST':
        action = request.form['action1']
        print(action)
        match action:
            case 'add':
                courseid = request.form['courseid']
                date = request.form['date']
                status = request.form['status']
                if not courseid or not date or not status:
                    session['message'] = "Empty role"
                else:
                    date_pattern = re.compile(r"\d{4}/\d{2}/\d{2}")
                    if not date_pattern.match(date):
                        session['message'] = "Date must be in yyyy/mm/dd format"    
                    else:
                        if dal.get_courseid(courseid):
                            dal.add_attendance(courseid, date, status)
                        else:
                            session['message'] = "Course ID does not exist"
            case 'delete':
                attendanceid = request.form['attendanceid']
                dal.delete_attendance(attendanceid)
            case 'update':
                attendanceid = request.form['attendanceid']
                new_courseid = request.form['courseid']
                new_date = request.form['date']
                new_status = request.form['status']
                if not new_courseid or not new_date or not new_status:
                    session['message'] = "Empty role"
                else:
                    date_pattern = re.compile(r"\d{4}/\d{2}/\d{2}")
                    if not date_pattern.match(new_date):
                        session['message'] = "Date must be in yyyy/mm/dd format"    
                    else:
                        if dal.get_courseid(new_courseid):
                            dal.update_attendance(attendanceid, new_courseid, new_date, new_status)
                        else:
                            session['message'] = "Course ID does not exist"
                
        return redirect(url_for('attendance'))
    if session.get('message'):
        message = session['message']
        session['message'] = None
    else:
        message = None
    return render_template('attendance.html', attendances=attendances, message=message)
