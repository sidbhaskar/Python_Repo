class Bank:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance
    def savings_account(self, debit):
        self.balance -= debit
        return self.balance

    def personal_loan(self, debit):
        self.balance -= debit
        return self.balance

    def home_loan(self, debit):
        self.balance -= debit
        return self.balance

bank = Bank(10000)

print("General balance: ", bank.get_balance())
print("Savings account balance after debit: ", bank.savings_account(1000))
print("Balance after personal loan: ", bank.personal_loan(2000))
print("Balance after home loan: ", bank.home_loan(3000))
