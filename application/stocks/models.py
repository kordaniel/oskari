from application import db
from application.models import Base

class Stock(Base):

    ticker = db.Column(db.String(16), unique=True, nullable=False)
    name = db.Column(db.String(144), nullable=False)
    
    def __init__(self, ticker, name):
        self.ticker = ticker
        self.name = name