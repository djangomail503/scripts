class Transaction:
    def __init__(self, transaction_id, transaction_type, amount, timestamp):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = timestamp

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Account(Person):
    def __init__(self, account_number, balance, name, age):
        super().__init__(name, age)
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
    def __init__(self, account_number, balance, name, age, interest_rate):
        super().__init__(account_number, balance, name, age)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        print(f"Interest earned: ${interest:.2f}")

# Example usage:
savings_account = SavingsAccount("A67890", 2000, "Bob", 35, 3.0)
savings_account.deposit(500)
savings_account.withdraw(200)
savings_account.display_info()
savings_account.display_balance()
savings_account.calculate_interest()
savings_account.display_transactions()
