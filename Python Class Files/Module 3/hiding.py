#write a program to hide your data using data encapulusation to protect companys copywrited name by others

class company():
    def __init__(self):
        self.__companyname = ("Google")

    def companyname(self):
        print(self.__companyname)

c1 = company()
c1.companyname()
