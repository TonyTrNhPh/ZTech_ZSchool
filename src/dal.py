from src import db
from src.models import Users, Announcements,Courses, Students, Grades

################################ Account Management #################################
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
    return Courses.query.all

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

    
def get_all_students():
    return Students.query.all()

def add_student(userid,fullname,dateofbirth,gender):
    student = Students(userid=userid,fullname=fullname,dateofbirth=dateofbirth,gender=gender)
    db.session.add(student)
    db.session.commit()

def get_all_grades():
    return Grades.query.all()

def add_grade(studentid,courseid, grade):
    grade = Grades(studentid=studentid,courseid=courseid, grade=grade)
    db.session.add(grade)
    db.session.commit()