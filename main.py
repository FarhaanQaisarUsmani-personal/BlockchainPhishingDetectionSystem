from mainfolder.phishingdetection import PhishingDetection
from mainfolder.Blockchain import Blockchain
from mainfolder.database import Database
from mainfolder.ui import UserInterface
import time

def main():
    # Initialize components
    blockchain = Blockchain()
    database = Database()
    phishingAgent = PhishingDetection()
    ui = UserInterface()

    ui.start()
    # Analyze transactions
    while True:
        transactions = blockchain.fetchTransactions()
        for transaction in transactions:
            if phishingAgent.analyzeTransaction(transaction):
                phishingAgent.reportSuspiciousActivity(transaction)
                database.logPhishingTransaction(transaction)
        
        address = ui.getUserInput()
        if address in phishingAgent.blacklistAddresses:
            ui.displayWarning(f"Address {address} is blacklisted!")
        
        time.sleep(10)

if __name__ == "__main__":
    main()