class BankAccount:
    BALANCE_FILE = "balance.txt"  # File to store balance

    def __init__(self, account_balance=0):
        try:
            # Try loading the last saved balance
            with open(self.BALANCE_FILE, "r") as f:
                self.account_balance = float(f.read())
        except FileNotFoundError:
            # If file doesn't exist, use the initial balance from main.py
            self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        self._save_balance()

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            self._save_balance()
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")

    def _save_balance(self):
        with open(self.BALANCE_FILE, "w") as f:
            f.write(str(self.account_balance))



