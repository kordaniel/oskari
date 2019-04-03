from flask import redirect, render_template, url_for

from application import app, db
from application.auth.models import User

@app.route("/user/<user_id>", methods = ["GET"])
def user_view(user_id):
    user = User.query.get(user_id)
    
    if user is None:
        return redirect(url_for("index"))
    
    for row in user.portfolios:
        print(row.name)
    
    return render_template("users/user.html", user = user)