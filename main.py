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
            if phishingAgent.analyzeTransaction(newTransaction):
                print("Suspicious transaction detected! Reporting...")
                phishingAgent.reportSuspiciousActivity(newTransaction)
                database.logPhishingTransaction(newTransaction)
        else:
            print("\nTransaction failed.\nThe transaction was not added to the blockchain.")
        
        
        address = ui.getUserInput()
        print("")
        print(f"Entered address: {address}")
        print(f"Blacklist contents: {phishingAgent.blacklistAddresses}")

if __name__ == "__main__":
    main()