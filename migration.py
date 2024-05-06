
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
        
        example_announcement = Announcements(
            userid = '1',
            title = 'Test',
            description = 'Hello',
            date = datetime.now(),
            who = 'Tất cả',
        )
        
        example_course = Courses(
            coursename = 'Test',
            teacherid = '2',
            status = True,            
        )
    
        
        
        # Add the data to the database
        # db.session.add(example_user)
        # db.session.add(example_announcement)
        db.session.add(example_course)    
        # db.session.add(example_student)
        db.session.commit()


