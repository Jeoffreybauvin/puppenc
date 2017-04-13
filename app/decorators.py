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
            nb_limit = int(request.args.get('_perPage', app.config['OBJECTS_PER_PAGE']))
            cur_page = int(request.args.get('_page', 1))
            sort_dir = str(request.args.get('_sortDir', 'asc'))
            sort_field = str(request.args.get('_sortField', 'id'))

            filter = str(request.args.get('filter', ''))
            obj_id = kwargs.get('id')
            sort = sort_field + " " + sort_dir
            if filter:
                obj = Type.query.filter(Type.name.like(filter)).all()
            else:
                if obj_id:
                    obj = Type.query.filter_by(id=int(obj_id)).first()
                else:
                    q = Type.query.count()
                    obj = Type.query.order_by(sort).paginate(cur_page, nb_limit).items
                    g.count = q

            if obj is None:
                return { "success": False, "message": u"%s not found" % type  }, 404

            g.obj_info = obj
            app.logger.info(u"%s %s, %s by %s" % (request.method, Type, g.obj_info, g.user))
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

            app.logger.info(u"Create Item %s %s by %s" % (Type, g.obj_name, g.user))
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
            content = request.get_json(silent=True)
            obj_id = kwargs.get('id')

            editable_properties = [ 'name', 'environment_id', 'class_id', 'hostgroup_id' ]
            for prop in editable_properties:
                if prop in content:
                    try:
                        Type.query.filter_by(id=obj_id).update({ prop: content[prop] }, synchronize_session=False)
                    except:
                        app.logger.info('Trying to update %s', prop)
                else:
                    app.logger.info('No %s given', prop)

            Type.query.filter_by(id=obj_id).update({ "update_date": db.func.current_timestamp() }, synchronize_session=False)
            db.session.commit()
            app.logger.info(u"Edit Item %s by %s" % (Type, g.user))
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
            app.logger.info(u"Delete Item %s by %s" % g.obj_info, g.user)
            return { "success": True, "message": u"%s deleted" % g.obj_info }, 200
        return func_wrapper
    return wrapper
