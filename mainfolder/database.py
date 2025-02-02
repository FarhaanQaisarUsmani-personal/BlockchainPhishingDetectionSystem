import json

class Database:
    def __init__(self):
        self.phishingTransactions = []
        self.knownPhishingAddresses = set()

    def logPhishingTransaction(self, transaction):
        """Log a phishing transaction to the database."""
        self.phishingTransactions.append(transaction)
        
        senderAddress = transaction.get("senderAddress")

        if senderAddress:
            self.knownPhishingAddresses.add(senderAddress)
        try:
            with open("phishingLogs.json", "r") as file:
                try:
                    data = json.load(file)
                    if not isinstance(data, list):
                        data = []
                except json.JSONDecodeError:
                    data = []
        except FileNotFoundError:
            data = []
        
        data.append(transaction)
        with open("phishingLogs.json", "w") as file:
            json.dump(transaction, file, indent=4)
            file.write("\n")

    def getKnownPhishingAddresses(self):
        """Retrieve a list of known phishing addresses."""
        return list(self.knownPhishingAddresses)