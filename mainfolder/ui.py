class UserInterface:
    def start(self):
        """Start the user interface."""
        print("Blockchain Phishing Detection System Started!")
        print("=============================================")

    def displayWarning(self, message):
        """Display a phishing warning to the user."""
        print(f"WARNING: {message}")

    def getUserInput(self):
        """Get user input for blockchain address verification."""
        return input("Enter a blockhain address to check: ").strip()