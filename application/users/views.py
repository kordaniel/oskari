from flask import redirect, render_template, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.auth.models import User, Role


@app.route("/users", methods=["GET"])
@login_required(role="ADMIN")
def users_index():
    return render_template("/users/all_users.html", users = User.query.all())

@app.route("/users/<user_id>", methods = ["GET"])
@login_required()
def user_view(user_id):    
    if not user_id.isdigit() or int(user_id) != current_user.id:
        return login_manager.unauthorized()
    
    user = User.query.get(user_id)
    
    if user is None:
        return redirect(url_for("index"))
    
    return render_template("users/user.html", user = user)

@app.route("/users/<user_id>", methods = ["POST"])
@login_required(role="ADMIN")
def user_switch_superuser_status(user_id):
    if user_id.isdigit():
        user = User.query.get(user_id)
        su_role = Role.query.filter_by(superuser=True).first()

        if user.is_superuser():
            user.roles.remove(su_role)
        else:
            user.roles.append(su_role)
        db.session.commit()
    
    return render_template("/users/all_users.html", users = User.query.all())

#@app.route("/user/<user_id>", methods = ["DELETE"])
#@login_required(role="ADMIN")
#def delete_user(user_id):
#    if not user_id.isdigit():
#        return render_template("users/all_users.html", users = User.query.all())