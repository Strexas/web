import flask
from flask import render_template
from flask_login import login_required

from data import db_session
from data.new import News
from data.user import User

news_feed_blueprint = flask.Blueprint(
    'news_feed',
    __name__,
    template_folder='templates'
)


@news_feed_blueprint.route('/news_feed/<int:id>')
@login_required
def news_feed(id):
    ses = db_session.create_sessin()
    user = ses.query(User).get(id)
    subs = [int(i) for i in user.subs.split(',')]
    news = ses.query(News).filter(News.id.in_(subs))[::-1]
    return render_template('news_feed.html', title='Feed', news=news, user=user.nickname, id=id)
