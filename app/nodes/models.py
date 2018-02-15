from app.puppenc import app, db
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref

from app.variables.models import Variable, NodeVariable
class Node(db.Model):

    nodes_variables = db.Table('nodes_variables',
        db.Column('nodes_id', db.Integer, db.ForeignKey('nodes.id')),
        db.Column('variables_id', db.Integer, db.ForeignKey('variables.id')),
         db.PrimaryKeyConstraint('nodes_id', 'variables_id')
    )

    db.mapper(NodeVariable, nodes_variables)

    __tablename__ = 'nodes'
    id             = db.Column(db.Integer, primary_key=True)
    name           = db.Column(db.String(255), unique=True)
    insert_date    = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_date    = db.Column(db.DateTime, default=None)
    delete_date    = db.Column(db.DateTime, default=None)
    hostgroup_id   = db.Column(db.Integer, db.ForeignKey('hostgroups.id'))
    environment_id = db.Column(db.Integer, db.ForeignKey('environments.id'))
    active         = db.Column(db.Integer, default=1)
    last_used      = db.Column(db.DateTime, default=None)
    nodes_var      = db.relationship(
        "Variable",
        secondary=nodes_variables,
        backref=db.backref('variables', lazy='dynamic')
    )


    def __init__(self, name, environment_id=None, hostgroup_id=None):
        self.name = name
        self.environment_id = environment_id
        self.hostgroup_id = hostgroup_id

    def __repr__(self):
        return '<Node %r>' % (self.name)
