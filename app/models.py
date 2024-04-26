
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from __init__ import app,db

class Users(db.Model):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    usertype = Column(String(10),nullable=False)
    status = Column(Boolean, default=True)
    announcement = relationship('Announcements', backref='users',lazy = True)
    
    def __init__(self, username, password, usertype):
        self.username = username
        self.password = password
        self.usertype = usertype
        self.status = True

   
class Announcements(db.Model):
    __tablename__ = 'announcements'
    announcement_id = Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey(Users.user_id), nullable=False)
    title = Column(String(20), nullable=False)
    discription = Column(String(200), nullable=False)
    date = Column(String(20), nullable=False)
    status = Column(Boolean, default=True)
    
def create_tables():
    with app.app_context():
        db.create_all()
            
if __name__ == '__main__':
    create_tables()
    with app.app_context():
        # Create a new user instance
        example_user = Users(
            username='admin',
            password='123',
            usertype='admin',
        )

        # Add the user to the session
        db.session.add(example_user)
        
        # Commit the session to save the changes to the database
        db.session.commit()