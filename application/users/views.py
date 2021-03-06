from flask import redirect, render_template, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.auth.models import User, Role


@app.route("/users/<int:page>", methods=["GET"])
@login_required(role="ADMIN")
def users_index(page=1):
    per_page=30
    return render_template("/users/all_users.html", 
        users = User.query.order_by(User.name).paginate(page, per_page, error_out=False))

@app.route("/users/profile/<user_id>", methods=["GET"])
@login_required()
def user_view(user_id):
    if (not current_user.is_superuser() and
            (not user_id.isdigit() or int(user_id) != current_user.id)):
        return login_manager.unauthorized()
    
    user = User.query.get(user_id)
    
    if user is None:
        return redirect(url_for("index"))
    
    return render_template("users/user.html", user = user)

@app.route("/users/superuser/<user_id>", methods=["POST"])
@login_required(role="ADMIN")
def user_switch_superuser_status(user_id):
    if user_id.isdigit():
        user = User.query.get(user_id)
        su_role = Role.query.filter_by(superuser=True).first()

        if not user.is_superuser():
            user.roles.append(su_role)
        elif user.get_id() != 1:
            user.roles.remove(su_role)
        else:
            pass
        db.session.commit()
    
    return redirect(url_for("users_index", page=1))