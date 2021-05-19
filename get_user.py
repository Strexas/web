import flask
from flask import render_template

from data import db_session
from data.user import User

from flask_login import current_user

get_user_blueprint = flask.Blueprint(
    'get_user',
    __name__,
    template_folder='templates'
)


@get_user_blueprint.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    ses = db_session.create_sessin()
    user = ses.query(User).get(id)
    news = user.news
    if not news:
        news = ['There is nothing to show']
    is_user = str(id) in current_user.subs
    return render_template('get_user.html', news=news, user=user.nickname, title=user.nickname, id=id, is_user=is_user)
