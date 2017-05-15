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

# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

admin = Admin(app, name='Puppenc', template_mode='bootstrap3')

class ClassView(ModelView):
    # create_modal = True
    can_export = True
    list_columns = [ 'id', 'name', 'insert_date' ]
    form_excluded_columns = ['hostgroupR', 'insert_date', 'update_date', 'delete_date']
    column_searchable_list = ['name']
    column_filters = ['name']
    # Readonly stuff
    can_create = False
    can_edit = False
    can_delete = False

class EnvironmentView(ModelView):
    # create_modal = True
    can_export = True
    list_columns = [ 'id', 'name', 'insert_date' ]
    form_excluded_columns = ['envR', 'insert_date', 'update_date', 'delete_date']
    column_searchable_list = ['name']
    column_filters = ['name']
    # Readonly stuff
    can_create = False
    can_edit = False
    can_delete = False

class HostgroupView(ModelView):
    # create_modal = True
    can_export = True
    column_display_pk = True
    # list_columns = [ 'id', 'name', 'insert_date', 'class_info' ]
    form_excluded_columns = ['nodesR', 'insert_date', 'update_date', 'delete_date']
    column_searchable_list = ['name', 'class_id']
    column_filters = ['name']
    # Readonly stuff
    can_create = False
    can_edit = False
    can_delete = False

class NodeView(ModelView):
    # create_modal = True
    can_export = True
    column_searchable_list = ['name', 'environment_id']
    column_filters = ['name']
    # Readonly stuff
    can_create = False
    can_edit = False
    can_delete = False


admin.add_view(ClassView(Class, db.session))
admin.add_view(EnvironmentView(Environment, db.session))
admin.add_view(HostgroupView(Hostgroup, db.session))
admin.add_view(NodeView(Node, db.session))

app.run(port=5001, host='0.0.0.0', debug=True)
