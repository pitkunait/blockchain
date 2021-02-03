from flask_marshmallow import Schema
from marshmallow.fields import Nested, Str, Int, Number
from api.schema.transaction import TransactionSchema


class BlockSchema(Schema):
    class Meta:
        ordered = True
        fields = ["index", "timestamp", "transactions", "nonce", "previous_hash", "hash"]

    index = Int()
    nonce = Int()
    timestamp = Number()
    previous_hash = Str()
    hash = Str()
    transactions = Nested(TransactionSchema, many=True)
