from flask import render_template, redirect
from flask_login import login_required, logout_user, current_user

from add_new import add_new_blueprint
from app import app
from data import db_session
from data.new import News
from find_news import find_news_blueprint
from get_new import get_new_blueprint
from get_user import get_user_blueprint
from log_in import log_in_blueprint
from log_up import log_up_blueprint
from news_feed import news_feed_blueprint


@app.route('/')
@app.route('/main', methods=['GET', 'POST'])
def main():
    message = 'Welcome, '
    if current_user.is_authenticated:
        address = f'user/{current_user.id}'
        message += current_user.nickname
    else:
        address = '/log_up'
        message += '\n you have to log in to continue'
    return render_template('main.html', title='Gossip', address=address,
                           message=message)


@app.route('/user/<int:id_user>/delete/<int:id_new>')
@login_required
def delete_new(id_user, id_new):
    ses = db_session.create_sessin()
    news = ses.query(News).filter(
        News.id == id_new, News.user_id == id_user).first()
    ses.delete(news)
    ses.commit()
    return redirect(f'/user/{id_user}')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/main')


@app.errorhandler(401)
def error(error):
    return main()


if __name__ == '__main__':
    db_session.global_init('db/gossip.sqlite')
    # регистрация и вход
    app.register_blueprint(log_up_blueprint)
    app.register_blueprint(log_in_blueprint)

    #  новости
    app.register_blueprint(add_new_blueprint)
    app.register_blueprint(get_new_blueprint)
    app.register_blueprint(find_news_blueprint)
    app.register_blueprint(news_feed_blueprint)

    # пользователь
    app.register_blueprint(get_user_blueprint)
    app.run(host='127.0.0.1', port=8080)
