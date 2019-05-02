from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required, login_manager
from application.auth.models import User, Role
from application.auth.forms import LoginForm, NewUserForm, EditUserForm, EditUserPasswordForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())
    
    form = LoginForm(request.form)
    if not form.validate():
        return render_template("auth/loginform.html", form = form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/register", methods = ["GET","POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form = NewUserForm())

    form = NewUserForm(request.form)
    if not form.validate():
        return render_template("auth/registerform.html", form = form)

    user = User(form.name.data, form.username.data, form.password.data, form.email.data)

    db.session().add(user)
    db.session().commit()

    user.set_default_role()

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/edit/<user_id>", methods = ["GET","POST"])
@login_required()
def auth_edit_profile(user_id):
    if not user_id.isdigit():
        return redirect("index")

    if int(user_id) != current_user.id and not current_user.is_superuser():
        return login_manager.unauthorized()
    
    if request.method == "GET":
        form = EditUserForm(obj=User.query.get(user_id))
        
        return render_template("auth/edit_profile.html", form = form)
    
    form = EditUserForm(request.form)
    
    # here is enough to compare form.id to user_id, since line 4 in
    # this method checks for credentials
    if (not form.id.data.isdigit() or 
            int(form.id.data) != int(user_id) or not form.validate()):
        return render_template("auth/edit_profile.html", form = form)

    user = User.query.get(user_id)
    
    user.name = form.name.data
    user.username = form.username.data
    user.email = form.email.data
    
    db.session.commit()

    return redirect(url_for("user_view", user_id=user_id))

@app.route("/auth/password/<user_id>", methods = ["GET", "POST"])
@login_required()
def auth_change_password(user_id):
    if not user_id.isdigit():
        return redirect("index")
    
    if int(user_id) != current_user.id and not current_user.is_superuser():
        return login_manager.unauthorized()
    
    if request.method == "GET":
        form = EditUserPasswordForm()
        form.id.data = user_id
        return render_template("auth/edit_password.html", form = form)
    
    form = EditUserPasswordForm(request.form)

    if (not form.id.data.isdigit() or 
            int(form.id.data) != int(user_id) or not form.validate()):
        return render_template("auth/edit_password.html", form = form)
    
    user = User.query.get(user_id)
    
    if form.old_password.data != user.password:
        form.old_password.errors.append("Invalid password")
        return render_template("auth/edit_password.html", form = form)

    user.password = form.new_password.data

    db.session.commit()

    return render_template("users/user.html", user = user)

@app.route("/auth/logout", methods = ["GET"])
@login_required()
def auth_logout():
    logout_user()
    return redirect(url_for("index"))