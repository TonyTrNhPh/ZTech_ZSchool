
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from src import app, db, lm

@lm.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)



class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    userid = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    usertype = Column(String(20), nullable=False)
    status = Column(Boolean, default=True)
    announcement = relationship('Announcements', backref='users', lazy=True)

    def __init__(self, username, password, usertype):
        self.username = username
        self.password = password
        self.usertype = usertype
        self.status = True

    def get_id(self):
        return (self.userid)


class Announcements(db.Model):
    __tablename__ = 'announcements'
    announcementid = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey(Users.userid), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(2000), nullable=False)
    who = Column(String(20), nullable=False)
    date = Column(String(30), nullable=False)
    published = Column(Boolean, default=True, nullable=False)
    status = Column(Boolean, default=True)
    
    def __init__(self,userid,title,description,who,date):
        self.userid = userid
        self.title = title
        self.description = description
        self.who = who
        self.date = date
        self.published = True
        self.status = True
        
    def get_id(self):
        return (self.announcementid)
    


class Teachers(db.Model):
    __tablename__ = 'teachers'
    teacherid = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey(Users.userid), nullable=False)
    fullname = Column(String(20), nullable=False)
    department = Column(String(20), nullable=False)
    status = Column(Boolean, default=True)

    def __init__ (self, userid, fullname, department):
        self.userid = userid
        self.fullname = fullname
        self.department = department
        self.status = True
        

class Courses(db.Model):
    __tablename__ = 'courses'
    courseid = Column(Integer, primary_key=True)
    coursename = Column(String(20), nullable=False)
    teacherid = Column(Integer, ForeignKey(Teachers.teacherid), nullable=False)
    status = Column(Boolean, default=True)


class Students(db.Model):
    __tablename__ = 'students'
    studentid = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey(Users.userid), nullable=False)
    fullname = Column(String(20), nullable=False)
    dateofbirth = Column(String(20), nullable=False)
    gender = Column(String(20), nullable=False)
    status = Column(Boolean, default=True)
    
    def __init__ (self, userid, fullname, dateofbirth, gender):
        self.userid = userid
        self.fullname = fullname
        self.dateofbirth = dateofbirth
        self.gender = gender
        self.status = True


class Grades(db.Model):
    __tablename__ = 'grades'
    gradeid = Column(Integer, primary_key=True)
    studentid = Column(Integer, ForeignKey(Students.studentid), nullable=False)
    courseid = Column(Integer, ForeignKey(Courses.courseid), nullable=False)
    grade = Column(Float, nullable=False)
    status = Column(Boolean, default=True)

class Course_documents(db.Model):
    __tablename__ = 'course_documents'
    documentid = Column(Integer, primary_key=True)
    documentname = Column(String(20), nullable=False)
    supplier = Column(String(20), nullable=False)
    year = Column(Integer, nullable=False)
    courseid = Column(Integer, ForeignKey(Courses.courseid), nullable=False)

class Course_feedback(db.Model):
    __tablename__ = "course_feedback"
    feedbackid = Column(Integer, primary_key=True)
    courseid = Column(Integer, ForeignKey(Courses.courseid),nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(100), nullable=False)


class Attendance(db.Model):
    __tablename__ = "attendance"
    attendanceid = Column(Integer, primary_key=True)
    courseid = Column(Integer, ForeignKey(Courses.courseid),nullable=False)
    date = Column(String(20), nullable=False)
    status = Column(String(20), nullable=False)