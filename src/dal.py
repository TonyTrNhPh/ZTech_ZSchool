from src import db
from flask_login import current_user
from src.models import Users, Courses, Students, Grades, Course_feedback, Course_documents, Attendance, Teachers, Announcements
def get_active_users():
    return Users.query.filter_by(status=1).all()

def get_user(username):
    return Users.query.filter_by(username=username).first()

def add_user(username, password, usertype):
    user = Users(username, password, usertype)
    db.session.add(user)
    db.session.commit()

def delete_user(userid):
    user = Users.query.get(userid)
    if user:
        user.status = 0
        db.session.commit()   

def update_user(userid, new_password, new_usertype):
    user = Users.query.get(userid)
    print(user)
    if user:
        user.usertype = new_usertype
        user.password = new_password
        db.session.commit()

def change_password(userid, new_password):
    user = Users.query.get(userid)
    if user:
        print("cung dc cai j")
        user.password = new_password
        db.session.commit()
    
        
################################  Announcements Management #############################
def get_active_announcements():
    return Announcements.query.filter_by(status=1).all()

def get_announcement_details(announcementid):
    return Announcements.query.filter_by(announcementid=announcementid).first()

def add_announcement(userid,title, description,who,date):
    announcement = Announcements(userid,title, description,who,date)
    db.session.add(announcement)
    db.session.commit()           
    
def update_announcement(announcementid,userid,new_title, new_description,who,date,published):
    announcement = Announcements.query.get(announcementid)
    print(announcement)
    if announcement:
        announcement.userid = userid
        announcement.title = new_title
        announcement.description = new_description
        announcement.who = who
        announcement.date = date
        announcement.published = published
        db.session.commit()
        
def delete_announcement(announcementid):
    announcement = Announcements.query.get(announcementid)
    if announcement:
        announcement.status = 0
        db.session.commit() 

################################ Course Management ################################
def get_all_courses():
    return Courses.query.filter_by(status=1).all()


def add_course(coursename,teacherid):
    course = Courses(coursename=coursename,teacherid=teacherid)
    db.session.add(course)
    db.session.commit()
    
def delete_course(courseid):
    course = Courses.query.get(courseid)
    if course:
        db.session.delete(course)
        db.session.commit()

def update_course(courseid, new_coursename, new_teacherid):
    course = Courses.query.get(courseid)
    if course:
        course.coursename = new_coursename
        course.teacherid = new_teacherid
        db.session.commit()
################################################################ Students management #################################
def get_all_students():
    return Students.query.all()

def get_student():
    if current_user.is_authenticated:
        userid = current_user.userid
    return Students.query.filter_by(userid=userid).all()

def add_student(fullname,dateofbirth,gender):
    user = Users(username='',password=dateofbirth,usertype='Sinh viên')
    db.session.add(user)
    db.session.flush()
    student = Students(userid=user.userid,fullname=fullname,dateofbirth=dateofbirth,gender=gender)
    db.session.add(student)
    db.session.flush()
    user.username = student.studentid
    db.session.commit()
    
    
    
def delete_student(studentid):
    student = Students.query.get(studentid)
    user = Users.query.filter_by(userid=student.userid).first()
    if student:
        user.status = 0
        db.session.delete(student)
        db.session.commit()

def update_student(studentid,new_fullname,new_dateofbirth,new_gender):
    student = Students.query.get(studentid)
    if student:
        student.fullname = new_fullname
        student.dateofbirth = new_dateofbirth
        student.gender = new_gender
        db.session.commit()
################################################################ Grades management #################################################################       
def get_all_grades():
    return Grades.query.all()


def add_grade(studentid,courseid, grade):
    grade = Grades(studentid=studentid,courseid=courseid, grade=grade)
    db.session.add(grade)
    db.session.commit()
    
def delete_grade(gradeid):
    grade = Grades.query.get(gradeid)
    if grade:
        db.session.delete(grade)
        db.session.commit()
        
def update_grade(gradeid,new_studentid,new_courseid,new_grade):
    grade = Grades.query.get(gradeid)
    if grade:
        grade.gradeid =new_studentid
        grade.courseid =new_courseid
        grade.grade = new_grade
        db.session.commit()
        
def get_all_document():
    return Course_documents.query.all()

def add_doc(documentname, supplier, year, courseid):
    doc = Course_documents(documentname= documentname, supplier=supplier, year=year, courseid=courseid)
    db.session.add(doc)
    db.session.commit()

def delete_doc(documentid):
    doc = Course_documents.query.get(documentid)
    if doc:
        db.session.delete(doc)
        db.session.commit()

def update_doc(documentid, new_docname, new_supplier, new_year, new_courseid):
    doc = Course_documents.query.get(documentid)
    if doc:
        doc.documentname = new_docname
        doc.supplier = new_supplier
        doc.year = new_year
        doc.courseid = new_courseid
        db.session.commit()

def get_all_feedback():
    return Course_feedback.query.all()  

def get_courseid(courseid):
    print(Courses.query.filter_by(courseid=courseid).first())
    return Courses.query.filter_by(courseid=courseid).first()

def add_feedback( courseid, rating, comment):
    feedback = Course_feedback( courseid=courseid, rating=rating, comment=comment)
    db.session.add(feedback)
    db.session.commit()   

def delete_feedback(feedbackid):
    feedback = Course_feedback.query.get(feedbackid)
    if feedback:
        db.session.delete(feedback)
        db.session.commit()

def update_feedback(feedbackid, new_courseid, new_rating, new_comment):
    feedback = Course_feedback.query.get(feedbackid)
    if feedback:
        feedback.courseid = new_courseid
        feedback.rating = new_rating
        feedback.comment = new_comment
        db.session.commit()

def get_all_attendance():
    return Attendance.query.all()  

def add_attendance( courseid, date, status):
    attendance = Attendance( courseid=courseid, date=date, status=status)
    db.session.add(attendance)
    db.session.commit()   

def delete_attendance(attendanceid):
    attendance = Attendance.query.get(attendanceid)
    if attendance:
        db.session.delete(attendance)
        db.session.commit()

def update_attendance(attendanceid, new_courseid, new_date, new_status):
    attendance = Attendance.query.get(attendanceid)
    if attendance:
        attendance.courseid = new_courseid
        attendance.date = new_date
        attendance.status = new_status
        db.session.commit()      
################################################################ Teachers management #################################################################  
def get_all_teachers():
    return Teachers.query.all()

def add_teacher(fullname,department):
    user = Users(username='',password=department,usertype='Giáo viên')
    db.session.add(user)
    db.session.flush()
    teacher = Teachers(userid=user.userid,fullname=fullname,department=department)
    db.session.add(teacher)
    db.session.flush()
    user.username = teacher.teacherid
    db.session.commit()
    
def delete_teacher(teacherid):
    teacher =  Teachers.query.get(teacherid)
    if teacher:
        db.session.delete(teacher)
        db.session.commit()
        
def update_teacher(teacherid,new_userid,new_fullname,new_department):
    teacher =  Teachers.query.get(teacherid)
    if teacher:
        teacher.userid = new_userid
        teacher.fullname = new_fullname
        teacher.department = new_department
        db.session.commit()
        
def update_teacher1(teacherid,new_fullname,new_department):
    teacher =  Teachers.query.get(teacherid)
    if teacher:
        teacher.fullname = new_fullname
        teacher.department = new_department
        db.session.commit()
        
def get_teacher():
    if current_user.is_authenticated:
        userid = current_user.userid
    return Teachers.query.filter_by(userid=userid).all()