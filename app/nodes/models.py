from app.puppenc import app, db
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref

class Node(db.Model):
    __tablename__ = 'nodes'
    id             = db.Column(db.Integer, primary_key=True)
    name           = db.Column(db.String(255), unique=True)
    insert_date    = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_date    = db.Column(db.DateTime, default=None)
    delete_date    = db.Column(db.DateTime, default=None)
    hostgroup_id   = db.Column(db.Integer, db.ForeignKey('hostgroups.id'))
    environment_id = db.Column(db.Integer, db.ForeignKey('environments.id'))
    active         = db.Column(db.Integer, default=1)

    def __init__(self, name=None, environment_id=None, hostgroup_id=None):
        self.name = name
        self.environment_id = environment_id
        self.hostgroup_id = hostgroup_id

    def __repr__(self):
        return '<Node %r>' % (self.name)
