from application import app, db
from flask import redirect, render_template, request, url_for
from application.stocks.models import Stock

@app.route("/stocks", methods=["GET"])
def stocks_index():
    return render_template("stocks/list.html", stocks = Stock.query.all())

@app.route("/stocks", methods=["POST"])
def stocks_create():
    s = Stock(request.form.get("ticker"), request.form.get("name"))
    
    db.session().add(s)
    db.session().commit()

    return redirect(url_for("stocks_index"))

@app.route("/stocks/new")
def stocks_form():
    return render_template("stocks/new.html")

@app.route("/stocks/<stock_id>", methods=["GET"])
def stocks_view(stock_id):
    return render_template("stocks/stock.html", s = Stock.query.get(stock_id))

@app.route("/stocks/update/<stock_id>", methods=["POST"])
def stocks_update(stock_id):
    s = Stock.query.get(stock_id)
    s.ticker = request.form.get("ticker")
    s.name = request.form.get("name")
    db.session().commit()
    return redirect(url_for("stocks_index"))