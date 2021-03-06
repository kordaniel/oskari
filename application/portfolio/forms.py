from flask_wtf import FlaskForm
from wtforms import StringField, validators
#from application.portfolio.models import Portfolio

class CreatePortfolioForm(FlaskForm):
    name = StringField("Portfolio name", [
        validators.DataRequired(message=("Proper name required")),
        validators.Length(min=5, max=144)
    ])

    class Meta:
        csrf = False
    # actually, there can be multiple portfolios with the same name
    # leaving this here for now, if I decide to use it later!
    #def validate_name(self, name):
    #    portfolio = Portfolio.query.filter_by(name=name.data).first()
    #    if portfolio is not None:
    #        raise validators.ValidationError("Name reserved")