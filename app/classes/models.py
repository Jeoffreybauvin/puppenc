from app.puppenc import db
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref

class Class(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    insert_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_date = db.Column(db.DateTime, default=None)
    delete_date = db.Column(db.DateTime, default=None)

    hostgroupR = db.relationship('Hostgroup', backref='class_info', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Class %r>' % (self.name)
