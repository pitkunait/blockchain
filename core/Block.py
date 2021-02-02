import hashlib
from api.schema.block import BlockSchema
from time import time


class Block:
    def __init__(self, index=None, transactions=None, nonce=None, previous_hash=None):
        self.index = index
        self.timestamp = time()
        self.transactions = transactions
        self.nonce = nonce
        self.previous_hash = previous_hash
        self.hash = ''

    def __str__(self):
        return self.serialize()

    def serialize(self, ignore=None):
        if ignore is None:
            ignore = []
        block_params = {x: self.__dict__[x] for x in self.__dict__ if x not in ignore}
        return BlockSchema().dumps(block_params)

    def hash_block(self):
        return hashlib.sha256(self.serialize(['hash']).encode()).hexdigest()

    def first_n(self, n):
        return self.hash_block()[:n]

    def set_hash(self):
        self.hash = self.hash_block()

    @staticmethod
    def from_schema(schema):
        block = Block()
        for key, value in schema.items():
            setattr(block, key, value)
        return block
