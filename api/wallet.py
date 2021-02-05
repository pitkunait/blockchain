from flask import Blueprint, request

from chain.globals import blockchain

wallet_api = Blueprint('wallet', __name__)


@wallet_api.route('/', methods=['get'])
def get_wallet():
    walletid = request.args.get('id')
    balance = blockchain.get_balance_by_id(walletid)
    return {'balance': balance}, 200
