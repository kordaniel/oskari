from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.portfolio.models import Portfolio
from application.portfolio.forms import CreatePortfolioForm

@app.route("/portfolios", methods=["GET"])
def portfolios_index():
    return render_template("portfolios/list.html", portfolios = Portfolio.query.all())

@app.route("/portfolios/new")
def portfolios_form():
    return render_template("portfolios/new.html", form = CreatePortfolioForm())

@app.route("/portfolios", methods=["POST"])
@login_required
def portfolios_create():
    form = CreatePortfolioForm(request.form)

    if not form.validate():
        return render_template("portfolios/new.html", form = form)
    
    p = Portfolio(form.name.data)
    p.account_id = current_user.id

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("portfolios_index"))