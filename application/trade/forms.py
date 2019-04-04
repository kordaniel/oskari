from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DecimalField, HiddenField, validators
from wtforms.fields.html5 import DateField
from flask_wtf.html5 import NumberInput

from application.stocks.models import Stock

class TradeForm(FlaskForm):
    ticker = StringField("Ticker", [
            validators.DataRequired(),
            validators.Length(min=1, max=16)],
            render_kw={"size": "4", "placeholder": "TICKER"})
    name = StringField("Name", [
            validators.DataRequired(),
            validators.Length(min=3, max=144)],
            render_kw={"size": "10", "placeholder": "Enter name"})
    amount = IntegerField("Amount", [
            validators.NumberRange(min=1)],
            widget=NumberInput(),
            render_kw={"size": "4", "placeholder": "0"})
    date = DateField("DateTime")
    price = DecimalField("Price", [
            validators.NumberRange(min=0)],
            render_kw={"placeholder": "1.234"})

    class Meta:
        csrf = False

class CloseTradeForm(FlaskForm):
    sellprice = DecimalField("Sell Price", [
        validators.NumberRange(min=0)],
        render_kw={"placeholder": "1.234"})
    selldate = DateField("DateTime")
    
    portfolio_id = HiddenField("Portfolio")

    class Meta:
        csrf = False