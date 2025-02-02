from mainfolder.phishingDetection import PhishingDetection
from mainfolder.blockchain import Blockchain
from mainfolder.database import Database
from mainfolder.ui import UserInterface

def main():
    # Initialize components
    blockchain = Blockchain()
    database = Database()
    phishing_agent = PhishingDetection()
    ui = UserInterface()

    # Fetch transactions from the blockchain
    transactions = blockchain.fetchTransactions()

    # Analyze transactions
    for transaction in transactions:
        if phishing_agent.analyzeTransaction(transaction):
            phishing_agent.reportSuspiciousActivity(transaction)
            database.logPhishingTransaction(transaction)

    # Start the user interface
    ui.start()

if __name__ == "__main__":
    main()