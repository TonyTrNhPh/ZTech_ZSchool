
from datetime import datetime
from src import app, db
from src.models import *


def create_tables():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    create_tables()
    with app.app_context():
        example_user = Users(
            username='admin',
            password='123',
            usertype='Quản trị viên',
        )
        example_USteacher = Users(
            username='gv',
            password='123',
            usertype='Giao vien',
        )
        example_USstudent = Users(
            username='sv',
            password='123',
            usertype='sinh vien',
        )
        example_announcement = Announcements(
            userid = '1',
            title = 'Test',
            description = 'Hello',
            date = datetime.now(),
            who = 'Tất cả',
        )
        example_teacher = Teachers(
            userid='2',
            fullname='tuan',
            department='code',
        )
        example_student = Students(
            userid='3',
            fullname='vo',
            dateofbirth='2003/11/27',
            gender='nam',
        )
        example_course = Courses(
            coursename = 'python',
            teacherid = '1',
        )               
        example_grade = Grades(
            studentid='1',
            courseid='1',
            grade='10.0',
        )
        example_feedback = Course_feedback(
            courseid = '1',
            rating = '10',
            comment='good',
        )               
        example_document = Course_documents(
            documentname='code',
            supplier='nvc',
            year='2024',
            courseid='1',
        )
        example_attendance = Attendance(
            courseid = '1',
            date = '2024/5/7',
            status='1',
        )       
    
        
        
        # Add the data to the database
        db.session.add(example_user)
        db.session.flush()
        db.session.commit()
        db.session.add(example_USteacher)
        db.session.flush()
        db.session.commit()
        db.session.add(example_USstudent)
        db.session.flush()
        db.session.commit()
        db.session.add(example_announcement)
        db.session.flush()
        db.session.commit()
        db.session.add(example_teacher)
        db.session.flush()
        db.session.commit()
        db.session.add(example_student)
        db.session.flush()
        db.session.commit()
        db.session.add(example_course)   
        db.session.flush()
        db.session.commit()
        db.session.add(example_grade) 
        db.session.flush()
        db.session.commit()
        db.session.add(example_feedback)
        db.session.flush()
        db.session.commit()
        db.session.add(example_document)
        db.session.flush()
        db.session.commit()
        db.session.add(example_attendance)
        db.session.flush()
        db.session.commit()


