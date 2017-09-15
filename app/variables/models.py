from app.puppenc import db
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref

class Variable(db.Model):
    __tablename__ = 'variables'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    content = db.Column(db.String(255))
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    insert_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_date = db.Column(db.DateTime, default=None)
    delete_date = db.Column(db.DateTime, default=None)
    __table_args__ = (db.UniqueConstraint('name', 'content'),)

    def __init__(self, name, content=None, class_id=None):
        self.name = name
        self.content = content
        self.class_id = class_id

    def __repr__(self):
        return '<Variable %r>' % (self.name)

class NodeVariable(object):
    def __init__(self, nodes_id, variables_id):
        self.nodes_id = nodes_id
        self.variables_id = variables_id
