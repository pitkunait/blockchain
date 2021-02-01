import logging
import threading

from blockchain.Block import Block
from blockchain.Transaction import Transaction

logger = logging.getLogger()


class Blockchain:

    def __init__(self):
        self.__current_transactions = []
        self.__chain = []
        self.create_genesis()
        self.pof_strength = 4
        self.start_mining_thread()

    @property
    def last_block(self):
        return self.__chain[-1]

    @property
    def last_transaction(self):
        return self.__current_transactions[-1]

    @property
    def pending_transactions(self):
        return self.__current_transactions

    @property
    def full_chain(self):
        return self.__chain

    @property
    def last100(self):
        return self.__chain[-20:]

    def create_genesis(self):
        genesis_block = Block(0, self.__current_transactions, 0, 'Genesis Block')
        self.__chain.append(genesis_block)

    def add_block(self, block):
        valid = self.validate_block(block)
        if valid:
            self.__chain.append(block)
            self.__current_transactions = []
            return True
        return False

    def create_transaction(self, sender, recipient, amount):
        transaction = Transaction(sender, recipient, amount)
        if transaction.validate():
            self.__current_transactions.append(transaction)
            return transaction, True
        return None, False

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
        print(f"Mined block {block.index}")
        if self.add_block(block):
            return block
        return None

    def validate_proof_of_work(self, block):
        return block.first_n(self.pof_strength) == '0' * self.pof_strength

    def validate_block(self, block):
        if block.index != self.last_block.index + 1:
            return False
        if block.previous_hash != self.last_block.hash:
            return False
        if block.hash != block.hash_block():
            return False
        if not self.validate_proof_of_work(block):
            return False
        return True
