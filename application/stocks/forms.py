from flask_wtf import FlaskForm
from wtforms import StringField, validators

class StockForm(FlaskForm):
    ticker = StringField("Ticker", [validators.Length(min=1, max=16)])
    name = StringField("Name", [validators.Length(min=3, max=144)])

    class Meta:
        csrd = False