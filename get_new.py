import flask
from flask import render_template, url_for

from data import db_session
from data.new import News
from data.user import User

from flask_login import current_user

get_new_blueprint = flask.Blueprint(
    'get_new',
    __name__,
    template_folder='templates'
)


@get_new_blueprint.route('/new/<int:id>', methods=['GET'])
def get_new(id):
    ses = db_session.create_sessin()
    new = ses.query(News).get(id)
    new.views += 1
    ses.commit()
    user = ses.query(User).get(new.user_id)
    address_image = url_for('static', filename=f'img/{new.id}.jpg')
    address_author = f'/user/{new.user_id}'
    return render_template('get_new.html', title=new.title, form=new, author=user.nickname, address_image=address_image, address_author=address_author)
