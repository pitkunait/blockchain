from flask import Blueprint, abort
from api.globals import blockchain
from api.schema.blockchain import BlockchainSchema
from api.schema.block import BlockSchema

blockchain_api = Blueprint('blockchain', __name__)


@blockchain_api.route('/')
def get_chain():
    """
    Returns the full blockchain
    Returns blockchain as a list of blocks with all transactions.
    ---
    """
    chain = blockchain.last100
    response = {
        'blockchain': chain
    }

    return BlockchainSchema().dump(response), 200


@blockchain_api.route('/block/<block_hash>')
def get_block(block_hash):
    """
    Returns the full blockchain
    Returns blockchain as a list of blocks with all transactions.
    ---
    """
    blocks = [x for x in blockchain.full_chain if x.hash == block_hash]
    if len(blocks) > 0:
        return BlockSchema().dump(blocks[0]), 200

    abort(404)
