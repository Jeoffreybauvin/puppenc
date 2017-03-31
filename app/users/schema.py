from app.puppenc import ma
from app.users.models import User

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        # Fields to expose
        fields = ('id', 'name', 'password')
