from flask_restful import Resource
from flask import jsonify, request, g

from app.puppenc import app, api, db, output_yaml, auth, PuppencResource

from app.nodes.models import Node
from app.hostgroups.models import Hostgroup
from app.environments.models import Environment
from app.classes.models import Class

class Enc(PuppencResource):
    @auth.login_required
    def get(self, page=1, node_name=None):
        """
        @api {get} /enc/<node-name> Get node informations (ENC)
        @apiName get_enc
        @apiGroup ENC
        @apiPermission user
        @apiVersion 1.0.0
        @apiParam   {String}    node_name       (uri parameter) The node's name
        @apiParam   {String}    output=yaml     (query parameter) Output result. Example : json
        @apiSuccess {Number}    id              The hostgroup's id.
        @apiSuccess {String}    name            The hostgroup's name.
        @apiSuccess {Datetime}  insert_date     The hostgroup's inserted date
        @apiSuccess {Datetime}  update_date     The hostgroup's updated date
        @apiSuccess {Datetime}  delete_date     The hostgroup's deleted date
        """
        output = str(request.args.get('output', 'yaml'))

        if not node_name:
            obj = Node.query.paginate(page, 10).items
            return { "success": False, "message": "No node provided" }, 304
        else:

            node = Node.query.filter_by(name=node_name).first()
            if not node:
                return { "success": False, "message": "Node not found" }, 404

            if node.hostgroup_id is None or node.environment_id is None:
                class_name = ''
                hostgroup_name = ''
                environment_name = ''
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

                class_name       = hg_class.class_name
                hostgroup_name   = hg_class.hostgroup_name


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

                environment_name = environment_node.environment_name


            if not hostgroup_name:
                hostgroup_name = ''

            if not environment_name:
                environment_name = ''

            app.logger.info('Get ENC on %s, by %s', node_name, g.user)
            # We need to display it on "ENC" format
            res = {
                'classes': [
                    class_name,
                ],
                'parameters': {
                    'puppetmaster': '',
                    'hostgroup': hostgroup_name
                },
                'environment': environment_name
            }

            if not res:
                return { "success": False, "message": "Node not found" }, 404
            else:
                if output == 'json':
                    return jsonify(res, 200)
                else:
                    return output_yaml(res, 200)
