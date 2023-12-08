# from abc import ABC, abstractmethod
#
# class AbstractClassExample(ABC):
#     @abstractmethod
#     def do_something(self):
#         pass
#
# class AnotherSubclass(AbstractClassExample):
#     def do_something(self):
#         super().do_something()
#         print("The subclass is doing something")
#
# x = AnotherSubclass()
# x.do_something()

#------------------------------------------------------------------------------

# class Account:
#   def __init__(self, balance):
#     self.__balance = balance  # Private variable using double underscore
#
#   def deposit(self, amount):
#     self.__balance += amount
#
#   def withdraw(self, amount):
#     if amount > self.__balance:
#       raise ValueError("Insufficient funds")
#     self.__balance -= amount
#
#   def get_balance(self):  # Public method to access private data
#     return self.__balance
#
# account = Account(100)
# account.deposit(50)
# account.withdraw(75)
#
# print("Account balance:", account.get_balance())  # 75


#------------------------------------------------------------------------------


# class Counter:
#   def __init__(self):
#     self.count = 0  # Instance variable
#
#   def increment(self):
#     self.count += 1
#
#   def get_count(self):
#     return self.count
#
#   def set_count(self, new_count):
#     self.count = new_count
#
# counter = Counter()
# counter.increment()
# counter.increment()
#
# print("Counter value:", counter.get_count())  # 2
#
# def change_count(counter, new_count):
#   counter.count = new_count  # Variable hiding
#
# change_count(counter, 10)
#
# print("Counter value:", counter.get_count())  # 10


# #------------------------------------------------------------------------------
#
#
class Car:
    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')

redcar = Car()
redcar.drive()
