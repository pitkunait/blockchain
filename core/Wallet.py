import hashlib
import uuid
import rsa
from core.Transaction import Transaction


class Wallet:
    def __init__(self):
        self.id = hashlib.sha256(uuid.uuid4().hex.encode()).hexdigest()
        pk, sk = rsa.newkeys(512)
        self.public_key = pk
        self.private_key = sk

    def sign_transaction(self, transaction: Transaction) -> Transaction:
        signature = rsa.sign(transaction.plain().encode(), self.private_key, 'SHA-1')
        transaction.public_key = self.public_key.save_pkcs1().hex()
        transaction.signature = signature.hex()
        return transaction
