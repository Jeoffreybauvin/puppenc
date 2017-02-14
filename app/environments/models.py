from app import db

class Environment(db.Model):
    __tablename__ = 'environments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    insert_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    delete_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Environment %r>' % (self.name)
