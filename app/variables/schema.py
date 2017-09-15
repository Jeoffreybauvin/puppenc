from app.puppenc import ma
from app.variables.models import Variable

class VariableSchema(ma.ModelSchema):
    class Meta:
        model = Variable
        # Fields to expose
        fields = ('id', 'name', 'content', 'class_id', 'insert_date', 'update_date')
