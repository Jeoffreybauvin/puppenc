from flask_restful import Resource
from flask import jsonify, request, g

from app.puppenc import api, db, app, auth, PuppencResource
from app.decorators import *

from app.classes.models import Class
from app.classes.schema import ClassSchema

class Classes(PuppencResource):
    def __init__(self):
        self.class_schema = ClassSchema()
        self.classes_schema = ClassSchema(many=True)

    @auth.login_required
    @get_item(Class)
    def get(self, id=None):
        """
        @api {get} /classes Get all classes
        @apiName get_classes
        @apiGroup Classes
        @apiVersion 1.0.0
        @apiPermission user
        @apiParam   {String}    [limit=10]      (query parameter) Objects per page to display. Use limit=0 for disabling limit
        @apiParam   {String}    [page=1]        (query parameter) Current page
        @apiParam   {String}    [filter]        (query parameter) Filter on name parameter (use * for searching any strings. Ex: *maclass*)
        @apiSuccess {Number}    id              The class's id.
        @apiSuccess {String}    name            The class's name.
        @apiSuccess {Array}     hostgroups      The class's hostgroups (by id)
        @apiSuccess {Datetime}  insert_date     The class's inserted date
        @apiSuccess {Datetime}  update_date     The class's updated date
        @apiSuccess {Datetime}  delete_date     The class's deleted date
        @apiExample {curl} Example usage :
            curl -X GET -u user:pwd http://127.0.0.1:5000/api/v1/classes
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            [
              {
                "delete_date": null,
                "hostgroups": [
                  1
                ],
                "id": 1,
                "insert_date": "2017-04-11T13:55:40+00:00",
                "name": "role::webserver",
                "update_date": null
              },
              {
                "delete_date": null,
                "hostgroups": [
                  2
                ],
                "id": 2,
                "insert_date": "2017-04-11T13:55:25+00:00",
                "name": "role::log",
                "update_date": null
              }
            ]
        """

        """
        @api {get} /classes/:id Get a single class
        @apiName get_class
        @apiGroup Classes
        @apiVersion 1.0.0
        @apiPermission user
        @apiParam   {Number}    id              The class's id.
        @apiSuccess {Number}    id              The class's id.
        @apiSuccess {String}    name            The class's name.
        @apiSuccess {Array}     hostgroups      The class's hostgroups (by id)
        @apiSuccess {Datetime}  insert_date     The class's inserted date
        @apiSuccess {Datetime}  update_date     The class's updated date
        @apiSuccess {Datetime}  delete_date     The class's deleted date
        @apiExample {curl} Example usage :
            curl -X GET http://127.0.0.1:5000/api/v1/classes/:id
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            {
                "delete_date": null,
                "hostgroups": [
                  1
                ],
                "id": 1,
                "insert_date": "2017-04-11T13:55:40+00:00",
                "name": "role::webserver",
                "update_date": null
            }
        """
        if not id:
            return self.classes_schema.jsonify(g.obj_info)
        else:
            return self.class_schema.jsonify(g.obj_info)

    @auth.login_required
    @body_is_valid
    @is_unique_item(Class)
    @post_item(Class)
    def post(self, id=None):
        """
        @api {post} /classes Add a new class
        @apiVersion 1.0.0
        @apiName add_class
        @apiGroup Classes
        @apiParam   {String}    name            The class's name.
        @apiPermission user
        @apiSuccess {Number}    id              The class's id.
        @apiExample {curl} Example usage :
            curl -X POST -H "Content-Type: application/json" \
            -d '{ "name": "role::my_class" }' \
            http://127.0.0.1:5000/api/v1/classes
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            {
              "333": {
                "name": "role::my_class"
              }
            }

        """
        pass

    @auth.login_required
    @body_is_valid
    @is_unique_item(Class)
    @get_item(Class)
    @edit_item(Class)
    def put(self, id=None):
        """
        @api {put} /classes/:id Edit an existing class
        @apiVersion 1.0.0
        @apiName edit_class
        @apiPermission user
        @apiGroup Classes
        @apiSuccess {Number}    success         True if success
        @apiSuccess {Number}    message         A information message
        @apiExample {curl} Example usage :
            curl -X PUT -H "Content-Type: application/json" \
            -d '{ "name": "role::my_class" }' \
            http://127.0.0.1:5000/api/v1/classes/:id
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            {
                "message": "successfully modified",
                "success": true
            }
        """
        pass

    @auth.login_required
    @get_item(Class)
    @delete_item(Class)
    def delete(self, id):
        """
        @api {delete} /classes/:id Delete a single class
        @apiVersion 1.0.0
        @apiName rm_class
        @apiPermission user
        @apiGroup Classes
        @apiParam   {Number}    id              The class's id.
        @apiSuccess {Boolean}   success         Success (True if ok).
        @apiSuccess {String}    message         A success or error message.
        @apiExample {curl} Example usage :
            curl -X DELETE http://127.0.0.1:5000/api/v1/classes/:id
        @apiSuccessExample {json} Success-Response:
            HTTP/1.0 200 OK
            {
                "message": "<Class 'role::my_new_class'> deleted",
                "success": true
            }
        """
        pass
