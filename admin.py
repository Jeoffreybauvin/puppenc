from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# Puppenc
from app.puppenc import api, db, output_yaml
from app.classes.models import Class
from app.nodes.models import Node
from app.environments.models import Environment
from app.hostgroups.models import Hostgroup

app = Flask(__name__)

app.secret_key = 'super secret key'
admin = Admin(app, name='puppenc', template_mode='bootstrap3')

admin.add_view(ModelView(Class, db.session))
admin.add_view(ModelView(Node, db.session))
admin.add_view(ModelView(Environment, db.session))
admin.add_view(ModelView(Hostgroup, db.session))

app.run(port=5001, debug=True)
