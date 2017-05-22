from flask_restful import Resource
from flask import jsonify, request, g

from app.puppenc import app, api, db, output_yaml, auth, PuppencResource
import json

from app.nodes.models import Node
from app.hostgroups.models import Hostgroup
from app.environments.models import Environment
from app.classes.models import Class
from app.variables.models import Variable

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
        @apiParam   {String}    [output=yaml]     (query parameter) Output result. Avaiable methods : yaml / json
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
                return { "success": False, "message": "Please, set a hostgroup and an environment" }, 404
            else:
                # I have an hostgroup or an environment, we can continue
                data = Node.query.join(
                    Hostgroup,
                    Node.hostgroup_id==Hostgroup.id,
                ).join(
                    Class,
                    Hostgroup.class_id==Class.id
                ).join(
                    Environment,
                    Node.environment_id==Environment.id
                ).add_columns(
                    Class.name.label('class_name'),
                    Hostgroup.name.label('hostgroup_name'),
                    Environment.name.label('environment_name')
                ).filter(
                    Node.name == node_name
                ).first()

                if not data:
                    # I have all except a class in my hostgroup
                    app.logger.warning('No class for the node %s', node_name)
                    class_name = ''

                    # Let's make a different request to handle a missing class
                    data = Node.query.join(
                        Hostgroup,
                        Node.hostgroup_id==Hostgroup.id,
                    ).join(
                        Environment,
                        Node.environment_id==Environment.id
                    ).add_columns(
                        Hostgroup.name.label('hostgroup_name'),
                        Environment.name.label('environment_name')
                    ).filter(
                        Node.name == node_name
                    ).first()

                else:
                    class_name = data.class_name

                hostgroup_name = data.hostgroup_name
                environment_name = data.environment_name

                # Parameters now
                params = {}
                params['parameters'] = {}
                # legacy
                params['parameters']['puppetmaster'] = ''
                params['parameters']['hostgroup'] = hostgroup_name

                for p in node.nodes_var:
                    if p.content == 'true':
                        content = True
                    elif p.content == 'false':
                        content = False
                    else:
                        if p.content[0] == '{':
                            try:
                                content = json.loads(p.content)
                            except:
                                app.logger.info('unable to format json')
                        else:
                            content = p.content

                    params['parameters'][p.name] = content

                app.logger.info('Get ENC on %s, by %s', node_name, g.user)
                # We need to display it on "ENC" format
                base = {
                    'classes': [
                        class_name,
                    ],
                    'environment': environment_name
                }

                res = base.copy()
                res.update(params)

                if output == 'json':
                    return jsonify(res, 200)
                else:
                    return output_yaml(res, 200)
