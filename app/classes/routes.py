from flask_restful import Resource
from flask import jsonify, request

from app.puppenc import api, db

from app.classes.models import Class
from app.classes.schema import ClassSchema

class Classes(Resource):
    def __init__(self):
        self.class_schema = ClassSchema()
        self.classes_schema = ClassSchema(many=True)

    def get(self, page=1, id=None):
        """
        @api {get} /classes Get all classes
        @apiVersion 1.0.0
        @apiName get_classes
        @apiGroup Classes
        @apiSuccess {Number}    id              The class's id.
        @apiSuccess {String}    name            The class's name.
        @apiSuccess {Datetime}  insert_date     The class's inserted date
        @apiSuccess {Datetime}  update_date     The class's updated date
        @apiSuccess {Datetime}  delete_date     The class's deleted date
        """

        """
        @api {get} /classes/<id> Get a single class
        @apiVersion 1.0.0
        @apiName get_class
        @apiGroup Classes
        @apiParam   {Number}    id              The class's id.
        @apiSuccess {Number}    id              The class's id.
        @apiSuccess {String}    name            The class's name.
        @apiSuccess {Datetime}  insert_date     The class's inserted date
        @apiSuccess {Datetime}  update_date     The class's updated date
        @apiSuccess {Datetime}  delete_date     The class's deleted date
        """
        if not id:
            obj = Class.query.paginate(page, 10).items
            return self.classes_schema.jsonify(obj)
        else:
            obj = Class.query.filter_by(id=id).first()
            if not obj:
                return { "success": False, "message": "Class not found" }, 404
            return self.class_schema.jsonify(obj)


    def post(self, id=None):
        """
        @api {post} /classes Add a new class
        @apiVersion 1.0.0
        @apiName add_class
        @apiGroup Classes
        @apiParam   {String}    name            The class's name.
        @apiSuccess {Number}    id              The class's id.
        @apiExample {curl} Example usage :
            curl -X POST -H "Content-Type: application/json" \
            -d '{ "name": "role::my_class" }' \
            http://127.0.0.1:5000/api/v1/classes
        """
        content = request.get_json(silent=True)
        if not 'name' in content:
            return { "success": False, "message": "No name given for this class" }, 500
        else:
            name = content['name']

        # Check if the class already exists
        exists = db.session.query(db.exists().where(Class.name == name)).scalar()
        if exists:
            return { "success": False, "message": "Class already exists" }, 200

        obj = Class(name)
        db.session.add(obj)
        db.session.commit()

        return jsonify({obj.id: {
            'name': obj.name,
        }})

    def delete(self, id):
        """
        @api {delete} /classes/<id> Delete a single class
        @apiVersion 1.0.0
        @apiName rm_class
        @apiGroup Classes
        @apiParam   {Number}    id              The class's id.
        @apiSuccess {Boolean}   success         Success (True if ok).
        @apiSuccess {String}    message         A success or error message.
        @apiExample {curl} Example usage :
            curl -X DELETE http://127.0.0.1:5000/api/v1/classes/<id>
        """
        class_obj = Class.query.filter_by(id=id).first()
        if not environment:
            return { "success": False, "message": "Class not found" }, 304
        else:
            db.session.delete(class_obj)
            db.session.commit()
            return { "success": True }, 200

# Let's expose something :)
api.add_resource(Classes, '/classes', '/classes/<int:id>')
