import os, sys, yaml, logging
from logging.handlers import RotatingFileHandler
from flask import Flask, Blueprint, make_response, request, abort, g, send_from_directory, redirect
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import validate, fields
from functools import wraps
from flask_httpauth import HTTPBasicAuth
import time

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

api = Api(api_bp, prefix=app.config['PREFIX'], catch_all_404s=True)
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

class PuppencResource(Resource):

    def start_timer():
        request.start_time = time.time()

    def stop_timer(response):
        resp_time = time.time() - request.start_time
        return resp_time

    @app.before_request
    def before_request():
        PuppencResource.start_timer()

    # Useful interceptor to log all endpoint responses
    @app.after_request
    def after_request(response):
        response.direct_passthrough = False
        resp_time = PuppencResource.stop_timer(response)

        timestamp = time.strftime('%Y-%b-%d %H:%M')

        if(response.status_code != 200):
            message = str(response.data)
        else:
            message = False

        if not 'user' in g:
            user = False
        else:
            if g.user:
                user = g.user.name
            else:
                user = False

        if request.headers.getlist("X-Forwarded-For"):
            client_ip = request.headers.getlist("X-Forwarded-For")[0]
        else:
            client_ip = request.remote_addr

        log = {
            "timestamp": timestamp,
            "user": user,
            "method": request.method,
            "remote_addr": client_ip,
            "endpoint": request.endpoint,
            "path": request.path,
            "full_path": request.full_path,
            "return_code": response.status_code,
            "view_args": request.view_args,
            "time": float(resp_time),
            "message": message
        }

        if(response.status_code != 200):
            app.logger.warning(log)
        else:
            app.logger.info(log)
        return response

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

@app.after_request
def after_request(r):
    return r

@app.route('/doc/')
@app.route('/doc')
def my_redirect():
    return redirect("/doc/index.html")

@app.route("/doc/<path:path>")
def static_dir(path):
    return send_from_directory('docs', path)

class Index(PuppencResource):
    def get(self):
        return { "name": "Puppenc", "version": app.config['VERSION'], "debug": app.config['DEBUG']}, 200

api.add_resource(Index, '/', '/index')

app.register_blueprint(api_bp)
