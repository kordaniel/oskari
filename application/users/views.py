from flask import redirect, render_template, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.auth.models import User


@app.route("/user", methods=["GET"])
@login_required(role="ADMIN")
def users_index():
    return "avautui"
    #return render_template("/users/all_users.html", users = User.query.all())

@app.route("/user/<user_id>", methods = ["GET"])
@login_required()
def user_view(user_id):    
    if not user_id.isdigit() or int(user_id) != current_user.id:
        return login_manager.unauthorized()
    
    user = User.query.get(user_id)
    
    if user is None:
        return redirect(url_for("index"))
    
    return render_template("users/user.html", user = user)