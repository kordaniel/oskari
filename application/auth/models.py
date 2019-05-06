from werkzeug.security import generate_password_hash, check_password_hash
from application import db
from application.models import Base

user_role = db.Table("userrole",
    db.Column("user_id", db.Integer, db.ForeignKey("account.id", ondelete="CASCADE")),
    db.Column("role_id", db.Integer, db.ForeignKey("role.id")))

class Role(Base):
    name = db.Column(db.String(16), nullable = False, unique=True)
    superuser = db.Column(db.Boolean, default=False, nullable=False, unique=False)

    def __init__(self, role_name, superuser = False):
        self.name = role_name
        self.superuser = superuser
    
    @staticmethod
    def get_default_role():
        return Role.query.filter_by(name="USER").first()

class User(Base):
    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(24), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(144), unique=True, nullable=False)

    roles = db.relationship("Role", secondary=user_role, lazy="subquery",
        backref=db.backref("users", passive_deletes=True, lazy=True))
    
    portfolios = db.relationship("Portfolio", backref="account", 
        passive_deletes=True, lazy=True)

    def __init__(self, name, username, password, email):
        self.name = name
        self.username = username
        self.email = email
        self.set_password(password)

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def is_superuser(self):
        su_role = Role.query.filter_by(superuser=True).first()
        return su_role.name in self.get_roles()
    
    def set_default_role(self):
        user_role = Role.get_default_role()
        
        if user_role.name not in self.get_roles():
            self.roles.append(user_role)
        db.session.commit()

    def get_roles(self):
        return [r.name for r in self.roles]
    
    def has_portfolio_with_id(self, portfolio_id):
        return any(p.id == int(portfolio_id) for p in self.portfolios)