import flask
from flask import render_template, request, redirect

from data import db_session
from data.user import User

from flask_login import current_user

get_user_blueprint = flask.Blueprint(
    'get_user',
    __name__,
    template_folder='templates'
)


@get_user_blueprint.route('/user/<int:id>', methods=['GET', 'POST'])
def get_user(id):
    ses = db_session.create_sessin()
    user = ses.query(User).get(id)
    if request.method == 'POST':
        cur_user = ses.query(User).get(current_user.id)
        if str(id) in current_user.subs:
            print(4)
            subs = current_user.subs.split(',')
            del subs[subs.index(str(id))]
            cur_user.subs = ','.join(subs)
        else:
            cur_user.subs += ',' + str(id)
        ses.commit()
        return redirect(f'/user/{id}')
    elif request.method == 'GET':
        news = user.news
        print(news)
        is_user = str(id) in current_user.subs
        return render_template('get_user.html', news=news, user=user.nickname, title=user.nickname, id=id, is_user=is_user)
