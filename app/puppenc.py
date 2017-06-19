import os, sys, yaml, logging
from logging.handlers import RotatingFileHandler
from flask import Flask, Blueprint, make_response, request, abort, g
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import validate, fields
from functools import wraps
from flask_httpauth import HTTPBasicAuth

WHOAMI='puppenc'

app = Flask(WHOAMI)
api_bp = Blueprint('api', WHOAMI)

app.config.update(dict(
    PROFILE = False,
    DEBUG = False,
    ENABLE_AUTH = True,
    PREFIX = '/api/v1',
    VERSION = '0.1',
    OBJECTS_PER_PAGE = 10,
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    DB_NAME = 'puppenc',
    DB_HOST = 'puppenc-mysql',
    DB_USER = 'root',
    DB_PASSWORD = 'puppenc',
))
app.config.from_object('config')
app.config.from_envvar('PUPPENC_SETTINGS', silent=True)

app.config.update(dict(SQLALCHEMY_DATABASE_CONN = 'mysql://' + app.config['DB_USER'] + ':' + app.config['DB_PASSWORD'] + '@' + app.config['DB_HOST']))
app.config.update(dict(SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_CONN'] + '/' + app.config['DB_NAME']))

api = Api(api_bp, prefix=app.config['PREFIX'])
db = SQLAlchemy(app)
ma = Marshmallow(app)
auth = HTTPBasicAuth()

def init_db():
    """Create the database."""
    try:
        print("Trying to create database " + app.config['DB_NAME'])
        engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_CONN']) # connect to server
        engine.execute('CREATE DATABASE ' + app.config['DB_NAME']) #create db - throw an error if already exists
    except:
        app.logger.warning('Aborting database creation ! Database already exists')

    try:
        db.create_all()
    except:
        app.logger.error('Aborting, something went wrong on creating the tables on host %s@%s:%s' % (app.config['DB_USER'], app.config['DB_HOST'], app.config['DB_NAME']))

    app.logger.info('Tables creation : done.')

def destroy_db():
    """ Destroy DB ! WARNING ! """
    app.logger.info("I'm destroying " + app.config['DB_NAME'])
    try:
        engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_CONN']) # connect to server
        engine.execute('DROP DATABASE ' + app.config['DB_NAME']) #create db - throw an error if already exists
    except:
        app.logger.info('Error on destroying database')

    app.logger.info('Database deleted')

@api.representation('text/plain')
def output_yaml(data, code, headers=None):
    headers = {'Content-Type': 'text/plain'}
    resp = make_response(yaml.dump(data, allow_unicode=True, default_flow_style=False, indent=5), code)
    resp.headers.extend(headers)
    return resp


def log_request(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

class PuppencResource(Resource):
    method_decorators = [log_request]

from app.environments.routes import Environments
from app.hostgroups.routes import Hostgroups
from app.classes.routes import Classes
from app.variables.routes import Variables
from app.users.routes import Users, Tokens
from app.enc.routes import Enc
from app.nodes.routes import Nodes
from app.nodes.routes_variables import NodesVariables

# Let's expose something :)
api.add_resource(Nodes, '/nodes', '/nodes/<int:id>')
api.add_resource(NodesVariables, '/nodes/<int:id>/variables')
api.add_resource(Hostgroups, '/hostgroups', '/hostgroups/<int:id>')
api.add_resource(Environments, '/environments', '/environments/<int:id>')
api.add_resource(Classes, '/classes', '/classes/<int:id>')
api.add_resource(Variables, '/variables', '/variables/<int:id>')
api.add_resource(Enc, '/enc/<string:node_name>')
api.add_resource(Users, '/users', '/users/<int:id>')
api.add_resource(Tokens, '/tokens')

class Index(PuppencResource):
    def get(self):
        return { "name": "Puppenc", "version": app.config['VERSION']}, 200

api.add_resource(Index, '/', '/index')

app.register_blueprint(api_bp)
