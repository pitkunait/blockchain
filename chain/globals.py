
from core.Blockchain import Blockchain
import threading


blockchain = Blockchain()


def start_mining_thread():
    def infinite_mine():
        while True:
            blockchain.mine_genesis()

    x = threading.Thread(target=infinite_mine, daemon=True)
    x.start()

