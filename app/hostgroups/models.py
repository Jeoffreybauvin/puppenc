from app.puppenc import db
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref

from app.nodes.models import Node

class Hostgroup(db.Model):
    __tablename__ = 'hostgroups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    insert_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_date = db.Column(db.DateTime, default=None)
    delete_date = db.Column(db.DateTime, default=None)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))

    nodesR = db.relationship('Node', backref='hostgroup_info', lazy='dynamic')

    def __init__(self, name=None, class_id=None):
        self.name = name
        self.class_id = class_id

    def __repr__(self):
        return '<Hostgroup %r>' % (self.name)
