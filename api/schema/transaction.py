from flask_marshmallow import Schema
from marshmallow.fields import Str, Number, Nested, Int


class TransactionSchema(Schema):
    class Meta:
        ordered = True
        fields = ["id", "sender", "recipient", "amount", "timestamp", "signature", "public_key"]

    id = Str()
    sender = Str()
    recipient = Str()
    amount = Int()
    timestamp = Number()
    signature = Str()
    public_key = Str()


class TransactionsSchema(Schema):
    class Meta:
        fields = ["transactions"]

    transactions = Nested(TransactionSchema(), many=True)


class TransactionCreatedSchema(Schema):
    class Meta:
        fields = ["message", "transaction"]

    message = Str()
    transaction = Nested(TransactionSchema)