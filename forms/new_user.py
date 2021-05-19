from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired as DR


class New_User(FlaskForm):
    nickname = StringField('Your nickname', validators=[DR()])
    password = PasswordField('Your password', validators=[DR()])
    password_again = PasswordField('Your password again', validators=[DR()])
    remember_me = BooleanField('Remember you?')
    submit = SubmitField('Ready!')
