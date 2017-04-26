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
    @apiName post_user
    @apiGroup Users
    @apiVersion 1.0.0
    @apiPermission public
    @apiParam   {String}    name              (json document) The user's name
    @apiParam   {Password}  password          (json document)The users's password
    @apiSuccess {String}    name              The user's name
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
    @apiPermission public
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
    @api {get} /tokens Get a token
    @apiName get_token
    @apiGroup Tokens
    @apiVersion 1.0.0
    @apiPermission user
    @apiSuccess {String}    token              The token
    @apiParam   {Number}    [duration=600]     (query parameter) Use a custom token duration
    @apiSuccess {Number}    duration           The token's validity
    @apiExample {curl} Example usage :
        curl -X GET -H "Content-Type: application/json" \
        http://127.0.0.1:5000/api/v1/tokens
    """
    @auth.login_required
    def get(self):
        duration = int(request.args.get('duration', app.config['AUTH_DURATION']))
        token = g.user.generate_auth_token(expiration=duration)
        return jsonify({'token': token.decode('ascii'), 'duration': duration})
