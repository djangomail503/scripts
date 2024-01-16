class Transaction:
    def __init__(self, transaction_id, transaction_type, amount, timestamp):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = timestamp

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def display_customer_info(self):
        print(f"Customer ID: {self.customer_id}, Name: {self.name}")

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

class SavingsAccount(Customer, Account):
    def __init__(self, customer_id, name, account_number, balance=0, interest_rate=0.0):
        Customer.__init__(self, customer_id, name)
        Account.__init__(self, account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        print(f"Interest earned: ${interest:.2f}")

# Example usage:
savings_account = SavingsAccount("C456", "Bob", "A54321", 1500, 3.0)
savings_account.deposit(500)
savings_account.withdraw(200)
savings_account.display_customer_info()
savings_account.display_balance()
savings_account.calculate_interest()
savings_account.display_transactions()
