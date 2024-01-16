class Transaction:
    def __init__(self, transaction_id, transaction_type, amount, timestamp):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = timestamp

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []
        self.transaction_counter = 1

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        transaction = Transaction(self.transaction_counter, "Deposit", amount, datetime.now())
        self.transactions.append(transaction)
        self.transaction_counter += 1

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            transaction = Transaction(self.transaction_counter, "Withdrawal", amount, datetime.now())
            self.transactions.append(transaction)
            self.transaction_counter += 1
        else:
            print("Insufficient funds!")

    def display_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(f"ID: {transaction.transaction_id}, {transaction.transaction_type}: ${transaction.amount:.2f} at {transaction.timestamp}")

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.0):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def display_balance(self):
        print(f"Savings Account Number: {self.account_number}, Balance: ${self.balance:.2f}, Interest Rate: {self.interest_rate}%")

    def withdraw(self, amount):
        # Override the withdraw method to add a fee for savings account withdrawals
        fee = 2.0
        total_amount = amount + fee
        super().withdraw(total_amount)  # Call the parent class method
        print(f"Withdrawal Fee: ${fee:.2f}")

    def deposit(self, amount, bonus_percentage):
        # Overload the deposit method to add a bonus for savings account deposits
        bonus = amount * (bonus_percentage / 100)
        total_amount = amount + bonus
        super().deposit(total_amount)  # Call the parent class method
        print(f"Bonus added: ${bonus:.2f}")

# Example usage:
savings_account = SavingsAccount("S123", 2000, 2.5)
savings_account.deposit(500, 5)  # Deposit $500 with a 5% bonus
savings_account.withdraw(200)
savings_account.display_balance()
savings_account.display_transactions()
