from flask_restful import Resource
from flask import jsonify, request

from app.puppenc import api, db, output_yaml, auth

from app.nodes.models import Node
from app.hostgroups.models import Hostgroup
from app.environments.models import Environment
from app.classes.models import Class

class Enc(Resource):
    @auth.login_required
    def get(self, page=1, node_name=None):
        """
        @api {get} /enc/<node-name> Get node informations (ENC)
        @apiVersion 1.0.0
        @apiName get_enc
        @apiGroup ENC
        @apiParam   {String}    node_name       The node's name
        @apiSuccess {Number}    id              The hostgroup's id.
        @apiSuccess {String}    name            The hostgroup's name.
        @apiSuccess {Datetime}  insert_date     The hostgroup's inserted date
        @apiSuccess {Datetime}  update_date     The hostgroup's updated date
        @apiSuccess {Datetime}  delete_date     The hostgroup's deleted date
        """
        if not node_name:
            obj = Node.query.paginate(page, 10).items
            return { "success": False, "message": "No node provided" }, 304
        else:

            node = Node.query.filter_by(name=node_name).first()
            if not node:
                return { "success": False, "message": "Node not found" }, 404

            if node.hostgroup_id is None:
                class_name = ''
                hostgroup_name = ''
            else:
                hg_class = Node.query.join(
                    Hostgroup,
                    Node.hostgroup_id==Hostgroup.id,
                ).join(
                    Class,
                    Hostgroup.class_id==Class.id
                ).add_columns(
                    Hostgroup.name.label('hostgroup_name'),
                    Class.name.label('class_name'),
                ).filter(
                    Node.name == node_name
                ).first()

                class_name     = hg_class.class_name
                hostgroup_name = hg_class.hostgroup_name

            # Death query
            environment_node = Node.query.join(
                Environment,
                Node.environment_id==Environment.id,
            ).add_columns(
                Node.id,
                Node.environment_id,
                Environment.name.label('environment_name'),
            ).filter(
                Node.name == node_name
            ).first()

            # We need to display it on "ENC" format
            res = {
                'classes': [
                    class_name,
                ],
                'parameters': {
                    'puppetmaster': '',
                    'hostgroup': hostgroup_name
                },
                'environment': environment_node.environment_name
            }

            if not res:
                return { "success": False, "message": "Node not found" }, 404
            return output_yaml(res, 200)
