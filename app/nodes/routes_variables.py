from flask_restful import Resource
from flask import jsonify, request, g

from sqlalchemy import exc

from app.puppenc import api, db, app, auth, PuppencResource
from app.decorators import *

from app.nodes.models import Node
from app.variables.models import Variable, NodeVariable
from app.nodes.schema import NodeSchema

class NodesVariables(PuppencResource):
    @auth.login_required
    @body_is_valid
    @get_item(Node)
    def post(self, id=None):
        """
        @api {post} /nodes/:id/variables Assign an existing variable to a node
        @apiVersion 1.0.0
        @apiName add_variable_to_node
        @apiPermission user
        @apiDescription The variable need to be created before.
        @apiGroup Nodes
        @apiParam   {Number}    id            The node's id
        @apiParam   {Number}    variable_id   The variable's id
        @apiSuccess {Number}    id            The node's id.
        @apiExample {curl} Example usage :
            curl -X POST -H "Content-Type: application/json" \
            -d '{ "variable_id": 1 }' \
            http://127.0.0.1:5000/api/v1/nodes/2/variables
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            {
                "message": "Successfully assign the variable <Variable 'name'> to the node <Node 'server01'>",
                "success": true
            }
        """
        content = request.get_json(silent=True)
        if not 'variable_id' in content:
            return { "success": False, "message": u"variable_id parameter is mandatory, check the documentation" }, 400

        # I assume the node exists, because of @get_item decorator
        obj_node = Node.query.filter_by(id=int(id)).first()

        obj_var = Variable.query.filter_by(id=int(content['variable_id'])).first()
        if not obj_var:
            return { "success": False, "message": u"Variable %s not found" % (content['variable_id'])  }, 404


        nb_variables_for_node = obj_node.nodes_var.count(obj_var)

        if nb_variables_for_node > 0:
            return { "success": False, "message": u"This variable is already associated to this node"  }, 200
        else:
            try:
                t = NodeVariable(id, content['variable_id'])
                db.session.add(t)
                db.session.commit()
                return { "success": True, "message": u"Successfully assign the variable %s to the node %s" % (obj_var, obj_node) }, 200
            except exc.IntegrityError:
                return { "success": False, "message": u"Something went wrong when adding the variable %s to %s" % (obj_var, obj_node)  }, 500

    @auth.login_required
    @get_item(Node)
    def delete(self, id):
        """
        @api {delete} /nodes/:id/variables Unassign an existing variable to a node
        @apiVersion 1.0.0
        @apiName rm_variable_to_node
        @apiPermission user
        @apiGroup Nodes
        @apiParam   {Number}    id            The node's id
        @apiParam   {Number}    variable_id   The variable's id
        @apiSuccess {Number}    id            The node's id.
        @apiExample {curl} Example usage :
            curl -X DELETE -H "Content-Type: application/json" \
            -d '{ "variable_id": 1 }' \
            http://127.0.0.1:5000/api/v1/nodes/2/variables
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            {
                "message": "OK",
                "success": true
            }

        """

        try:
            content = request.get_json(silent=True)
            t = Node.query.get(id)
            a = Variable.query.get(content['variable_id'])
            t.nodes_var.remove(a)
            db.session.commit()
            return { "success": True, "message": u"OK" }, 200
        except Exception as error:
            return { "success": False, "message": u"Something went wrong when deleting : %s" % (error)  }, 500
