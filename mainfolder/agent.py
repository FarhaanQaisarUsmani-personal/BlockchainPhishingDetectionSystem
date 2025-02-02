import json
import time
from mainfolder.Blockchain import Blockchain
from mainfolder.database import Database
from mainfolder.phishingdetection import PhishingDetection
from mainfolder.ui import UserInterface

class Agent:
    def __init__(self):
        """Initializes agent parameters"""
        self.blockchain = Blockchain()
        self.database = Database()
        self.phishingdetection = PhishingDetection()
        self.ui = UserInterface()

    def monitorTransactions(self):
        """Monitor blockchain transactions for suspicious activity."""
        while True:
            transactions = self.blockchain.fetchTransactions()

            for transaction in transactions:
                if self.phishingdetection.analyzeTransaction(transaction):
                    self.ui.displayWarning(f"Suspicious transaction: {transaction['hash']}")
            
            time.sleep(15)

    def communicateWithAgents(self, message, recipentAgent):
        """Facilitate communication between agents in a multi-agent system."""
        print(f"Sending message to agent: {message}")
        recipentAgent.receiveMessage(message)

    def receiveMessage(self, message):
        print(f"Receieved message: {message}")