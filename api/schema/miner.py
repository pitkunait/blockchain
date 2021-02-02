from flask_marshmallow import Schema
from marshmallow.fields import Nested, Str
from api.schema.block import BlockSchema


class MineSchema(Schema):
    class Meta:
        fields = ["message", "block"]

    message = Str()
    block = Nested(BlockSchema)
