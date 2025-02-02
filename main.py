from mainfolder.phishingDetection import PhishingDetection
from mainfolder.blockchain import Blockchain
from mainfolder.database import Database
from mainfolder.ui import UserInterface
import time

def main():
    # Initialize components
    blockchain = Blockchain()
    database = Database()
    phishingAgent = PhishingDetection()
    ui = UserInterface(phishingAgent)

    ui.start()

    # Monitor transactions
    while True:
        try:
            transactionID = int(input("Enter transaction ID: "))
        except ValueError:
            print("Invalid transaction ID. Please enter a valid integer.")
            continue

        sender = input("Enter sender address/name: ").strip()

        success, newTransaction = blockchain.addTransaction(transactionID, sender)

        if success:
            print("\nTansaction added successfully!")
            print(f"Details: {newTransaction}")
        else:
            print("\nTransaction failed.\nThe transaction was not added to the blockchain.")
        
        # Analyze transactions for phishing attempts
        transactions = blockchain.fetchTransactions()
        for transaction in transactions:
            if phishingAgent.analyzeTransaction(transaction):
                phishingAgent.reportSuspiciousActivity(transaction)
                database.logPhishingTransaction(transaction)
        
        address = ui.getUserInput()
        print("")
        print(f"Entered address: {address}")
        print(f"Blacklist contents: {phishingAgent.blacklistAddresses}")

        if address in phishingAgent.blacklistAddresses:
            ui.displayWarning(f"Address {address} is blacklisted!")
        
        time.sleep(5)

if __name__ == "__main__":
    main()