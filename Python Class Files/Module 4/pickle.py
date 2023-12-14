class emp :
    def __init__(self,id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
    def dis(self):
        print(self.name , self.id , self.sal)

import pickle

f = open('emp.dat','wb')
n = int(input('Enter the num of Employees: '))
for i in range(n):
    name = input('Name: ')
    f.write(name)
