from app.puppenc import ma
from app.classes.models import Class

class ClassSchema(ma.ModelSchema):
    class Meta:
        model = Class
        # Fields to expose
        fields = ('id', 'name', 'insert_date', 'update_date', 'delete_date')
