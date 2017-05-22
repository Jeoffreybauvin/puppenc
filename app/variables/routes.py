from flask_restful import Resource
from flask import jsonify, request, g

from app.puppenc import api, db, app, auth, PuppencResource
from app.decorators import *

from app.variables.models import Variable
from app.variables.schema import VariableSchema

class Variables(PuppencResource):
    def __init__(self):
        self.variable_schema = VariableSchema()
        self.variables_schema = VariableSchema(many=True)

    @auth.login_required
    @get_item(Variable)
    def get(self, id=None):
        """
        @api {get} /variables Get all variables
        @apiName get_variables
        @apiGroup Variables
        @apiVersion 1.0.0
        @apiPermission user
        @apiParam   {String}    [limit=10]      (query parameter) Objects per page to display
        @apiParam   {String}    [page=1]        (query parameter) Current page
        @apiParam   {String}    [filter]        (query parameter) Filter on name parameter (use * for searching any strings. Ex: *mavariable*)
        @apiSuccess {Number}    id              The variable's id.
        @apiSuccess {String}    name            The variable's name.
        @apiSuccess {Datetime}  insert_date     The variable's inserted date
        @apiSuccess {Datetime}  update_date     The variable's updated date
        @apiSuccess {Datetime}  delete_date     The variable's deleted date
        @apiExample {curl} Example usage :
            curl -X GET -u user:pwd http://127.0.0.1:5000/api/v1/variables
        """

        """
        @api {get} /variables/:id Get a single variable
        @apiName get_variable
        @apiGroup Variables
        @apiVersion 1.0.0
        @apiPermission user
        @apiParam   {Number}    id              The variable's id.
        @apiSuccess {Number}    id              The variable's id.
        @apiSuccess {String}    name            The variable's name.
        @apiSuccess {Datetime}  insert_date     The variable's inserted date
        @apiSuccess {Datetime}  update_date     The variable's updated date
        @apiSuccess {Datetime}  delete_date     The variable's deleted date
        @apiExample {curl} Example usage :
            curl -X GET http://127.0.0.1:5000/api/v1/variables/:id
        """
        if not id:
            return self.variables_schema.jsonify(g.obj_info)
        else:
            return self.variable_schema.jsonify(g.obj_info)

    @auth.login_required
    @body_is_valid
    @is_unique_item(Variable)
    # @post_item(Variable)
    def post(self, id=None):
        """
        @api {post} /variables Add a new variable
        @apiVersion 1.0.0
        @apiName add_variable
        @apiGroup Variables
        @apiDescription Strings named true or false are automatically converted to Booleans. Strings in json format are automatically converted to objects.
        @apiParam   {String}    name            The variable's name.
        @apiParam   {String}    content         The variable's content : you can use json here to specify arrays.
        @apiPermission user
        @apiSuccess {Number}    id              The variable's id.
        @apiExample {curl} Simple string
            curl -X POST -H "Content-Type: application/json" \
            -d '{ "name": "my_variable", "content": "my_content" }' \
            http://127.0.0.1:5000/api/v1/variables
        @apiExample {curl} JSON
            curl -i -X POST -H "Content-Type: application/json" \
            -d '{ "name": "array", "content":"{\"ntp_servers\": [ \"ntp1\", \"ntp2\" ] }" }' \
            http://127.0.0.1:5000/api/v1/variables
        """
        data = request.get_json(silent=True)
        if not 'content' in data:
            content = None
        else:
            content = data['content']

        obj = Variable(g.obj_name, content=content)
        db.session.add(obj)
        db.session.commit()
        app.logger.info(u"Create Item %s %s by %s" % (Variable, g.obj_name, g.user))
        return jsonify({obj.id: {
            'name': obj.name,
        }})

    @auth.login_required
    @body_is_valid
    @is_unique_item(Variable)
    @get_item(Variable)
    @edit_item(Variable)
    def put(self, id=None):
        """
        @api {put} /variables/:id Edit an existing variable
        @apiVersion 1.0.0
        @apiName edit_variable
        @apiPermission user
        @apiGroup Variables
        @apiSuccess {Number}    success         True if success
        @apiSuccess {Number}    message         A information message
        @apiExample {curl} Example usage :
            curl -X PUT -H "Content-Type: application/json" \
            -d '{ "name": "my_new_name" }' \
            http://127.0.0.1:5000/api/v1/variables/:id
        """
        pass

    @auth.login_required
    @get_item(Variable)
    @delete_item(Variable)
    def delete(self, id):
        """
        @api {delete} /variables/:id Delete a single variable
        @apiVersion 1.0.0
        @apiName rm_variable
        @apiPermission user
        @apiGroup Variables
        @apiParam   {Number}    id              The variable's id.
        @apiSuccess {Boolean}   success         Success (True if ok).
        @apiSuccess {String}    message         A success or error message.
        @apiExample {curl} Example usage :
            curl -X DELETE http://127.0.0.1:5000/api/v1/variables/:id
        """
        pass
