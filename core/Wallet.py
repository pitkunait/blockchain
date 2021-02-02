import hashlib
import uuid

import rsa

from rsa.pem import save_pem

from core.Transaction import Transaction


class Wallet:
    def __init__(self):
        self.id = hashlib.sha256(uuid.uuid4().hex.encode()).hexdigest()
        pk, sk = rsa.newkeys(512)
        self.public_key = pk
        self.private_key = sk

    def sign_transaction(self, transaction: Transaction) -> Transaction:
        signature = rsa.sign(transaction.plain().encode(), self.private_key, 'SHA-1')
        der = self.public_key._save_pkcs1_der()
        # self.public_key.save_pkcs1()
        transaction.public_key = save_pem(der, 'PUBLIC KEY').hex()
        transaction.signature = signature.hex()
        return transaction