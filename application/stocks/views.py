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