from flask_restful import Resource
from flask import jsonify, request

from app.puppenc import api, db

from app.hostgroups.models import Hostgroup
from app.hostgroups.schema import HostgroupSchema

class Hostgroups(Resource):
    def __init__(self):
        self.hostgroup_schema = HostgroupSchema()
        self.hostgroups_schema = HostgroupSchema(many=True)

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
            obj = Hostgroup.query.paginate(page, 10).items
            return self.hostgroups_schema.jsonify(obj)
        else:
            obj = Hostgroup.query.filter_by(id=id).first()
            if not obj:
                abort(404)
            return self.hostgroup_schema.jsonify(obj)


    def post(self, id=None):
        """
        @api {post} /hostgroups Add a new hostgroup
        @apiVersion 1.0.0
        @apiName add_hostgroup
        @apiGroup Hostgroups
        @apiParam   {String}    name            The hostgroup's name.
        @apiSuccess {Number}    id              The hostgroup's id.
        """
        content = request.get_json(silent=True)
        name = content['name']
        class_id = content['class_id']
        obj = Hostgroup(name, class_id)
        db.session.add(obj)
        db.session.commit()

        return jsonify({obj.id: {
            'name': obj.name,
        }})

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
        hostgroup = Environment.query.filter_by(id=id).first()
        if not environment:
            return { "success": False, "message": "Environment not found" }, 304
        else:
            db.session.delete(environment)
            db.session.commit()
            return { "success": True }, 200

# Let's expose something :)
api.add_resource(Hostgroups, '/hostgroups', '/hostgroups/<int:id>')
