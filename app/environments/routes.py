from flask_restful import Resource
from flask import jsonify, request

from app.puppenc import api, db

from app.environments.models import Environment
from app.environments.schema import EnvironmentSchema

class Environments(Resource):
    def __init__(self):
        self.environment_schema = EnvironmentSchema()
        self.environments_schema = EnvironmentSchema(many=True)

    def get(self, page=1, id=None):
        """
        @api {get} /environments Get all environments
        @apiVersion 1.0.0
        @apiName get_environments
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
            obj = Environment.query.paginate(page, 10).items
            return self.environments_schema.jsonify(obj)
        else:
            obj = Environment.query.filter_by(id=id).first()
            if not obj:
                return { "success": False, "message": "Environment not found" }, 404
            return self.environment_schema.jsonify(obj)


    def post(self):
        """
        @api {post} /environments Add a new environment
        @apiVersion 1.0.0
        @apiName add_environment
        @apiGroup Environments
        @apiParam   {String}    name            The environment's name.
        @apiSuccess {Number}    id              The environment's id.
        """
        content = request.get_json(silent=True)
        name = content['name']
        obj = Environment(name)
        db.session.add(obj)
        db.session.commit()

        return jsonify({obj.id: {
            'name': obj.name,
        }})

    def delete(self, id):
        """
        @api {delete} /environments/<id> Delete a single environment
        @apiVersion 1.0.0
        @apiName rm_hostgorup
        @apiGroup Environments
        @apiParam   {Number}    id              The environment's id.
        @apiSuccess {Boolean}   success         Success (True if ok).
        @apiSuccess {String}    message         A success or error message.
        """
        environment_obj = Environment.query.filter_by(id=id).first()
        if not environment:
            return { "success": False, "message": "Environment not found" }, 304
        else:
            db.session.delete(environment_obj)
            db.session.commit()
            return { "success": True }, 200

# Let's expose something :)
api.add_resource(Environments, '/environments', '/environments/<int:id>')
