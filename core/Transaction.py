from time import time
import uuid
import rsa
from rsa import VerificationError
from api.schema.transaction import TransactionSchema


class Transaction:
    def __init__(self,
                 id: str = None,
                 sender: str = None,
                 recipient: str = None,
                 amount: float = None,
                 signature: str = None,
                 public_key: str = None):
        if not id:
            id = uuid.uuid4().hex
        self.id = id
        self.sender = sender
        self.recipient = recipient
        self.timestamp = time()
        self.amount = amount
        self.signature = signature
        self.public_key = public_key

    def validate(self):
        if self.amount < 0:
            return False
        if not self.verify_signature():
            return False
        return True

    def serialize(self, ignore=None):
        if ignore is None:
            ignore = []
        block_params = {x: self.__dict__[x] for x in self.__dict__ if x not in ignore}
        return TransactionSchema().dumps(block_params, separators=(',', ':'))

    def plain(self):
        return self.serialize(['signature', 'public_key'])

    def verify_signature(self):
        transaction = self.plain().encode()
        if self.signature and self.public_key:
            pk_bytes = bytes.fromhex(self.public_key)
            pk = rsa.PublicKey.load_pkcs1_openssl_pem(pk_bytes)
            try:
                return rsa.verify(transaction, bytes.fromhex(self.signature), pk)
            except VerificationError:
                return False
        else:
            return False

    @staticmethod
    def from_schema(schema):
        transaction = Transaction()
        for key, value in schema.items():
            setattr(transaction, key, value)
        return transaction
