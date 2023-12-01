class Person:
    pass
p = Person()
# print(p)

class person_class:
    def sayHi(self):
        print('Hello, How are you?')
# p = person_class().sayHi()

class Person_class2:
    '''Represents a person'''
    population = 0
    def __init__(self,name):
        '''Represents a person'''

        self.name = name
        print('Initializing %s'%self.name)
        Person_class2.population += 1
    def sayHi(self):
        print('HI, my name is %s'%self.name)

    def howMany(self):

        if Person_class2.population ==1 :
            print('I am Alone')
        else :
            print('We have %s person here')

Sid= Person_class2('Sid').sayHi()
