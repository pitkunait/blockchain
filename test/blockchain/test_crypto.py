from unittest import TestCase
from core import Blockchain
from core.Transaction import Transaction
from core.Wallet import Wallet


class TestTransaction(TestCase):
    def test_create_transaction(self):
        wallet = Wallet()
        transaction = Transaction()
        signed = wallet.sign_transaction(transaction)
        signed.verify_signature()
        self.assertTrue(signed.verify_signature())


