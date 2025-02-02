import json

class Database:
    def __init__(self):
        self.phishingTransactions = {}
        self.knownPhishingAddresses = set()

    def logPhishingTransaction(self, transaction):
        """Log a phishing transaction to the database."""
        pass

    def getKnownPhishingAddresses(self):
        """Retrieve a list of known phishing addresses."""
        return []