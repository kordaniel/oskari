from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.portfolio.models import Portfolio
from application.portfolio.forms import CreatePortfolioForm
from application.trade.forms import TradeForm

@app.route("/portfolios", methods=["GET"])
def portfolios_index():
    return render_template("portfolios/list.html", portfolios = Portfolio.query.order_by(Portfolio.name).all())

@app.route("/portfolios/<portfolio_id>", methods=["GET"])
@login_required()
def portfolios_view(portfolio_id):
    p = Portfolio.query.get(portfolio_id)

    if p is None:
        return redirect(url_for("portfolios_index"))
    
    if p.account_id != current_user.id:
        return login_manager.unauthorized()
    
    return render_template("portfolios/portfolio.html", portfolio = p, form = TradeForm())

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

    return redirect(url_for("portfolios_index"))