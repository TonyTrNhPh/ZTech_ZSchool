from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/zschool'
app.config['SQLALCHEMY__TRACK_MODIFICATIONS'] = True
app.config["SECRET_KEY"] = "ZSchool"

db = SQLAlchemy(app=app)
lm = LoginManager(app=app)