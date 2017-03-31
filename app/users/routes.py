from flask_restful import Resource
from flask import jsonify, request, url_for

from app.puppenc import api, db, app, PuppencResource
from app.decorators import *

from app.users.models import User
from app.users.schema import UserSchema

class Users(PuppencResource):
    def __init__(self):
        self.user_schema = UserSchema()
        self.users_schema = UserSchema(many=True)

    """
    @api {post} /users Create a user
    @apiVersion 1.0.0
    @apiName post_user
    @apiGroup Users
    @apiParam   {String}    name              The user's name
    @apiParam   {Password}  password          The users's password
    @apiSuccess {String}    name              The user's name
    @apiPermission none
    @apiExample {curl} Example usage :
        curl -X POST -H "Content-Type: application/json" \
        -d '{"name":"my_username","password":"my_password"}' \
        http://127.0.0.1:5000/api/v1/users
    """
    def post(self):
        name = request.json.get('name')
        password = request.json.get('password')
        if name is None or password is None:
            abort(400) # missing arguments
        if User.query.filter_by(name = name).first() is not None:
            abort(400) # existing user
        user = User(name = name)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        app.logger.info("Create user %s", user.name)
        return { 'name': user.name }, 200

    """
    @api {get} /users/<id> Get a single user
    @apiVersion 1.0.0
    @apiName get_user
    @apiGroup Users
    @apiParam   {Number}    id                The user's id
    @apiSuccess {String}    name              The user's name
    @apiPermission none
    @apiExample {curl} Example usage :
        curl -X GET -H "Content-Type: application/json" \
        http://127.0.0.1:5000/api/v1/users/1
    """
    def get(self, id):
        user = User.query.get(id)
        if not user:
            abort(400)
        return jsonify({'name': user.name})


class Tokens(PuppencResource):
    def __init__(self):
        self.user_schema = UserSchema()
        self.users_schema = UserSchema(many=True)

    """
    @api {get} /tokens/<id> Get a token
    @apiVersion 1.0.0
    @apiName get_token
    @apiGroup Tokens
    @apiSuccess {String}    token              The token
    @apiSuccess {Number}    duration           The token's validity
    @apiPermission user
    @apiExample {curl} Example usage :
        curl -X GET -H "Content-Type: application/json" \
        http://127.0.0.1:5000/api/v1/tokens
    """
    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token()
        app.logger.info("Generate a token for %s", g.user.name)
        return jsonify({'token': token.decode('ascii'), 'duration': app.config['AUTH_DURATION']})
