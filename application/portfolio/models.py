from application import db
from application.models import Base

from sqlalchemy.sql import text

class Portfolio(Base):

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
    nullable=False)
    trades = db.relationship("Trade", backref="trade", lazy = True)

    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name

    def account_name(self):
        stmt = text("SELECT account.name FROM account"
                    " WHERE account.id = :account_id").params(account_id=self.account_id)
        res = db.engine.execute(stmt).fetchone()
        
        return res[0]
    
    @staticmethod
    def find_all_portfolios():
        stmt = text("SELECT account.name, portfolio.name from account"
                    " LEFT JOIN portfolio ON account.id = portfolio.account_id")
        res = db.engine.execute(stmt)
        for row in res:
            print(row)