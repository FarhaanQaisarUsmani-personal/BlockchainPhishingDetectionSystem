import json
import time
from mainfolder.blockchain import Blockchain
from mainfolder.database import Database

class Agent:
    def __init__(self):
        """Initializes agent parameters"""
        self.blockchain = Blockchain()
        self.database = Database()

    def monitorTransactions(self):
        """Monitor blockchain transactions for suspicious activity."""
        while True:
            transactions = self.blockchain.fetchTransactions()

            for transaction in transactions:
                senderAddress = transaction.get("senderAddress", "")

                if senderAddress in self.database.getKnownPhishingAddresses():
                    print(f"ALERT: Suspicious transaction detected from {senderAddress}")
            
            time.sleep(10)

    def communicateWithAgents(self, message, recipentAgent):
        """Facilitate communication between agents in a multi-agent system."""
        print(f"Sending message to agent: {message}")
        recipentAgent.receiveMessage(message)

    def receiveMessage(self, message):
        print(f"Receieved message: {message}")