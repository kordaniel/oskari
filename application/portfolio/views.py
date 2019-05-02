from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required, current_user
from application.portfolio.models import Portfolio
from application.portfolio.forms import CreatePortfolioForm
from application.trade.forms import StockListForm, TradeForm

@app.route("/portfolios", methods=["GET"])
@login_required(role="ADMIN")
def portfolios_index():
    return render_template("portfolios/list.html", portfolios = Portfolio.query.order_by(Portfolio.name).all())

@app.route("/portfolios/current_user")
@login_required()
def current_user_portfolios():
    return render_template("portfolios/user_portfolios.html", portfolios = current_user.portfolios)

@app.route("/portfolios/<portfolio_id>", methods=["GET"])
@login_required()
def portfolios_view(portfolio_id):
    p = Portfolio.query.get(portfolio_id)

    if p is None:
        return redirect(url_for("portfolios_index"))
    
    if (p.account_id == current_user.id or 
            (current_user.is_authenticated and current_user.is_superuser())):
        return render_template("portfolios/portfolio.html",
            portfolio = p, form = TradeForm())

    return login_manager.unauthorized()

@app.route("/portfolios/new")
@login_required()
def portfolios_form():
    return render_template("portfolios/new.html", form = CreatePortfolioForm())

@app.route("/portfolios", methods=["POST"])
@login_required()
def portfolios_create():
    form = CreatePortfolioForm(request.form)

    if not form.validate():
        return render_template("portfolios/new.html", form = form)
    
    p = Portfolio(form.name.data)
    p.account_id = current_user.id

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("portfolios_view", portfolio_id = p.id))

@app.route("/portfolios/delete/<portfolio_id>", methods=["DELETE"])
@login_required()
def portfolios_delete(portfolio_id):
    portfolio = Portfolio.query.get(portfolio_id)
    #user_id = portfolio.user_id
    print("*_*_*_"*100)
    if portfolio is not None:
        for trade in portfolio.trades:
            db.session.delete(trade)
        db.session.delete(portfolio)
        db.session.commit()
    
    #if portfolio is not None:
    #    print("deleting portfolio ", portfolio.id)
    #    print(portfolio.name)
    #else:
    #    print("ERROR")
    return redirect(url_for("current_user_portfolios"))