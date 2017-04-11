from app.puppenc import db, app, g
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)


class User(db.Model):
    __tablename__ = 'users'
    id            = db.Column(db.Integer, primary_key =True)
    name          = db.Column(db.String(32), index    = True)
    password_hash = db.Column(db.String(128))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User %r>' % (self.name)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=app.config['AUTH_DURATION']):
        app.logger.info("Generate a token for %s with duration of %s seconds", g.user, expiration)
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        # app.logger.info('Sending a token for user %s', user)
        return user
