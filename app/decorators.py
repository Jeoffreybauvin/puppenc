from flask import Flask, Blueprint, make_response, request, abort, g, jsonify
from functools import wraps
from app.puppenc import api, db, app, auth, PuppencResource
from app.users.models import User

@auth.verify_password
def verify_password(name_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(name_or_token)
    if not user:
        # try to authenticate with name/password
        user = User.query.filter_by(name=name_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

# decorator
# check if body is valid (valid json)
def body_is_valid(func):
    def wrapper(*args, **kwargs):
        body = request.get_data()
        if not body:
            return { "success": False, "message": "No body given" }, 500
        else:
            try:
                content = request.get_json()
            except:
                return { "success": False, "message": "Invalid json syntax" }, 500
        return func(*args, **kwargs)

    return wrapper

# decorator
# check if my item is unique
def is_unique_item(Type):
    def wrapper(f):
        @wraps(f)
        def func_wrapper(*args, **kwargs):
            # Check if the item already exists
            content = request.get_json(silent=True)
            if not 'name' in content:
                return { "success": False, "message": u"'name' parameter is mandatory for this %s" % type }, 500

            name = content['name']
            exists = db.session.query(db.exists().where(Type.name == name)).scalar()
            if exists:
                return { "success": False, "message": u"%s already exists" % name }, 200
            g.obj_name = name
            return f(*args, **kwargs)
        return func_wrapper
    return wrapper

# decorator
# retrieve my item
def get_item(Type):
    def wrapper(f):
        @wraps(f)
        def func_wrapper(*args, **kwargs):
            obj_id = kwargs.get('id')
            nb_limit = int(request.args.get('limit', app.config['OBJECTS_PER_PAGE']))
            cur_page = int(request.args.get('page', 1))
            if obj_id:
                obj = Type.query.filter_by(id=obj_id).first()
            else:
                obj = Type.query.paginate(cur_page, nb_limit).items

            if obj is None:
                return { "success": False, "message": u"%s not found" % type  }, 404

            g.obj_info = obj
            return f(*args, **kwargs)
        return func_wrapper
    return wrapper

# decorator
# post my item
def post_item(Type):
    def wrapper(f):
        @wraps(f)
        def func_wrapper(*args, **kwargs):

            obj = Type(g.obj_name)
            db.session.add(obj)
            db.session.commit()

            app.logger.info(u"Create Item %s %s" % (Type, g.obj_name))
            return jsonify({obj.id: {
                'name': obj.name,
            }})
        return func_wrapper
    return wrapper

# decorator
# edit my item
def edit_item(Type):
    def wrapper(f):
        @wraps(f)
        def func_wrapper(*args, **kwargs):
            obj_id = kwargs.get('id')

            Type.query.filter_by(id=obj_id).update({ "update_date": db.func.current_timestamp() }, synchronize_session=False)
            Type.query.filter_by(id=obj_id).update({ "name": g.obj_name }, synchronize_session=False)

            db.session.commit()
            app.logger.info(u"Edit Item %s %s" % (Type, g.obj_name))
            return { "success": True, "message": "successfully modified" }, 200

            return f(*args, **kwargs)
        return func_wrapper
    return wrapper

# decorator
# delete my item
def delete_item(Type):
    def wrapper(f):
        @wraps(f)
        def func_wrapper(*args, **kwargs):
            response = f(*args, **kwargs)
            db.session.delete(g.obj_info)
            db.session.commit()
            app.logger.info(u"Delete Item %s" % g.obj_info)
            return { "success": True, "message": u"%s deleted" % g.obj_info }, 200
        return func_wrapper
    return wrapper
