from app.puppenc import db
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref

from app.nodes.models import Node


class Environment(db.Model):
    __tablename__ = 'environments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    insert_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_date = db.Column(db.DateTime, default=None)
    delete_date = db.Column(db.DateTime, default=None)

    nodes = db.relationship('Node', backref='env_info', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Environment %r>' % (self.name)
