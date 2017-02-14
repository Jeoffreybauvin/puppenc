from flask_restful import Resource
from flask import jsonify, request
from app.puppenc import api, db, parser
from app.objects.models import Environment, Class

class Objects(Resource):
    def get(self, page=1, id=None):
        """
        @api {get} /environments Get all Environments
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
        @api {get} /environments/<id> Get a single Environment
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
            environments = Environment.query.paginate(page, 10).items
            res = {}
            for env in environments:
                res[env.id] = {
                    'name': env.name,
                    'insert_date': env.insert_date,
                    'update_date': env.update_date,
                    'delete_date': env.delete_date,
                }
        else:
            environment = Environment.query.filter_by(id=id).first()
            if not environment:
                abort(404)
            res = {
                'name': environment.name,
                'insert_date': environment.insert_date,
                'update_date': environment.update_date,
                'delete_date': environment.delete_date,
            }
        return jsonify(res)


    def post(self, id=None):
        """
        @api {post} /environments Add a new Environment
        @apiVersion 1.0.0
        @apiName add_environment
        @apiGroup Environments
        @apiParam   {String}    name            The environment's name.
        @apiSuccess {Number}    id              The environment's id.
        """
        content = request.get_json(silent=True)
        name = content['name']
        environment = Environment(name)

        db.session.add(environment)
        db.session.commit()

        return jsonify({environment.id: {
            'name': environment.name,
        }})

    def delete(self, id):
        """
        @api {delete} /environments/<id> Delete a single Environment
        @apiVersion 1.0.0
        @apiName rm_environment
        @apiGroup Environments
        @apiParam   {Number}    id              The environment's id.
        @apiSuccess {Boolean}   success         Success (True if ok).
        @apiSuccess {String}    message         A success or error message.
        """
        environment = Environment.query.filter_by(id=id).first()
        if not environment:
            return { "success": False, "message": "Environment not found" }, 304
        else:
            db.session.delete(environment)
            db.session.commit()
            return { "success": True }, 200


api.add_resource(
    Objects,
    '/environments',
    '/environments/<int:id>',
    '/classes'
)
