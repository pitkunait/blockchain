from flask import Blueprint

from api.schema.blockchain import BlockchainSchema
from chain.globals import blockchain

blockchain_api = Blueprint('blockchain', __name__)


@blockchain_api.route('/')
def get_chain():
    chain = blockchain.last20
    response = {'blockchain': chain}
    return BlockchainSchema().dump(response), 200
