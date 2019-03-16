from application import app, db
from flask import render_template, request
from application.stocks.models import Stock

@app.route("/stocks/new")
def stocks_form():
    return render_template("stocks/new.html")

@app.route("/stocks", methods=["POST"])
def stocks_create():
    s = Stock(request.form.get("ticker"), request.form.get("name"))
    
    db.session().add(s)
    db.session().commit()

    return "All stocks live here"