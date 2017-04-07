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
        @apiVersion 1.0.0
        @apiName get_environments
        @apiPermission user
        @apiGroup Environments
        @apiSuccess {Number}    id              The environment's id.
        @apiSuccess {String}    name            The environment's name.
        @apiSuccess {Datetime}  insert_date     The environment's inserted date
        @apiSuccess {Datetime}  update_date     The environment's updated date
        @apiSuccess {Datetime}  delete_date     The environment's deleted date
        """

        """
        @api {get} /environments/<id> Get a single environment
        @apiVersion 1.0.0
        @apiPermission user
        @apiName get_environment
        @apiGroup Environments
        @apiParam   {Number}    id              The environment's id.
        @apiSuccess {Number}    id              The environment's id.
        @apiSuccess {String}    name            The environment's name.
        @apiSuccess {Datetime}  insert_date     The environment's inserted date
        @apiSuccess {Datetime}  update_date     The environment's updated date
        @apiSuccess {Datetime}  delete_date     The environment's deleted date
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
        @apiVersion 1.0.0
        @apiName add_environment
        @apiPermission user
        @apiGroup Environments
        @apiParam   {String}    name            The environment's name.
        @apiSuccess {Number}    id              The environment's id.
        """
        pass

    @auth.login_required
    @body_is_valid
    @is_unique_item(Environment)
    @get_item(Environment)
    @edit_item(Environment)
    def put(self, id=None):
        """
        @api {put} /environments/<id> Edit an existing environment
        @apiVersion 1.0.0
        @apiName edit_environment
        @apiPermission user
        @apiGroup Environments
        @apiParam   {String}    name            The environment's name.
        @apiSuccess {Number}    success         True if success
        @apiSuccess {Number}    message         A information message
        @apiExample {curl} Example usage :
            curl -X PUT -H "Content-Type: application/json" \
            -d '{ "name": "my_new_environment" }' \
            http://127.0.0.1:5000/api/v1/environments/<id>
        """
        pass

    @auth.login_required
    @get_item(Environment)
    @delete_item(Environment)
    def delete(self, id):
        """
        @api {delete} /environments/<id> Delete a single environment
        @apiVersion 1.0.0
        @apiName rm_hostgorup
        @apiGroup Environments
        @apiPermission user
        @apiParam   {Number}    id              The environment's id.
        @apiSuccess {Boolean}   success         Success (True if ok).
        @apiSuccess {String}    message         A success or error message.
        """
        pass
