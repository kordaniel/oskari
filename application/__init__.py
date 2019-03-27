# flask-application
from flask import Flask
app = Flask(__name__)

# database
from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///stocks.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# app logic
from application import views

from application.stocks import models
from application.stocks import views

from application.auth import models
from application.auth import views

# authentication
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# create database tables if necessary
db.create_all()