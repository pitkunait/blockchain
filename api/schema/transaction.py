from flask_marshmallow import Schema
from marshmallow.fields import Str, Number, Nested


class TransactionSchema(Schema):
    class Meta:
        ordered = True
        fields = ["id", "sender", "recipient", "amount", "timestamp", "signature", "public_key"]

    id = Str()
    sender = Str()
    recipient = Str()
    amount = Number()
    timestamp = Number()
    signature = Str()
    public_key = Str()


class TransactionCreatedSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["message", "transaction"]

    message = Str()
    transaction = Nested(TransactionSchema)