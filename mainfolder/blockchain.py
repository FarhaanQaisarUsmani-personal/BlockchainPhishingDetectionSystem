from datetime import datetime
import hashlib
import os
import random

class Blockchain:
    def __init__(self, blacklist=None):
        self.transactions = []
        self.amounts = [0.005]
        self.blacklist = blacklist if blacklist else []
        self.loadLastTransactions()


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

        
    def loadLastTransactions(self):
        """Load the last transactions from the database."""
        if os.path.exists("suspicious_transactions.log"):
            with open("suspicious_transactions.log", "r") as file:
                lastTransaction = file.readlines()
                
                if lastTransaction:
                    try:
                        lastLine = lastTransaction[-1].strip()
                        transactionID_str, sender = lastLine.split(",")
                        self.lastTransactionID = int(transactionID_str.strip())
                        self.lastSender = sender.strip()
                    except (ValueError, IndexError) as e:
                        print(f"Error parsing last transactino data: {e}")
                        self.lastTransactionID = 1
                        self.lastSender = "0x123456789abcdef"
                else:
                    self.lastTransactionID = 1
                    self.lastSender = "0x123456789abcdef" # Default sender
        else:
            # If no log file exists, start a new log file
            self.lastTransactionID = 1
            self.lastSender = "0x123456789abcdef"
    
    def saveLastTransaction(self, transactionID, sender):
        """Save a transaction to the database."""
        with open("suspicious_transactions.log", "a") as file:
            file.write(f"{transactionID}, {sender}\n")
            
            self.lastSender = sender

    def addTransaction(self, sender):
        """Add a new transaction to the blockchain."""
        if sender in self.blacklist or self.lastSender in self.blacklist:
            print("Transaction cancelled: Sender or Receiver is blacklisted.")
            return False, None

        transactionID = self.lastTransactionID + 1
        previousSender = self.lastSender

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
            newTransaction["status"] = "Success"
            self.transactions.append(newTransaction)
            self.saveLastTransaction(transactionID, sender)
            self.lastTransactionID = transactionID
            self.lastSender = sender
            return True, newTransaction
        else:
            newTransaction["status"] = "Failed"
            return False, None
