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
    
    class Meta:
        csrf = False