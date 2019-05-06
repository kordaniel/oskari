from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, HiddenField, SubmitField, validators
from application.auth.models import User

class LoginForm(FlaskForm):
    username = StringField("Username", [
        validators.DataRequired(message=("Username required")),
        validators.Length(min=5, max=24, message=("Enter your username"))
    ])
    password = PasswordField("Password", [
        validators.DataRequired(message=("Password required")),
        validators.Length(min=8, max=40, message=("Enter your password"))
    ])

    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    name = StringField("Full name", [
        validators.DataRequired(message=("Enter your full name")),
        validators.Length(min=6, max=144, message=("Name must be [6-144] characters long"))
    ])
    email = StringField("Email address", [
        validators.Length(min=6, max=144, message=('Email length must be atleast 6 characters')),
        validators.Email(message=('Enter an valid email address')),
        validators.DataRequired(message=('Email cannot be empty'))
    ])
    username = StringField("Username", [
        validators.DataRequired(message=("Username cannot be empty")),
        validators.Length(min=5, max=24, message=("Username must be 5-24 characters long"))
    ])
    password = PasswordField("Password", [
        validators.DataRequired(message=("Password cannot be empty")),
        validators.Length(min=8, max=40, message=("Password must be 8-40 characters long"))
    ])
    confirm = PasswordField("Confirm Password", [
        validators.EqualTo("password", message=("Passwords must match"))
    ])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise validators.ValidationError("Username taken, please use a different username")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise validators.ValidationError("Email already in use, please use a different email address")
    
    class Meta:
        csrf = False

class EditUserForm(FlaskForm):
    name = StringField("Full name", [
        validators.DataRequired(message=("Enter your full name")),
        validators.Length(min=6, max=144, message=("Name must be [6-144] characters long"))
    ])
    email = StringField("Email address", [
        validators.Length(min=6, max=144, message=('Email length must be atleast 6 characters')),
        validators.Email(message=('Enter an valid email address')),
        validators.DataRequired(message=('Email cannot be empty'))
    ])
    username = StringField("Username", [
        validators.DataRequired(message=("Username cannot be empty")),
        validators.Length(min=5, max=24, message=("Username must be 5-24 characters long"))
    ])
    id = HiddenField("User ID", [
        validators.DataRequired(message=("ID missing"))
    ])
    submit = SubmitField("Update")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user is not None and user.get_id() != int(self.id.data):
            raise validators.ValidationError("Username already in use, please use a different username")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user is not None and user.get_id() != int(self.id.data):
            raise validators.ValidationError("Email already in use, please use a different email address")
    
    class Meta:
        csrf = False

class EditUserPasswordForm(FlaskForm):
    old_password = PasswordField("Old password", [
        validators.DataRequired(message=("Old password is required")),
    ])
    new_password = PasswordField("New password", [
        validators.DataRequired(message=("Password cannot be empty")),
        validators.Length(min=8, max=40, message=("Password must be 8-40 characters long"))
    ])
    confirm_password = PasswordField("Confirm Password", [
        validators.EqualTo("new_password", message=("Passwords must match"))
    ])
    id = HiddenField("User ID", [
        validators.DataRequired(message=("ID missing"))
    ])
    submit = SubmitField("Update password")

    class Meta:
        csrf = False
