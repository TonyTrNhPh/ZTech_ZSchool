from flask_sqlalchemy import SQLAlchemy
from __init__ import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/zschool'
app.config['SQLALCHEMY__TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)


    
