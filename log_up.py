import flask
from flask import render_template, redirect
from flask_login import login_user

from data import db_session
from data.user import User
from forms.new_user import New_User

log_up_blueprint = flask.Blueprint(
    'log_up',
    __name__,
    template_folder='templates'
)


@log_up_blueprint.route('/log_up', methods=['GET', 'POST'])
def log_up():
    user = User()
    reg_form = New_User()
    if reg_form.validate_on_submit():
        ses = db_session.create_sessin()
        params = dict()
        if reg_form.password.data != reg_form.password_again.data:
            params['message'] = 'passwords do not equal'
        if ses.query(User).filter(User.nickname == reg_form.nickname.data).first():
            params['message'] = 'This nickname is already exist'
        if params:
            params['title'] = 'Log up'
            params['form'] = reg_form
            return render_template('log_up.html', **params)
        user.nickname = reg_form.nickname.data
        user.hashed_password = reg_form.password.data
        user.generate_password()
        ses.add(user)
        ses.commit()
        login_user(user, remember=reg_form.remember_me.data)
        return redirect('/')
    return render_template('log_up.html', title='Log up', form=reg_form)
