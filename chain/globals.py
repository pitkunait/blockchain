from core.Block import Block
from core.Blockchain import Blockchain
import threading


blockchain = Blockchain()


def start_mining_thread(self):
    def infinite_mine():
        while True:
            self.mine()

    x = threading.Thread(target=infinite_mine, daemon=True)
    x.start()


def mine(self):
    nonce = 0
    while True:
        nonce += 1
        block = Block(self.last_block.index + 1, self.__current_transactions, nonce, self.last_block.hash)
        if self.validate_proof_of_work(block):
            block.set_hash()
            break
    if self.add_block(block):
        return block
    return None
