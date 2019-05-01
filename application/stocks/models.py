from application import db
from application.models import Base

from sqlalchemy.sql import text

class Stock(Base):

    ticker = db.Column(db.String(16), unique=True, nullable=False)
    name = db.Column(db.String(144), nullable=False)
    
    def __init__(self, ticker, name):
        self.ticker = ticker
        self.name = name
    
    def is_in_number_of_trades(self):
        stmt = text("SELECT COUNT(*) FROM Tradestock"
                    " WHERE stock_id = :stock_id").params(stock_id=self.id)
        res = db.engine.execute(stmt).fetchone()

        return res[0]

    def is_in_number_of_portfolios(self):
        stmt = text("SELECT COUNT(DISTINCT(portfolio.id)) FROM Portfolio"
                    " INNER JOIN Trade ON Portfolio.id = Trade.portfolio_id"
                    " INNER JOIN Tradestock ON Trade.id = Tradestock.trade_id"
                    " INNER JOIN Stock ON Tradestock.stock_id = Stock.id"
                    " WHERE stock.id = :stock_id").params(stock_id=self.id)
        res = db.engine.execute(stmt).fetchone()

        return res[0]

    @staticmethod
    def find_all_stocks_alphabetically():
        stmt = text("SELECT * FROM Stock"
                    " ORDER BY name ASC")
        res = db.engine.execute(stmt)
        return [(stock.ticker, stock.name) for stock in res]