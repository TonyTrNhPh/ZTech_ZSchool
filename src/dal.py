from src.models import Users
def get_all_users():
    return Users.query.all()