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