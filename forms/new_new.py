from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField
from wtforms.validators import DataRequired as DR


class New_New(FlaskForm):
    title = StringField('Title', validators=[DR()])
    content = TextAreaField('Content', validators=[DR()])
    file = FileField('picture')
    submit = SubmitField('Ready!')
