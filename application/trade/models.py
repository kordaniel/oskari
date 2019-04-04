from application import db
from application.models import Base

trade_stock = db.Table("tradestock",
    db.Column("trade_id", db.Integer, db.ForeignKey("trade.id"), primary_key = True),
    db.Column("stock_id", db.Integer, db.ForeignKey("stock.id"), primary_key = True))
    
class Trade(Base):

    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'),
        nullable=False)

    stocks = db.relationship("Stock", secondary = trade_stock, lazy="subquery",
        backref = db.backref("stocks", lazy = True))

    amount = db.Column(db.Integer, nullable = False)
    buyprice = db.Column(db.Float, nullable = False)
    sellprice = db.Column(db.Float, nullable = True)
    