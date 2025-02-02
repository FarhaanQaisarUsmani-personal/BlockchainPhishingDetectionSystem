from datetime import datetime
import hashlib
import time
import random

class Blockchain:
    def __init__(self):
        self.amounts = [{"amount": 0.0005, "timestamp": 1245}]
        self.transactions = [{"id": 1, "sender": "0x123456789abcdef", "receiver": "Bob", "amount": 0.0005, "hash": "abc123", "timestamp": 1245}]

    def fetchTransactions(self):
        """Fetch transactions from the blockchain network."""
        return self.transactions

    def validateTransaction(self, transaction):
        """Validate a blockchain transaction."""
        requiredKeys = {"id", "sender", "receiver", "amount", "hash", "timestamp"}

        if not requiredKeys.issubset(transaction.keys()): #Check if all required keys are present
            return False
        
        if transaction["amount"] <= 0: #Check if amount positive
            return False
        
        if not isinstance(transaction["hash"], str) or len(transaction["hash"]) < 6: #Mimicking hash validation
            return False
        
        return True
    
    def getCurrentTimeStamp(self):
        """Get the current timestamp."""
        return int(datetime.now().strftime("%H%M"))
    
    def getLastSender(self):
        """Get the last sender of a transaction."""
        if self.transactions:
            return self.transactions[-1]["sender"]
        return None
    
    def generateTransactionHash(self, transactionID, sender, timestamp):
        """Generate a unique hash based on transaction details."""
        hashInput = f"{transactionID}{sender}{timestamp}".encode()
        return hashlib.sha256(hashInput).hexdigest()
    
    def generateRandomAmount(self):
        """Generate a random amount for a transaction."""
        return round(random.uniform(0.0001, 0.01), 6)

    def addTransaction(self, transactionID, sender):
        """Add a new transaction to the blockchain."""
        lastTransaction = self.transactions[-1]
        previousSender = lastTransaction["sender"]

        amount = self.generateRandomAmount()
        timestamp = self.getCurrentTimeStamp()
        hashValue = self.generateTransactionHash(transactionID, sender, timestamp)

        newTransaction = {
            "id": transactionID,
            "sender": sender,
            "receiver": previousSender,
            "amount": amount,
            "hash": hashValue,
            "timestamp": timestamp
        }

        if self.validateTransaction(newTransaction):
            self.transactions.append(newTransaction)
            return True, newTransaction
        
        return False, None