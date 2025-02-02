import os
import time
import sys

class UserInterface:
    def __init__(self, phishingDetection):
        self.phishingDetection = phishingDetection

    def start(self):
        """Start the user interface."""
        print("Blockchain Phishing Detection System Started!")
        print("=============================================")

    def displayWarning(self, message):
        """Display a phishing warning to the user."""
        print(f"WARNING: {message}")

    def getUserInput(self):
        """Get user input for blockchain address verification."""
        while True:
            try:
                address = input("\nEnter address to check (q to quit, a to add): ").strip()

                if address in self.phishingDetection.blacklistAddresses:
                    print(f"Address {address} is already in the blacklist.")
                    
                if address.lower() == "q":
                    time.sleep(5)
                    os.system('cls')
                    sys.exit()

                if address.lower() == "a":
                    newAddress = input("\nEnter address to add to blacklist: ").strip()
                    self.addToBlacklist(newAddress)
                    return newAddress
                
                return address
            except KeyboardInterrupt:
                sys.exit()

    def addToBlacklist(self, address):
        """Manually add an address to the blacklist"""
        self.phishingDetection.blacklistAddresses.add(address)
        print(f"Address {address} has been added to the blacklist!")