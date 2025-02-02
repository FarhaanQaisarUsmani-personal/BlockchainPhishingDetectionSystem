import json
class PhishingDetection:
    def __init__(self):
        self.blacklistAddresses = {"0x123456789abcdef", "0xabcdef123456789"} # Examples of phishing addresses
        self.suspiciousThreshold = 0.8 #Risk score threshold for flagging transactions

    def analyzeTransaction(self, transaction):
        """Analyze a blockchain transaction to detect phishing attempts."""

        sender = transaction.get("sender")
        receiver = transaction.get("receiver")
        amount = transaction.get("amount")
        metadata = transaction.get("metadata", "")

        if sender in self.blacklistAddresses or receiver in self.blacklistAddresses:
            return True # Phishing detected
        
        if amount < 0.001:
            return True # Possible Phishing behaviour
        
        if "http" in metadata or "www" in metadata:
            return True #Possible phishing URL detected
        
        riskScore = self.calculateRiskScore(transaction)

        if riskScore > self.suspiciousThreshold:
            return True
        
        return False
    
    def calculateRiskScore(self, transactions):
        """Calculate a risk score based on transaction details"""
        score = 0.0

        if transactions.get("sender") not in self.blacklistAddresses:
            score += 0.2
        
        if transactions.get("receiver") not in self.blacklistAddresses:
            score += 0.2

        if transactions.get("amount", 1) < 0.001:
            score += 0.4

        return min(score, 1.0) #Ensuring risk score does not exceed 1.0

    def reportSuspiciousActivity(self, transaction):
        """Report suspicious activity to the alert system."""

        print("Suspicious transaction detected! Reporting...")

        with open("suspicious_transactions.log", "a") as logFile:
            json.dump(transaction, logFile, indent=4)
            logFile.write("\n")

        self.blacklistAddresses.add(transaction.get("sender"))