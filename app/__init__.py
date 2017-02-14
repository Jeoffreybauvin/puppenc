import os
import sys
from flask import Flask, Blueprint
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

api_bp = Blueprint('api', __name__)

app.config.from_object('config')

api = Api(api_bp, prefix=app.config['PREFIX'])
db = SQLAlchemy(app)

parser = reqparse.RequestParser()
parser.add_argument('as_yaml', type=int, default=0)

from app.environments.routes import Environments

class Index(Resource):
    def get(self):
        return 'Welcome to Puppenc'

api.add_resource(Index, '/')

app.register_blueprint(api_bp)
