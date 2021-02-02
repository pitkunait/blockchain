from flask import Blueprint, request


from api.schema.transaction import TransactionCreatedSchema, TransactionSchema
from chain.globals import blockchain
from core.Transaction import Transaction

transaction_api = Blueprint('transaction', __name__)


@transaction_api.route('/', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['transaction']
    if not all(k in values for k in required):
        return TransactionCreatedSchema().dumps({'message': 'Invalid transaction'}), 400
    transaction_schema = TransactionSchema().load(values['transaction'])
    transaction = Transaction.from_schema(transaction_schema)
    transaction, valid = blockchain.add_transaction(transaction)
    if valid:
        response = {
            'message': "New transaction registered",
            'transaction': transaction
        }
        return TransactionCreatedSchema().dumps(response), 201
    return TransactionCreatedSchema().dumps({'message': 'Invalid transaction'}), 400
