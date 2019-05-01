from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, login_required
from application.auth.models import User, Role
from application.auth.forms import LoginForm, NewUserForm, EditUserForm

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
    # CHECK IF CURRENT_USER IS ADMIN OR ID == user_id..
    
    if request.method == "GET":
        user = User.query.get(user_id)
        form = EditUserForm(obj=User.query.get(user_id))
        
        return render_template("auth/edit_profile.html", form = form)
    
    # request.method == POST
    form = EditUserForm(request.form)
    
    if not form.id.data.isdigit() or not form.validate():
        return render_template("auth/edit_profile.html", form = form, user_id = user_id)

    return "edit" + str(user_id)

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))