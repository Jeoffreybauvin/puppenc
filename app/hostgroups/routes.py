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
    def get(self, id=None):
        """
        @api {get} /hostgroups Get all hostgroups
        @apiName get_hostgroups
        @apiGroup Hostgroups
        @apiVersion 1.0.0
        @apiPermission user
        @apiParam   {String}    [limit=10]      (query parameter) Objects per page to display. Use limit=0 for disabling limit
        @apiParam   {String}    [page=1]        (query parameter) Current page
        @apiParam   {String}    [filter]        (query parameter) Filter on name parameter (use * for searching any strings. Ex: *maclass*)
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
        @apiPermission user
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
    # @post_item(Hostgroup)
    def post(self, id=None):
        """
        @api {post} /hostgroups Add a new hostgroup
        @apiVersion 1.0.0
        @apiName add_hostgroup
        @apiPermission user
        @apiGroup Hostgroups
        @apiParam   {String}    name            The hostgroup's name.
        @apiParam   {Number}    class_id        The related class id.
        @apiSuccess {Number}    id              The hostgroup's id.
        """
        content = request.get_json(silent=True)
        if not 'class_id' in content:
            class_id = None
        else:
            class_id = content['class_id']

        obj = Hostgroup(g.obj_name, class_id=class_id)
        db.session.add(obj)
        db.session.commit()
        app.logger.info(u"Create Hostgroup %s %s by %s" % (Hostgroup, g.obj_name, g.user))
        return jsonify({obj.id: {
            'name': obj.name,
        }})

    @auth.login_required
    @edit_item(Hostgroup)
    def put(self, id):
        """
        @api {put} /hostgroups/:id Edit an hostgroup
        @apiVersion 1.0.0
        @apiName put_hostgroup
        @apiGroup Hostgroups
        @apiPermission user
        @apiParam {Number}    id              The hostgroup's id.
        @apiParam {String}    name            The hostgroup's name.
        @apiParam {Number}    class_id        The hostgroup's class_id.
        @apiSuccess {Boolean}   success         Success (True if ok).
        @apiSuccess {String}    message         A success or error message.
        @apiExample {curl} Example usage :
            curl -X PUT -H "Content-Type: application/json" \
            -d '{ "name": "my_new_hostgroup" }' \
            http://127.0.0.1:5000/api/v1/hostgroups/1
        """
        pass

    @auth.login_required
    @get_item(Hostgroup)
    @delete_item(Hostgroup)
    def delete(self, id):
        """
        @api {delete} /hostgroups/<id> Delete a single hostgroup
        @apiVersion 1.0.0
        @apiPermission user
        @apiName rm_hostgorup
        @apiGroup Hostgroups
        @apiParam   {Number}    id              The hostgroup's id.
        @apiSuccess {Boolean}   success         Success (True if ok).
        @apiSuccess {String}    message         A success or error message.
        """
        pass
