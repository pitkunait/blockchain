from flask import Blueprint
from api.globals import blockchain
from api.schema.miner import MineSchema

miner_api = Blueprint('miner', __name__)


@miner_api.route('/mine', methods=['POST'])
def mine():
    """
    Mines a new block into the chain
    Consolidates the pending transactions into a new block, and adds the block to the blockchain
    ---
    produces:
        - application/json
    responses:
        200:
            description: Result of the mining attempt and the new block
    """
    block = blockchain.mine('address')

    response = {
        'message': "New Block Mined",
        'block': block
    }

    return MineSchema().dumps(response), 200
