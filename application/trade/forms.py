from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DecimalField, HiddenField, validators
from wtforms.fields.html5 import DateField
from flask_wtf.html5 import NumberInput

from application.stocks.models import Stock

class StockListForm(FlaskForm):
    stocks = SelectField("Stocks", [
            validators.DataRequired()])

    def __init__(self, *args, **kwargs):
        super(StockListForm, self).__init__(*args, **kwargs)
        self.stocks.choices = Stock.find_all_stocks_alphabetically()
    
    class Meta:
        csrd = False

class TradeForm(FlaskForm):
    stocks = SelectField("Select stock", [
            validators.DataRequired()])
    amount = IntegerField("Amount", [
            validators.NumberRange(min=1)],
            widget=NumberInput(),
            render_kw={"placeholder": "0"})
    date = DateField("DateTime", render_kw={"size": "2"})
    price = DecimalField("Price", [
            validators.NumberRange(min=0)],
            render_kw={"placeholder": "1.234"})

    def __init__(self, *args, **kwargs):
        super(TradeForm, self).__init__(*args, **kwargs)
        self.stocks.choices = Stock.find_all_stocks_alphabetically()
    
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