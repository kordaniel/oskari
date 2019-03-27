from application import db

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    ticker = db.Column(db.String(16), unique=True, nullable=False)
    name = db.Column(db.String(144), nullable=False)

    def __init__(self, ticker, name):
        self.ticker = ticker
        self.name = name