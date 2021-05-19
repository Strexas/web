import flask
from flask import render_template, redirect
from flask_login import login_user

from data import db_session
from data.user import User
from forms.login import LoginForm

log_in_blueprint = flask.Blueprint(
    'log_in',
    __name__,
    template_folder='templates'
)


@log_in_blueprint.route('/log_in', methods=['GET', 'POST'])
def log_in():
    in_form = LoginForm()
    if in_form.validate_on_submit():
        ses = db_session.create_sessin()
        user = ses.query(User).filter(User.nickname == in_form.nickname.data).first()
        if not user:
            return render_template('log_in.html', message='Such nickname is not exist', form=in_form, title='Log in',)
        if not user.check_password(in_form.password.data):
            return render_template('log_in.html', message='Password is not right', form=in_form, title='Log in',)
        login_user(user, remember=in_form.remember_me.data)
        return redirect('/main')
    return render_template('log_in.html', title='Log in', form=in_form)
