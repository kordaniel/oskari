from flask import render_template
from application import app
from application.auth.models import User

@app.route('/')
def index():
    users = User.query.all()
    for user in users:
        print(user.name)
        for r in user.roles:
            print(r.name)
        print("----------")
    return render_template('index.html')