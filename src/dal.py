from src import db
from src.models import Users
def get_all_users():
    return Users.query.all()

def add_user(username, password, usertype):
    user = Users(username, password, usertype)
    db.session.add(user)
    db.session.commit()