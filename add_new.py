import flask
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from data import db_session
from data.new import News
from forms.new_new import New_New

add_new_blueprint = flask.Blueprint(
    'add_new',
    __name__,
    template_folder='templates'
)


@add_new_blueprint.route('/add_new', methods=['GET', 'POST'])
@login_required
def add_new():
    new_form = New_New()
    new = News()
    if new_form.validate_on_submit():
        ses = db_session.create_sessin()
        if ses.query(News).filter(News.user == current_user,
                                  News.title == new_form.title.data).first():
            return render_template('add_new.html', title='Add new',
                                   message='You already have such gossip', form=new_form)
        new.title = new_form.title.data
        new.content = new_form.content.data
        new.user_id = current_user.id
        ses.add(new)
        ses.commit()
        id = ses.query(News).filter(News.user_id == current_user.id,
                                    News.title == new.title).first()
        if new_form.file.data:
            new_form.file.data.save(
                url_for('static', filename=f'img/{id.id}.jpg')[1:])
        return redirect(f'user/{current_user.id}')

    return render_template('add_new.html', title='Add new', form=new_form)
