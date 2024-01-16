from datetime import datetime

class Transaction:
    def __init__(self, transaction_id, transaction_type, amount):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now()

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        transaction = Transaction(len(self.transactions) + 1, "Deposit", amount)
        self.transactions.append(transaction)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            transaction = Transaction(len(self.transactions) + 1, "Withdrawal", amount)
            self.transactions.append(transaction)
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def __iter__(self):
        return iter(self.transactions)

    def filter_transactions(self, transaction_type):
        for transaction in self.transactions:
            if transaction.transaction_type == transaction_type:
                yield transaction

# Example usage:
account = BankAccount("101112", 2000)
account.deposit(500)
account.withdraw(300)
account.deposit(700)

# Iterate over deposit transactions using the generator
for transaction in account.filter_transactions("Deposit"):
    print(f"Transaction ID: {transaction.transaction_id}, Type: {transaction.transaction_type}, Amount: ${transaction.amount}, Timestamp: {transaction.timestamp}")










"""
In the easy example, the transaction_history method uses the yield keyword to create a simple generator function. The BankAccount class can be iterated using a for loop, and each transaction is yielded one by one.

In the medium example, the BankAccount class implements the __iter__ method, allowing instances of the class to be used as iterators directly. This simplifies the usage of the iterator protocol, making it more Pythonic.

In the hard example, the Transaction class includes a timestamp attribute. The filter_transactions method is implemented using a generator to filter transactions based on their type. This demonstrates a more complex scenario where additional data and filtering are involved.

"""