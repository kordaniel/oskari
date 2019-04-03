from application import db
from application.models import Base

class User(Base):
    __tablename__ = "account"
    
    name = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(8), default="user", nullable=False) #admin/user
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(144), unique=True, nullable=False)

    portfolios = db.relationship("Portfolio", backref="account", lazy=True)

    def __init__(self, name, username, password, email):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        #self. role = role

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True