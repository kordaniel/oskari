# flask-application
from flask import Flask
app = Flask(__name__)

# database connectivity and ORM
from flask_sqlalchemy import SQLAlchemy
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_ECHO"] = True

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# login functionality
app.config["SECRET_KEY"] = os.urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# roles in login_required
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()
            
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True

                for user_role in current_user.get_roles():
                    if user_role == role:
                        unauthorized = False
                        break
            
            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# app logic
from application import views

from application.stocks import models
from application.stocks import views

from application.portfolio import models
from application.portfolio import views

from application.trade import models
from application.trade import views

from application.auth import models
from application.auth import views

from application.users import views

# listeners to configugre sqlite3 to use foreign key constraints
# and to add default values into tables after creation
from sqlalchemy import event
from sqlalchemy.engine import Engine
from application.auth.models import Role, User

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

@event.listens_for(Role.__table__, 'after_create')
def insert_initial_roles(*args, **kwargs):
    db.session.add(Role("ADMIN", True))
    db.session.add(Role("USER", False))
    db.session.commit()

@event.listens_for(User.__table__, 'after_create')
def insert_initial_superuser(*args, **kwargs):
    if os.environ.get("HEROKU"):
        super_user = User(
            os.environ.get("SU_NAME"),
            os.environ.get("SU_USERNAME"),
            os.environ.get("SU_PASSWD"),
            os.environ.get("SU_EMAIL"))
    else:
        super_user = User(
            "Development Superuser",
            "administrator",
            "topsekret",
            "admin@oskariadmin.com")
    db.session.add(super_user)
    db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# create database tables if necessary
try:
    db.create_all()
    # Set roles for default user with id = 1,
    # including ADMIN-role.gur
    su_user = User.query.get(1)
    su_user.set_default_role()
    su_role = Role.query.filter_by(superuser=True).first()
    if su_role.name not in su_user.get_roles():
        su_user.roles.append(su_role)
        db.session.commit()
except:
    pass