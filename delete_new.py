import flask
from flask import render_template, request, redirect

from data import db_session
from data.user import User
from data.new import News

from flask_login import current_user, login_required

delete_new_blueprint = flask.Blueprint(
    'delete_new',
    __name__,
    template_folder='templates'
)


@delete_new_blueprint.route('/user/<int:id_user>/delete/<int:id_new>')
@login_required
def delete_new(id_user, id_new):
    ses = db_session.create_sessin()
    news = ses.query(News).filter(
        News.id == id_new, News.user_id == id_user).first()
    ses.delete(news)
    ses.commit()
    return redirect(f'/user/{id_user}')
