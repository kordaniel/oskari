from flask_wtf import FlaskForm
from wtforms import StringField, validators
from application.stocks.models import Stock

class StockForm(FlaskForm):
    ticker = StringField("Ticker", [
        validators.DataRequired(message=("Ticker required")),
        validators.Length(min=1, max=16)])
    name = StringField("Name", [
        validators.DataRequired(message=("Enter company name, 3-144 characters accepted")),
        validators.Length(min=3, max=144)])

    def validate_ticker(self, ticker):
        stock = Stock.query.filter_by(ticker=ticker.data).first()
        if stock is not None:
            raise validators.ValidationError("Ticker already in database")
    
    class Meta:
        csrd = False