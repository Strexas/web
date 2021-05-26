from flask import Flask
from flask_login import LoginManager
from data import db_session
from data.user import User
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
app.config['SECRET_KEY'] = 'security_is_important'
# run_with_ngrok(app)

login_man = LoginManager()
login_man.init_app(app)


@login_man.user_loader
def loader_user(user_id):
    ses = db_session.create_sessin()
    return ses.query(User).get(user_id)
