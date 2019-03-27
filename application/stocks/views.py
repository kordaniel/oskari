from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.stocks.models import Stock
from application.stocks.forms import StockForm

@app.route("/stocks", methods=["GET"])
def stocks_index():
    return render_template("stocks/list.html", stocks = Stock.query.all())

@app.route("/stocks", methods=["POST"])
@login_required
def stocks_create():
    this_form = StockForm(request.form)

    if not this_form.validate():
        return render_template("stocks/new.html", form = this_form)
    
    s = Stock(this_form.ticker.data, this_form.name.data)

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("stocks_index"))

@app.route("/stocks/new")
@login_required
def stocks_form():
    return render_template("stocks/new.html", form = StockForm())

@app.route("/stocks/<stock_id>", methods=["GET"])
def stocks_view(stock_id):
    s = Stock.query.get(stock_id)
    form = StockForm(obj=s)

    return render_template("stocks/stock.html", s = s, form = form)

@app.route("/stocks/update/<stock_id>", methods=["POST"])
@login_required
def stocks_update(stock_id):
    s = Stock.query.get(stock_id)
    form = StockForm(request.form)

    if not form.validate():
        return render_template("stocks/stock.html", s = s, form = form)
    
    form.populate_obj(s)
    db.session().commit()
    return redirect(url_for("stocks_index"))