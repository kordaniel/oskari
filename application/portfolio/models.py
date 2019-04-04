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
    
    def open_trades(self):
        print("MOORAOMWRORM")
        stmt = text("SELECT Stock.ticker, Stock.name, Trade.id,"
                    " Trade.date_created AS buydate,  Trade.amount, Trade.buyprice"
                    " FROM Trade, Tradestock, Stock"
                    " WHERE Trade.portfolio_id = :portfolio_id"
                    " AND Trade.sellprice IS null"
                    " AND Trade.id = Tradestock.trade_id"
                    " AND Tradestock.stock_id = Stock.id"
                    ).params(portfolio_id=self.id)
        res = db.engine.execute(stmt)
        
        response = []
        row_data = {}

        for rowproxy in res:
            for column, value in rowproxy.items():
                row_data = {**row_data, **{column: value}}
            response.append(row_data)

        return response

    def closed_trades(self):
        #stmt = text("SELECT * FROM trade"
        #            " WHERE portfolio_id = :portfolio_id"
        #            " AND sellprice IS NOT null").params(portfolio_id=self.id)
        stmt = text("SELECT Stock.ticker, Stock.name, Trade.date_created AS buydate, Trade.date_modified AS selldate, Trade.amount,"
                    " Trade.buyprice, Trade.sellprice"
                    " FROM Trade, Tradestock, Stock"
                    " WHERE Trade.portfolio_id = :portfolio_id"
                    " AND Trade.sellprice IS NOT null"
                    " AND Trade.id = Tradestock.trade_id"
                    " AND Tradestock.stock_id = Stock.id"
                    ).params(portfolio_id=self.id)
        res = db.engine.execute(stmt)

        response = []
        row_data = {}

        #CHANGE TOTAL RETURN CALCULATION TO BE DONE IN DB!?
        for rowproxy in res:
            for column, value in rowproxy.items():
                row_data = {**row_data, **{column: value}}
            row_data["total_return"] = (row_data["sellprice"] - row_data["buyprice"]) * row_data["amount"]
            response.append(row_data)

        return response

    @staticmethod
    def find_all_portfolios():
        stmt = text("SELECT account.name, portfolio.name from account"
                    " LEFT JOIN portfolio ON account.id = portfolio.account_id")
        res = db.engine.execute(stmt)
        for row in res:
            print(row)