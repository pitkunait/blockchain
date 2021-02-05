import logging

from core.Block import Block

logger = logging.getLogger(__name__)


class Blockchain:

    def __init__(self):
        self.__current_transactions = []
        self.__chain = []
        self.__transaction_ids = []
        self.pof_strength = 4
        self.create_genesis()

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
    def last20(self):
        return self.__chain[-20:]

    @property
    def all_transactions(self):
        transactions = []
        for block in self.full_chain:
            transactions += block.transactions
        return transactions

    def get_transactions_by_id(self, id):
        transactions = []
        for transaction in self.all_transactions:
            if transaction['recipient'] == id or transaction['sender'] == id:
                transactions.append(transaction)
        return transactions

    def get_transaction_balance(self, transaction, id):
        if transaction.recipient == id:
            return transaction.amount
        elif transaction.sender == id:
            return -transaction.amount

    def get_balance_by_id(self, id):
        balance = 0
        for block in self.full_chain:
            for transaction in block.transactions:
                balance += self.get_transaction_balance(transaction, id)
        for transaction in self.pending_transactions:
            balance += self.get_transaction_balance(transaction, id)
        return balance

    def create_genesis(self):
        genesis_block = Block(0, self.__current_transactions, 0, 'Genesis Block')
        self.__chain.append(genesis_block)
        self.mine_genesis()

    def add_block(self, block):
        if self.validate_block(block):
            block.parseTransactions()
            self.__chain.append(block)
            self.__current_transactions = []
            return True
        return False

    def add_transaction(self, transaction):
        if self.validate_transaction(transaction):
            self.__current_transactions.append(transaction)
            self.__transaction_ids.append(transaction.id)
            return transaction, True
        return None, False

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

    def validate_transaction(self, transaction):
        if not transaction.validate():
            logger.error('Transaction not validated')
            return False
        if self.get_balance_by_id(transaction.sender) < transaction.amount:
            logger.error('Not enough balance')
            return False
        if transaction.id in self.__transaction_ids:
            logger.error('Already present')
            return False
        return True

    def mine_genesis(self):
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
