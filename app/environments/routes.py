from flask_restful import Resource
from flask import jsonify, request

from app.puppenc import api, db, app, auth, PuppencResource
from app.decorators import *

from app.environments.models import Environment
from app.environments.schema import EnvironmentSchema

class Environments(PuppencResource):
    def __init__(self):
        self.environment_schema = EnvironmentSchema()
        self.environments_schema = EnvironmentSchema(many=True)

    @auth.login_required
    @get_item(Environment)
    def get(self, id=None):
        """
        @api {get} /environments Get all environments
        @apiName get_environments
        @apiGroup Environments
        @apiVersion 1.0.0
        @apiPermission user
        @apiParam   {String}    [limit=10]      (query parameter) Objects per page to display. Use limit=0 for disabling limit
        @apiParam   {String}    [page=1]        (query parameter) Current page
        @apiParam   {String}    [filter]        (query parameter) Filter on name parameter (use * for searching any strings. Ex: *maclass*)
        @apiSuccess {Number}    id              The environment's id
        @apiSuccess {String}    name            The environment's name
        @apiSuccess {Array}     nodes           The environment's nodes (by id)
        @apiSuccess {Datetime}  insert_date     The environment's inserted date
        @apiSuccess {Datetime}  update_date     The environment's updated date
        @apiSuccess {Datetime}  delete_date     The environment's deleted date
        @apiExample {curl} Example usage :
            curl -X GET -u user:pwd http://127.0.0.1:5000/api/v1/environments
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            [
              {
                "delete_date": null,
                "id": 1,
                "insert_date": "2017-04-11T13:56:03+00:00",
                "name": "stable",
                "nodes": [
                  104,
                  2582,
                  2588
                ],
                "update_date": null
              },
              {
                "delete_date": null,
                "id": 2,
                "insert_date": "2017-04-11T13:56:04+00:00",
                "name": "staging",
                "nodes": [
                  8,
                  34,
                  42
                ],
                "update_date": null
              }
            ]
        """
        """
        @api {get} /environments/:id Get a single environment
        @apiName get_environment
        @apiGroup Environments
        @apiVersion 1.0.0
        @apiPermission user
        @apiParam   {Number}    id              (uri parameter) The environment's id.
        @apiSuccess {Number}    id              The environment's id.
        @apiSuccess {String}    name            The environment's name.
        @apiSuccess {Array}     nodes           The environment's nodes (by id)
        @apiSuccess {Datetime}  insert_date     The environment's inserted date
        @apiSuccess {Datetime}  update_date     The environment's updated date
        @apiSuccess {Datetime}  delete_date     The environment's deleted date
        @apiExample {curl} Example usage :
            curl -X GET -u user:pwd http://127.0.0.1:5000/api/v1/environments/1
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            {
              "delete_date": null,
              "id": 2,
              "insert_date": "2017-04-11T13:56:03+00:00",
              "name": "my_environment",
              "nodes": [
                1498,
                2817,
                2818
              ],
              "update_date": null
            }
        """
        if not id:
            return self.environments_schema.jsonify(g.obj_info)
        else:
            return self.environment_schema.jsonify(g.obj_info)

    @auth.login_required
    @body_is_valid
    @is_unique_item(Environment)
    @post_item(Environment)
    def post(self):
        """
        @api {post} /environments Add a new environment
        @apiName add_environment
        @apiGroup Environments
        @apiVersion 1.0.0
        @apiPermission user
        @apiParam   {String}    name            (json document) The environment's name.
        @apiSuccess {Number}    id              The environment's id.
        @apiExample {curl} Example usage :
            curl -X POST -H "Content-Type: application/json" \
            -d '{ "name": "my_new_environment" }' \
            http://127.0.0.1:5000/api/v1/environments
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            {
              "227": {
                "name": "my_new_environment"
              }
            }
        """
        pass

    @auth.login_required
    @body_is_valid
    @is_unique_item(Environment)
    @get_item(Environment)
    @edit_item(Environment)
    def put(self, id=None):
        """
        @api {put} /environments/:id Edit an existing environment
        @apiName edit_environment
        @apiGroup Environments
        @apiVersion 1.0.0
        @apiPermission user
        @apiParam   {String}    name            (uri parameter) The environment's id
        @apiParam   {String}    name            (json document) The new environment's name
        @apiSuccess {Number}    success         True if success
        @apiSuccess {Number}    message         A information message
        @apiExample {curl} Example usage :
            curl -X PUT -H "Content-Type: application/json" \
            -d '{ "name": "my_new_environment" }' \
            http://127.0.0.1:5000/api/v1/environments/:id
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            {
                "message": "successfully modified",
                "success": true
            }
        """
        pass

    @auth.login_required
    @get_item(Environment)
    @delete_item(Environment)
    def delete(self, id):
        """
        @api {delete} /environments/:id Delete a single environment
        @apiName rm_hostgorup
        @apiGroup Environments
        @apiVersion 1.0.0
        @apiPermission user
        @apiParam   {Number}    id              (uri parameter) The environment's id.
        @apiSuccess {Boolean}   success         Success (True if ok).
        @apiSuccess {String}    message         A success or error message.
        @apiExample {curl} Example usage :
            curl -X DELETE http://127.0.0.1:5000/api/v1/environments/:id
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            {
                "message": "<Environment 'my_new_environment'> deleted",
                "success": true
            }
        """
        pass
