from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired as DR


class LoginForm(FlaskForm):
    nickname = StringField('Your nickname', validators=[DR()])
    password = PasswordField('Your password', validators=[DR()])
    remember_me = BooleanField('Remember you?', default=True)
    submit = SubmitField('Ready!')
