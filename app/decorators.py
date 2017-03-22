from flask import Flask, Blueprint, make_response, request, abort, g, jsonify
from functools import wraps
from app.puppenc import api, db, app, PuppencResource

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


def get_item(Type):
    def wrapper(f):
        @wraps(f)
        def func_wrapper(*args, **kwargs):
            obj_id = kwargs.get('id')
            if obj_id:
                obj = Type.query.filter_by(id=obj_id).first()
            else:
                obj = Type.query.paginate(1, 1000).items

            if obj is None:
                return { "success": False, "message": u"%s not found" % type  }, 404

            g.obj_info = obj
            return f(*args, **kwargs)
        return func_wrapper
    return wrapper


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
