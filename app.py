from flask import Flask
from flask_marshmallow import Marshmallow

from api.blockchain import blockchain_api
from api.home import api
from api.miner import miner_api
from api.transaction import transaction_api


def create_app():
    app = Flask(__name__)
    return app


app = create_app()
ma = Marshmallow(app)

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(blockchain_api, url_prefix='/api/blockchain')
app.register_blueprint(miner_api, url_prefix='/api/miner')

app.register_blueprint(transaction_api, url_prefix='/api/transaction')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
