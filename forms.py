from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class PasswordForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')
    submit = SubmitField('Submit')
