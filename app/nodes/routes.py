from flask_restful import Resource
from flask import jsonify, request, g

from sqlalchemy import exc

from app.puppenc import api, db, app, auth, PuppencResource
from app.decorators import *

from app.nodes.models import Node
from app.nodes.schema import NodeSchema

class Nodes(PuppencResource):
    def __init__(self):
        self.node_schema = NodeSchema()
        self.nodes_schema = NodeSchema(many=True)

    @auth.login_required
    @get_item(Node)
    def get(self, id=None):
        """
        @api {get} /nodes Get all nodes
        @apiName get_nodes
        @apiGroup Nodes
        @apiVersion 1.0.0
        @apiPermission user
        @apiParam   {String}    [limit=10]      (query parameter) Objects per page to display. Use limit=0 for disabling limit
        @apiParam   {String}    [page=1]        (query parameter) Current page
        @apiParam   {String}    [filter]        (query parameter) Filter on name parameter (use * for searching any strings. Ex: *maclass*)
        @apiSuccess {Number}    id              The node's id.
        @apiSuccess {String}    name            The node's name.
        @apiSuccess {Array}     nodes_var       The node's variables (by id)
        @apiSuccess {Datetime}  insert_date     The node's inserted date
        @apiSuccess {Datetime}  update_date     The node's updated date
        @apiSuccess {Datetime}  delete_date     The node's deleted date
        @apiSuccess {Datetime}  last_used       The node's last use threw /nodes or /enc
        @apiExample {curl} Example usage :
            curl -X GET -u user:pwd http://127.0.0.1:5000/api/v1/nodes
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            [
              {
                "active": 1,
                "delete_date": null,
                "environment_id": 2,
                "hostgroup_id": 1,
                "id": 8,
                "insert_date": "2017-04-11T14:00:38+00:00",
                "last_used": "2017-04-11T14:00:38+00:00",
                "name": "server01",
                "nodes_var": [
                    1,
                    2
                ],
                "update_date": null
              },
              {
                "active": 1,
                "delete_date": null,
                "environment_id": 2,
                "hostgroup_id": 13,
                "id": 34,
                "insert_date": "2017-04-11T13:59:20+00:00",
                "name": "server02",
                "nodes_var": [],
                "update_date": null
              }
            ]
        """
        """
        @api {get} /nodes/:id Get a single node
        @apiVersion 1.0.0
        @apiName get_node
        @apiPermission user
        @apiGroup Nodes
        @apiParam   {Number}    id              The node's id.
        @apiSuccess {Number}    id              The node's id.
        @apiSuccess {String}    name            The node's name.
        @apiSuccess {Datetime}  insert_date     The node's inserted date
        @apiSuccess {Datetime}  update_date     The node's updated date
        @apiSuccess {Datetime}  delete_date     The node's deleted date
        @apiExample {curl} Example usage :
            curl -X GET -u user:pwd http://127.0.0.1:5000/api/v1/nodes/1
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            {
              "active": 1,
              "delete_date": null,
              "environment_id": 2,
              "hostgroup_id": 36,
              "id": 1,
              "insert_date": "2017-04-11T13:59:20+00:00",
              "name": "server02",
              "nodes_var": [],
              "update_date": null
            }
        """
        if not id:
            return self.nodes_schema.jsonify(g.obj_info)
        else:
            return self.node_schema.jsonify(g.obj_info)


    @auth.login_required
    @is_unique_item(Node)
    @body_is_valid
    # @post_item(Node)
    def post(self, id=None):
        """
        @api {post} /nodes Add a new node
        @apiVersion 1.0.0
        @apiName add_node
        @apiPermission user
        @apiGroup Nodes
        @apiParam   {String}    name            The node's name.
        @apiSuccess {Number}    id              The node's id.
        @apiExample {curl} Example usage :
            curl -X POST -H "Content-Type: application/json" \
            -d '{ "name": "my_server", "environment_id":1 }' \
            http://127.0.0.1:5000/api/v1/nodes
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            {
              "2826": {
                "name": "my_server"
              }
            }
        """
        content = request.get_json(silent=True)
        if not 'environment_id' in content:
            environment_id = None
        else:
            environment_id = content['environment_id']

        if not 'hostgroup_id' in content:
            hostgroup_id = None
        else:
            hostgroup_id = content['hostgroup_id']

        obj = Node(g.obj_name, hostgroup_id=hostgroup_id, environment_id=environment_id)
        db.session.add(obj)
        db.session.commit()
        app.logger.info(u"Create Item %s %s by %s" % (Node, g.obj_name, g.user))
        return jsonify({obj.id: {
            'name': obj.name,
        }})


    @auth.login_required
    def put(self, id):
        """
        @api {put} /nodes/:id Edit a node
        @apiVersion 1.0.0
        @apiName put_node
        @apiGroup Nodes
        @apiPermission user
        @apiParam {Number}    id              The node's id.
        @apiParam {String}    name            The node's name.
        @apiParam {Number}    environment_id  The node's environment_id.
        @apiParam {Number}    hostgroup_id    The node's hostgroup_id.
        @apiSuccess {Boolean}   success         Success (True if ok).
        @apiSuccess {String}    message         A success or error message.
        @apiExample {curl} Example usage :
            curl -X PUT -H "Content-Type: application/json" \
            -d '{ "name": "my_new_server" }' \
            http://127.0.0.1:5000/api/v1/nodes/1
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            {
                "message": "successfully modified",
                "success": true
            }

        """
        node = Node.query.filter_by(id=id).first()
        if not node:
            return { "success": False, "message": "Node not found" }, 304
        else:
            Node.query.filter_by(id=id).update({ "update_date": db.func.current_timestamp() }, synchronize_session=False)

            content = request.get_json(silent=True)
            if 'name' in content:
                Node.query.filter_by(id=id).update({ "name": content['name'] }, synchronize_session=False)

            if 'environment_id' in content:
                try:
                    Node.query.filter_by(id=id).update({ "environment_id": content['environment_id'] }, synchronize_session=False)
                except exc.SQLAlchemyError:
                    return { "success": False, "message": "Environment not found" }, 301

            if 'hostgroup_id' in content:
                try:
                    Node.query.filter_by(id=id).update({ "hostgroup_id": content['hostgroup_id'] }, synchronize_session=False)
                except exc.SQLAlchemyError:
                    app.logger.info(u"Cannot edit node %s : hostgroup %s not found" % (id, content['hostgroup_id']))
                    return { "success": False, "message": "Hostgroup not found" }, 301


            db.session.commit()
            return { "success": True, "message": "successfully modified" }, 200

    @auth.login_required
    @get_item(Node)
    def delete(self, id):
        """
        @api {delete} /nodes/:id Delete a single node
        @apiVersion 1.0.0
        @apiDescription Delete will not delete the node from the database
            The flag active is set to 0, and delete_date is set to NOW()
        @apiPermission user
        @apiName rm_node
        @apiGroup Nodes
        @apiParam   {Number}    id              The node's id.
        @apiSuccess {Boolean}   success         Success (True if ok).
        @apiSuccess {String}    message         A success or error message.
        @apiExample {curl} Example usage :
            curl -X DELETE http://127.0.0.1:5000/api/v1/nodes/:id
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            {
                "success": true
            }
        """
        if g.obj_info.active == 1:
            Node.query.filter_by(id=id).update({ "active": 0, "delete_date": db.func.current_timestamp() }, synchronize_session=False)
            db.session.commit()
            return { "success": True }, 200
        else:
            # Node is already deactivated, we can delete it
            db.session.delete(g.obj_info)
            db.session.commit()
            app.logger.info(u"Delete Item %s" % g.user)
            app.logger.info(u"%s Node %s by %s" % (request.method, g.obj_info, g.user))
            return { "success": True, "message": u"%s deleted" % g.obj_info }, 200
