# WAP to perform polymorphism using function overloading , bank operation ,general balance, saving acc , personal loan ,home load , balance will be old (balance - debit)

class Customer:

    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def get_balance(self):
        return self.balance

    def home_loan(self, home_load):
        self.balance -= home_load
        return self.balance

    def edu_load(self, edu_balance):
        self.balance -= edu_balance
        return self.balance

    def car_loan(self, car_loan):
        self.balance -= car_loan
        return self.balance


Customer = Customer('Rahul', 'id12345', 100000)
print('Name:', Customer.name)
print('Account no.', Customer.account_no)
print('General Balance: ', Customer.balance)
print('')
print('Balance After Home Loan: ', Customer.home_loan(10000))
print('Balance After Education Loan: ', Customer.edu_load(2000))
print('Balance After Car Loan: ', Customer.car_loan(5000))
