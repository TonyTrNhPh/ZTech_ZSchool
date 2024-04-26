from database import db
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from __init__ import app

class User(db.Model):
    user_id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    role = Column(String(10),nullable=False)
    status = Column(Boolean, default=True)
    announcement = relationship('Announcement', backref='user',lazy = True)
    
   
   
class Announcement(db.Model):
    announcement_id = Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey(User.user_id), nullable=False)
    title = Column(String(20), nullable=False)
    discription = Column(String(200), nullable=False)
    date = Column(String(20), nullable=False)
    status = Column(Boolean, default=True)
    
def create_tables():
    with app.app_context():
        db.create_all()
            
if __name__ == '__main__':
    create_tables()