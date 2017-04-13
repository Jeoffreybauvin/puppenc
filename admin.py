from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

# Puppenc
from app.puppenc import api, db, output_yaml
from app.classes.models import Class
from app.nodes.models import Node
from app.environments.models import Environment
from app.hostgroups.models import Hostgroup

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = '123456790'
app.config['SQLALCHEMY_ECHO'] = True

app.config.update(dict(
    PROFILE = False,
    DEBUG = False,
    PREFIX = '/api/v1',
    VERSION = '0.1',
    OBJECTS_PER_PAGE = 10,
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    DB_NAME = 'puppenc',
    DB_HOST = 'puppenc-mysql',
    DB_USER = 'root',
    DB_PASSWORD = 'puppenc',
))

app.config.update(dict(SQLALCHEMY_DATABASE_CONN = 'mysql://' + app.config['DB_USER'] + ':' + app.config['DB_PASSWORD'] + '@' + app.config['DB_HOST']))
app.config.update(dict(SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_CONN'] + '/' + app.config['DB_NAME']))


admin = Admin(app, name='admin_puppenc', template_mode='bootstrap3')

admin.add_view(ModelView(Class, db.session))
admin.add_view(ModelView(Node, db.session))
admin.add_view(ModelView(Environment, db.session))
admin.add_view(ModelView(Hostgroup, db.session))

app.run(port=5001, host='0.0.0.0', debug=True)
