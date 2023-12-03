#Create a student class with 3 attributes and 2 functions

class employee() :

    def __init__(self,name , age , id ,salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary

emp1 = employee('Harshit',22,1000,100000)
emp2 = employee('Arjun',24,2000,250000)

print(emp1.__dict__)

