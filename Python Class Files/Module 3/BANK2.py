#WAP to implement abstract base class using a banking applicatiion , create a derive class using absrtact class and display the intrest rate of a FD
from abc import abstractmethod


class bank():
    def bank_info(self):
        print("Welcome to bank")

    @abstractmethod
    def interest(self):
        "Abstract Method"
        pass

class SBI(bank):
    def interest(self):
        "Implementation of Abstract method"
        print("In sbi bank 5 rs")

s = SBI()
s.bank_info()
