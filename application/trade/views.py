from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.stocks.models import Stock
from application.trade.models import  Trade
from application.trade.forms import TradeForm
from application.portfolio.models import Portfolio

@app.route("/trade/new/<portfolio_id>", methods= ["POST"])
@login_required
def trade_create(portfolio_id):
    portfolio = Portfolio.query.get(portfolio_id)
    form = TradeForm(request.form)

    if not form.validate():
        return render_template("portfolios/portfolio.html", portfolio = portfolio, form = form)
    
    trade = Trade()
    
    stock = Stock.query.filter_by(ticker=form.ticker.data).first()
    if stock is None:
        return "EI"
    
    trade.portfolio_id = portfolio_id
    trade.amount = form.amount.data
    trade.buyprice = form.price.data
    
    trade.stocks.append(stock)
    db.session.add(trade)
    db.session.commit()
    return redirect(url_for("portfolios_view", portfolio_id=portfolio_id))