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
    transactions = blockchain.fetch_transactions()

    # Analyze transactions
    for transaction in transactions:
        if phishing_agent.analyze_transaction(transaction):
            phishing_agent.report_suspicious_activity(transaction)
            database.log_phishing_transaction(transaction)

    # Start the user interface
    ui.start()

if __name__ == "__main__":
    main()