class InvestmentAccount:
    def __init__(self, account_id, balance=0):
        self.account_id = account_id
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, InvestmentAccount):
            combined_id = f"Combined_{self.account_id}_{other.account_id}"
            combined_balance = self.balance + other.balance
            return InvestmentAccount(combined_id, combined_balance)
        else:
            raise TypeError("Unsupported operand type. Use with another InvestmentAccount object.")

    def __str__(self):
        return f"InvestmentAccount {self.account_id}, Balance: ${self.balance:.2f}"

class Portfolio:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __add__(self, other):
        if isinstance(other, Portfolio):
            combined_portfolio = Portfolio()
            combined_portfolio.accounts = self.accounts + other.accounts
            return combined_portfolio
        else:
            raise TypeError("Unsupported operand type. Use with another Portfolio object.")

    def __str__(self):
        return f"Portfolio with {len(self.accounts)} accounts"

# Example usage:
account1 = InvestmentAccount("IA1", 5000)
account2 = InvestmentAccount("IA2", 7500)

portfolio1 = Portfolio()
portfolio1.add_account(account1)

portfolio2 = Portfolio()
portfolio2.add_account(account2)

combined_portfolio = portfolio1 + portfolio2
print(combined_portfolio)  # Output: Portfolio with 2 accounts
