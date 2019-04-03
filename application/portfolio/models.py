from application import db
from application.models import Base

class Portfolio(Base):
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
    nullable=False)

    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name