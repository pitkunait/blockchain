import time


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.timestamp = time.time()
        self.amount = amount

    def validate(self):
        if self.amount < 0:
            return False
        return True
