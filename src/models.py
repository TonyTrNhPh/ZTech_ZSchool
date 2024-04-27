
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
    usertype = Column(String(10), nullable=False)
    status = Column(Boolean, default=True)
    announcement = relationship('Announcements', backref='users', lazy=True)

    def __init__(self, username, password, usertype):
        self.username = username
        self.password = password
        self.usertype = usertype
        self.status = True


class Announcements(db.Model):
    __tablename__ = 'announcements'
    announcementid = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey(Users.userid), nullable=False)
    title = Column(String(20), nullable=False)
    discription = Column(String(200), nullable=False)
    date = Column(String(20), nullable=False)
    status = Column(Boolean, default=True)


class Teachers(db.Model):
    __tablename__ = 'teachers'
    teacherid = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey(Users.userid), nullable=False)
    fullname = Column(String(20), nullable=False)
    department = Column(String(20), nullable=False)
    status = Column(Boolean, default=True)


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


class Grades(db.Model):
    __tablename__ = 'grades'
    gradeid = Column(Integer, primary_key=True)
    studentid = Column(Integer, ForeignKey(Students.studentid), nullable=False)
    courseid = Column(Integer, ForeignKey(Courses.courseid), nullable=False)
    grade = Column(Float, nullable=False)
    status = Column(Boolean, default=True)


def create_tables():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    create_tables()
    with app.app_context():
        # Create a new user instance
        example_user = Users(
            username='sv',
            password='123',
            usertype='admin',
        )
        example_course = Courses(
            coursename='Python',
            teacherid='1',
        )
        example_teacher = Teachers(
            userid='1',
            fullname='vo',
            department='python',
        )
        example_student = Students(
            userid='1',
            fullname='thai',
            dateofbirth='2003/27/11',
            gender='Nam'
        )
        example_grade = Grades(
            studentid='1',
            courseid='1',
            grade='Python',
        )
        # Add the user to the session
        db.session.add(example_user)

        db.session.add(example_course)

        db.session.add(example_teacher)

        db.session.add(example_student)

        db.session.add(example_grade)

        # Commit the session to save the changes to the database
        db.session.commit()
