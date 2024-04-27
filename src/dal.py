from src import db
from src.models import Users, Courses, Students, Grades
def get_all_users():
    return Users.query.all()

def add_user(username, password, usertype):
    user = Users(username, password, usertype)
    db.session.add(user)
    db.session.commit()
    
def get_all_courses():
    return Courses.query.all()

def add_course(coursename,teacherid):
    course = Courses(coursename,teacherid)
    db.session.add(course)
    db.session.commit()
    
def get_all_students():
    return Students.query.all()

def add_student(userid,fullname,dateofbirth,gender):
    student = Students(userid,fullname,dateofbirth,gender)
    db.session.add(student)
    db.session.commit()

def get_all_grades():
    return Grades.query.all()

def add_grade(studentid,courseid, grade):
    grade = Grades(studentid,courseid, grade)
    db.session.add(grade)
    db.session.commit()