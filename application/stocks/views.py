from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.stocks.models import Stock
from application.stocks.forms import StockForm

@app.route("/stocks/<int:page>", methods=["GET"])
def stocks_index(page=1):
    per_page=10
    return render_template("stocks/list.html", 
        stocks = Stock.query.order_by(Stock.name).paginate(page, per_page, error_out=False))

@app.route("/stocks", methods=["POST"])
@login_required()
def stocks_create():
    this_form = StockForm(request.form)

    if not this_form.validate():
        return render_template("stocks/new.html", form = this_form)
    
    s = Stock(this_form.ticker.data, this_form.name.data)

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("stocks_index", page=1))

@app.route("/stocks/new", methods=["GET"])
@login_required()
def stocks_form():
    return render_template("stocks/new.html", form = StockForm())

@app.route("/stocks/view/<stock_id>", methods=["GET"])
def stocks_view(stock_id):
    s = Stock.query.get(stock_id)

    if request.method == "GET" and s is not None:
        return render_template("/stocks/stock.html", s = s, form = StockForm(obj = s))
    
    return redirect(url_for("stocks_index", page=1))

@app.route("/stocks/update/<stock_id>", methods=["POST"])
@login_required()
def stocks_update(stock_id):
    s = Stock.query.get(stock_id)
    form = StockForm(request.form)

    if form.ticker.data != s.ticker and not form.validate() or not form.name.validate(form):
        return render_template("stocks/stock.html", s = s, form = form)
    
    form.populate_obj(s)
    db.session().commit()
    return redirect(url_for("stocks_index", page=1))

@app.route("/stocks/delete/<stock_id>", methods=["DELETE"])
@login_required(role="ADMIN")
def stocks_delete(stock_id):
    s = Stock.query.get(stock_id)
    
    if s is not None:
        db.session().delete(s)
        db.session().commit()

    return redirect(url_for("stocks_index", page=1))