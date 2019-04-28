from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.stocks.models import Stock
from application.trade.models import  Trade
from application.trade.forms import TradeForm, CloseTradeForm
from application.portfolio.models import Portfolio

@app.route("/trade/new/<portfolio_id>", methods= ["POST"])
@login_required
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
    
    trade.stocks.append(stock)
    db.session.add(trade)
    db.session.commit()

    return redirect(url_for("portfolios_view", portfolio_id=portfolio_id))

@app.route("/trade/close", methods = ["GET"])
@login_required
def trade_finish():
    trade = Trade.query.get(request.args.get("trade_id"))
    portfolio_id = request.args.get("portfolio_id")
    
    if trade is None:
        return redirect(url_for("portfolios_view", portfolio_id = portfolio_id))
    
    form = CloseTradeForm(portfolio_id = portfolio_id)
    
    return render_template("trade/closetrade.html", 
            form = form, portfolio_id = portfolio_id, trade = trade)

@app.route("/trade/close/<trade_id>", methods = ["POST"])
@login_required
def trade_close(trade_id):
    # fix set sell_date, now only flask updates date_modified
    trade = Trade.query.get(trade_id)
    form = CloseTradeForm(request.form)

    if not form.validate():
        return render_template("trade/closetrade.html",
            form = form, trade = trade)
    
    trade.sellprice = form.sellprice.data

    db.session().commit()

    #print("FASSFAFA ID", form.portfolio_id)
    #ei toimi hiddenfield
    #return redirect(url_for("portfolios_view", portfolio_id = 3))
    return redirect(url_for("portfolios_index"))