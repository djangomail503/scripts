class Transaction:
    def __init__(self, transaction_id, transaction_type, amount, timestamp):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = timestamp

class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance
        self._transactions = []
        self._transaction_counter = 1

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            transaction = Transaction(self._transaction_counter, "Deposit", amount, datetime.now())
            self._transactions.append(transaction)
            self._transaction_counter += 1
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            transaction = Transaction(self._transaction_counter, "Withdrawal", amount, datetime.now())
            self._transactions.append(transaction)
            self._transaction_counter += 1
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_transactions(self):
        print("Transaction History:")
        for transaction in self._transactions:
            print(f"ID: {transaction.transaction_id}, {transaction.transaction_type}: ${transaction.amount:.2f} at {transaction.timestamp}")

# Inherit from BankAccount to demonstrate encapsulation in inheritance
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.0):
        super().__init__(account_number, balance)
        self._interest_rate = interest_rate

    def calculate_interest(self):
        interest = self._balance * (self._interest_rate / 100)
        print(f"Interest earned: ${interest:.2f}")

# Example usage:
savings_account = SavingsAccount("13579", 1000, 2.5)
print("Initial balance:", savings_account.get_balance())
savings_account.deposit(500)
savings_account.withdraw(200)
savings_account.calculate_interest()
savings_account.display_transactions()






"""
In the SavingsAccount class, which inherits from BankAccount, encapsulation is maintained. 
The new class introduces an additional private attribute _interest_rate, and the interest is calculated through the calculate_interest method. 
The encapsulation principles are extended to the derived class. 
This showcases encapsulation in an inheritance scenario.
"""