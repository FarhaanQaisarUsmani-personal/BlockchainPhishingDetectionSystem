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
    ui = UserInterface(phishingAgent)

    ui.start()
    # Analyze transactions
    while True:
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
        else:
            print("Would you like to add this address in the blacklist? (Y?N)")
            choice = input("")

            if choice.upper() == "Y":
                newAddress = input("\nEnter address to add to blacklist: ").strip()
                ui.addToBlacklist(newAddress)
                return newAddress

        
        time.sleep(5)

if __name__ == "__main__":
    main()