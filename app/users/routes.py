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
        # return { "success": True, "message": u"%s added" % name }, 200
        return { 'name': user.name }, 200

    def get(self, id):
        user = User.query.get(id)
        if not user:
            abort(400)
        return jsonify({'name': user.name})


class Tokens(PuppencResource):
    def __init__(self):
        self.user_schema = UserSchema()
        self.users_schema = UserSchema(many=True)

    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token()
        app.logger.info(token)
        return jsonify({'token': token.decode('ascii'), 'duration': app.config['AUTH_DURATION']})
