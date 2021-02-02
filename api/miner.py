from flask import Blueprint, request
from api.schema.miner import MineSchema
from api.schema.block import BlockSchema
from chain.globals import blockchain
from core.Block import Block

miner_api = Blueprint('miner', __name__)


@miner_api.route('/', methods=['POST'])
def mine():
    values = request.get_json()
    required = ['block']
    if not all(k in values for k in required):
        return MineSchema().dumps({'message': 'Invalid block'}), 400
    block_schema = BlockSchema().load(values['block'])
    block = Block.from_schema(block_schema)
    valid = blockchain.add_block(block)
    if valid:
        response = {
            'message': "New Block Mined",
            'block': block
        }
        return MineSchema().dumps(response), 201
    return MineSchema().dumps({'message': 'Invalid block'}), 400

