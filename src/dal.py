from src import db
from src.models import Users, Courses, Students, Grades
def get_active_users():
    return Users.query.filter_by(status=1).all()

def get_user(username):
    print(Users.query.filter_by(username=username).first())
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

def get_all_courses():
    return Courses.query.all()

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
    
def delete_student(studentid):
    student = Students.query.get(studentid)
    if student:
        db.session.delete(student)
        db.session.commit()

def update_student(studentid,new_userid,new_fullname,new_dateofbirth,new_gender):
    student = Students.query.get(studentid)
    if student:
        student.userid = new_userid
        student.fullname = new_fullname
        student.dateofbirth = new_dateofbirth
        student.gender = new_gender
        db.session.commit()
        
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
        
