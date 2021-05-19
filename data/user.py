import datetime
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
import sqlalchemy as sa
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import orm


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    nickname = sa.Column(sa.String, nullable=True)
    hashed_password = sa.Column(sa.String, nullable=True)

    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now())
    subs = sa.Column(sa.String, default='1')
    news = orm.relation("News", back_populates='user')

    def generate_password(self):
        self.hashed_password = generate_password_hash(self.hashed_password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
