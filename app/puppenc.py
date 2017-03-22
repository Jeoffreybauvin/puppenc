import os, sys, yaml, logging
from logging.handlers import RotatingFileHandler
from flask import Flask, Blueprint, make_response, request, abort, g
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import validate, fields
from functools import wraps

WHOAMI='puppenc'

app = Flask(WHOAMI)

api_bp = Blueprint('api', WHOAMI)

app.config.from_object('config')

api = Api(api_bp, prefix=app.config['PREFIX'])
db = SQLAlchemy(app)
ma = Marshmallow(app)

def init_db():
    """Create the database."""
    # print("Will create " + app.config['DATABASE'])
    # engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_CONN']) # connect to server
    # engine.execute('CREATE DATABASE ' + app.config['DATABASE']) #create db - throw an error if already exists
    db.create_all()

def destroy_db():
    """ Destroy DB ! WARNING ! """
    print("Will destroy " + app.config['DATABASE'])
    engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_CONN']) # connect to server
    engine.execute('DROP DATABASE ' + app.config['DATABASE']) #create db - throw an error if already exists


@api.representation('text/plain')
def output_yaml(data, code, headers=None):
    headers = {'Content-Type': 'text/plain'}
    resp = make_response(yaml.dump(data, allow_unicode=True, default_flow_style=False, indent=5), code)
    resp.headers.extend(headers)
    return resp


def log_request(func):
    def wrapper(*args, **kwargs):
        # For now, no log
        # app.logger.info('prout')
        return func(*args, **kwargs)
    return wrapper

class PuppencResource(Resource):
    method_decorators = [log_request]

from app.environments.routes import Environments
from app.hostgroups.routes import Hostgroups
from app.classes.routes import Classes
from app.nodes.routes import Nodes

from app.enc.routes import Enc

# Let's expose something :)
api.add_resource(Nodes, '/nodes', '/nodes/<int:id>')
api.add_resource(Hostgroups, '/hostgroups', '/hostgroups/<int:id>')
api.add_resource(Environments, '/environments', '/environments/<int:id>')
api.add_resource(Classes, '/classes', '/classes/<int:id>')
api.add_resource(Enc, '/enc/<string:node_name>')


class Index(Resource):
    def get(self):
        return { "name": "Puppenc", "version": app.config['PREFIX']}, 200

api.add_resource(Index, '/', '/index')
app.register_blueprint(api_bp)
