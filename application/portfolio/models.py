from application import db, app
from application.models import Base

from sqlalchemy.sql import text

class Portfolio(Base):

    account_id = db.Column(db.Integer, 
        db.ForeignKey('account.id', ondelete='CASCADE'), nullable=False)
    trades = db.relationship("Trade", backref="portfolio", 
        passive_deletes=True, lazy = True)

    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name

    def account_name(self):
        stmt = text("SELECT account.name FROM account"
                    " WHERE account.id = :account_id").params(account_id=self.account_id)
        res = db.engine.execute(stmt).fetchone()
        
        return res[0]
    
    def open_trades(self):
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
        stmt = text("SELECT Stock.ticker, Stock.name,"
                    " Trade.date_created AS buydate, Trade.date_modified AS selldate, Trade.amount,"
                    " Trade.buyprice, Trade.sellprice,"
                    " ROUND(((Trade.sellprice - Trade.buyprice) * Trade.amount)::numeric, 2) AS total_return"
                    " FROM Trade, Tradestock, Stock"
                    " WHERE Trade.portfolio_id = :portfolio_id"
                    " AND Trade.sellprice IS NOT null"
                    " AND Trade.id = Tradestock.trade_id"
                    " AND Tradestock.stock_id = Stock.id"
                    ).params(portfolio_id=self.id)
        
        
        if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
            # using sqlite, need to use differnet query
            # this is probably an dumb way to do this, but...
            stmt = text("SELECT Stock.ticker, Stock.name,"
                        " Trade.date_created AS buydate, Trade.date_modified AS selldate, Trade.amount,"
                        " Trade.buyprice, Trade.sellprice,"
                        " ROUND(((Trade.sellprice - Trade.buyprice) * Trade.amount), 2) AS total_return"
                        " FROM Trade, Tradestock, Stock"
                        " WHERE Trade.portfolio_id = :portfolio_id"
                        " AND Trade.sellprice IS NOT null"
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

#    @staticmethod
#    def find_all_portfolios():
#        stmt = text("SELECT account.name, portfolio.name from account"
#                    " LEFT JOIN portfolio ON account.id = portfolio.account_id")
#        res = db.engine.execute(stmt)
#        for row in res:
#            print(row)