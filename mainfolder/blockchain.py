class Blockchain:
    def __init__(self):
        self.transactions = [{"id": 1, "sender": "Alice", "receiver": "Bob", "amount": 2.5, "hash": "abc123"},
                             {"id": 2, "sender": "Eve", "receiver": "Charlie", "amount": 5.0, "hash": "def456"},
                             {"id": 3, "sender": "Mallory", "receiver": "Alice", "amount": 1.2, "hash": "ghi789"}]

    def fetch_transactions(self):
        """Fetch transactions from the blockchain network."""
        return self.transactions

    def validate_transaction(self, transaction):
        """Validate a blockchain transaction."""
        requiredKeys = {"id", "sender", "receiver", "amount", "hash"}

        if not requiredKeys.issubset(transaction.keys()): #Check if all required keys are present
            return False
        
        if transaction["amount"] <= 0: #Check if amount positive
            return False
        
        if not isinstance(transaction["hash"], str) or len(transaction["hash"]) < 6: #Mimicking hash validation
            return False
        
        return True