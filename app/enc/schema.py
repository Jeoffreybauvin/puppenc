# from app.puppenc import ma
# from app.hostgroups.models import Hostgroup
# from app.hostgroups.schema import HostgroupSchema
# from app.nodes.models import Node
# from marshmallow import fields
#
# class EncSchema(ma.ModelSchema):
#     id = fields.Int()
#     name = fields.Str()
#     hostgroup_name = fields.Nested(HostgroupSchema)
#
#     class Meta:
#         model = Node
#         # Fields to expose
#         fields = ('id', 'name', 'hostgroup_info')
