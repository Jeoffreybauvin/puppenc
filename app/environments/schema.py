from app.puppenc import ma
from app.environments.models import Environment

class EnvironmentSchema(ma.ModelSchema):
    class Meta:
        model = Environment
        # Fields to expose
        fields = ('id', 'name', 'insert_date', 'update_date', 'delete_date')
