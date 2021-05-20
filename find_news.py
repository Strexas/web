from flask import request, Blueprint, render_template
from data import db_session
from data.new import News


find_news_blueprint = Blueprint(
    'find_news',
    __name__,
    template_folder='templates'
)


@find_news_blueprint.route('/find_news', methods=['GET', 'POST'])
def find_news():
    ses = db_session.create_sessin()
    if request.method == 'GET':
        news = ses.query(News).all()
        return render_template('find_news.html', title='Find news', news=news)
    elif request.method == 'POST':
        req = request.form['req']
        news = ses.query(News).filter(News.title.like(f'%{req}%'))
        k = 0
        print(dir(news))
        for _ in news:
            k += 1
            if k == 1:
                break
        if k:
            return render_template('find_news.html', news=news, value=req)
        else:
            return render_template('find_news.html', message='nothing is found', value=req)
