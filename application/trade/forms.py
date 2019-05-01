from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DecimalField, HiddenField, SubmitField, validators
from wtforms.fields.html5 import DateField
from flask_wtf.html5 import NumberInput

from application.stocks.models import Stock

class DecimalFieldWithDotAndCommas(DecimalField):
    def process_formdata(self, valuelist):
        if valuelist:
            valuelist[0] = valuelist[0].replace(",", ".")
        return super(DecimalFieldWithDotAndCommas, self).process_formdata(valuelist)

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
            validators.DataRequired()],
            render_kw={"class": "form-control form-control-sm"})
    amount = IntegerField("Amount", [
            validators.NumberRange(min=1)],
            widget=NumberInput(),
            render_kw={"placeholder": "0"})
    date = DateField("DateTime",
            format="%Y-%m-%d",
            render_kw={"size": "2"})
    #get time from datefield
    #(form.)date.data.strftime("%Y-%m-%d")
    price = DecimalFieldWithDotAndCommas("Price", [
            validators.NumberRange(min=0)],
            render_kw={"placeholder": "1.234"})
    submit = SubmitField("Open new position")

    def __init__(self, *args, **kwargs):
        super(TradeForm, self).__init__(*args, **kwargs)
        self.stocks.choices = Stock.find_all_stocks_alphabetically()
    
    class Meta:
        csrf = False

class CloseTradeForm(FlaskForm):
    sellprice = DecimalFieldWithDotAndCommas("Sell Price", [
        validators.NumberRange(min=0)],
        render_kw={"placeholder": "1.234"})
    selldate = DateField("DateTime")

    portfolio_id = HiddenField("Portfolio")

    class Meta:
        csrf = False