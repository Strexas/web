import datetime
import sqlalchemy as sa
from sqlalchemy import orm

from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy_serializer.serializer import SerializerMixin


class News(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'news'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String, nullable=True)
    content = sa.Column(sa.String, nullable=True)

    date = datetime.date.today().ctime().split()
    date = date[2] + ' ' + date[1] + ' ' + date[-1]
    created_date = sa.Column(sa.String, default=date)

    views = sa.Column(sa.Integer, default=0)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    user = orm.relation('User')
