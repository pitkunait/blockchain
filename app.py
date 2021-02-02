from flask import Flask
from flask_marshmallow import Marshmallow

from api.blockchain import blockchain_api
from api.miner import miner_api
from api.transaction import transaction_api

app = Flask(__name__)
ma = Marshmallow(app)

app.register_blueprint(blockchain_api, url_prefix='/api/blockchain')
app.register_blueprint(miner_api, url_prefix='/api/mine')
app.register_blueprint(transaction_api, url_prefix='/api/transaction')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
