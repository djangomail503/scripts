from datetime import datetime

def log_transaction(func):
    def wrapper(account, amount):
        result = func(account, amount)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction_log = {"account": account.account_number, "amount": amount, "timestamp": timestamp}
        account.transaction_logs.append(transaction_log)
        print(f"Transaction logged - Account: {account.account_number}, Amount: ${amount}, Timestamp: {timestamp}")
        return result
    return wrapper

class Transaction:
    def __init__(self, transaction_id, transaction_type, amount):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now()

def transaction_log_decorator(log_format):
    def decorator(func):
        def wrapper(account, amount):
            result = func(account, amount)
            log_message = log_format.format(account=account, amount=amount, timestamp=datetime.now())
            transaction_log = {"account": account.account_number, "message": log_message, "timestamp": datetime.now()}
            account.transaction_logs.append(transaction_log)
            print(f"Transaction logged - {log_message}")
            return result
        return wrapper
    return decorator

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transaction_logs = []

    @log_transaction
    def deposit(self, amount):
        self.balance += amount

    @log_transaction
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# Example usage:
account = BankAccount("101112", 2000)
account.deposit(500)
account.withdraw(300)








"""
In the easy example, the log_transaction decorator is used to log transactions. It wraps the deposit and withdraw methods of the BankAccount class, printing a message after each transaction.

In the medium example, an additional decorator transaction_log_decorator is introduced, which allows customization of the log message format. It demonstrates a more versatile use of decorators.

In the hard example, the BankAccount class maintains a list of transaction logs, and each transaction is logged with more detailed information, such as the account number, log message, and timestamp. This showcases a more complex scenario where the decorator also updates internal state.

In the banking sector, decorators can be used to add various functionalities to methods, such as logging, authorization checks, or performance monitoring, without modifying the original code of the methods. They provide a clean and reusable way to extend the behavior of functions or methods in a flexible manner.

"""