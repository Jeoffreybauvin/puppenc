from app.puppenc import ma
from app.nodes.models import Node

class NodeSchema(ma.ModelSchema):
    class Meta:
        model = Node
        # Fields to expose
        fields = (
            'id',
            'name',
            'insert_date',
            'update_date',
            'delete_date',
            'hostgroup_id',
            'environment_id',
            'active',
            'last_used',
            'nodes_var'
        )
