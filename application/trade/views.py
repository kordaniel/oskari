from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.stocks.models import Stock
from application.trade.models import  Trade
from application.trade.forms import TradeForm, CloseTradeForm
from application.portfolio.models import Portfolio

@app.route("/trade/new/<portfolio_id>", methods= ["POST"])
@login_required()
def trade_create(portfolio_id):
    portfolio = Portfolio.query.get(portfolio_id)
    form = TradeForm(request.form)

    if not form.validate():
        return render_template("portfolios/portfolio.html", portfolio = portfolio, form = form)

    stock = Stock.query.filter_by(ticker=form.stocks.data).first()
    
    if stock is None:
        return render_template("portfolios/portfolio.html", portfolio = portfolio, form = form)
    
    trade = Trade()

    trade.portfolio_id = portfolio_id
    trade.amount = form.amount.data
    trade.buyprice = form.price.data
    trade.date_created = form.date.data
    trade.date_modified = form.date.data
    
    trade.stocks.append(stock)
    db.session.add(trade)
    db.session.commit()

    return redirect(url_for("portfolios_view", portfolio_id=portfolio_id))

@app.route("/trade/close", methods = ["GET"])
@login_required()
def trade_finish():
    trade = Trade.query.get(request.args.get("trade_id"))
    portfolio_id = request.args.get("portfolio_id")
    
    if trade is None:
        return redirect(url_for("portfolios_view", portfolio_id = portfolio_id))
    
    form = CloseTradeForm(portfolio_id = portfolio_id)
    
    return render_template("trade/closetrade.html", 
            form = form, trade = trade)

@app.route("/trade/close/<trade_id>", methods = ["POST"])
@login_required()
def trade_close(trade_id):
    trade = Trade.query.get(trade_id)
    form = CloseTradeForm(request.form)

    if not form.validate():
        return render_template("trade/closetrade.html",
            form = form, trade = trade)
    
    trade.sellprice = form.sellprice.data
    trade.date_modified = form.selldate.data

    db.session().commit()

    return redirect(url_for("portfolios_view", portfolio_id = form.portfolio_id.data))

@app.route("/trade/delete/<trade_id>", methods=["DELETE"])
@login_required()
def trade_delete(trade_id):
    trade = Trade.query.get(trade_id)
    portfolio_id = trade.portfolio_id

    if trade is not None:
        db.session.delete(trade)
        db.session.commit()
    
    return redirect(url_for("portfolios_view", portfolio_id=portfolio_id))