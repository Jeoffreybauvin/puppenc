from flask_restful import Resource
from flask import jsonify, request

from app.puppenc import api, db, app, auth, PuppencResource
from app.decorators import *

from app.hostgroups.models import Hostgroup
from app.hostgroups.schema import HostgroupSchema

class Hostgroups(PuppencResource):
    def __init__(self):
        self.hostgroup_schema = HostgroupSchema()
        self.hostgroups_schema = HostgroupSchema(many=True)

    @auth.login_required
    @get_item(Hostgroup)
    def get(self, page=1, id=None):
        """
        @api {get} /hostgroups Get all hostgroups
        @apiVersion 1.0.0
        @apiName get_hostgroups
        @apiGroup Hostgroups
        @apiSuccess {Number}    id              The hostgroup's id.
        @apiSuccess {String}    name            The hostgroup's name.
        @apiSuccess {Datetime}  insert_date     The hostgroup's inserted date
        @apiSuccess {Datetime}  update_date     The hostgroup's updated date
        @apiSuccess {Datetime}  delete_date     The hostgroup's deleted date
        """

        """
        @api {get} /hostgroups/<id> Get a single hostgroup
        @apiVersion 1.0.0
        @apiName get_hostgroup
        @apiGroup Hostgroups
        @apiParam   {Number}    id              The hostgroup's id.
        @apiSuccess {Number}    id              The hostgroup's id.
        @apiSuccess {String}    name            The hostgroup's name.
        @apiSuccess {Datetime}  insert_date     The hostgroup's inserted date
        @apiSuccess {Datetime}  update_date     The hostgroup's updated date
        @apiSuccess {Datetime}  delete_date     The hostgroup's deleted date
        """
        if not id:
            return self.hostgroups_schema.jsonify(g.obj_info)
        else:
            return self.hostgroup_schema.jsonify(g.obj_info)

    @auth.login_required
    @is_unique_item(Hostgroup)
    @body_is_valid
    @post_item(Hostgroup)
    def post(self, id=None):
        """
        @api {post} /hostgroups Add a new hostgroup
        @apiVersion 1.0.0
        @apiName add_hostgroup
        @apiGroup Hostgroups
        @apiParam   {String}    name            The hostgroup's name.
        @apiSuccess {Number}    id              The hostgroup's id.
        """
        pass

    @auth.login_required
    @get_item(Hostgroup)
    @delete_item(Hostgroup)
    def delete(self, id):
        """
        @api {delete} /hostgroups/<id> Delete a single hostgroup
        @apiVersion 1.0.0
        @apiName rm_hostgorup
        @apiGroup Hostgroups
        @apiParam   {Number}    id              The hostgroup's id.
        @apiSuccess {Boolean}   success         Success (True if ok).
        @apiSuccess {String}    message         A success or error message.
        """
        pass
