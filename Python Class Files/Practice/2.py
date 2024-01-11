class Employee :
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return  self.__age

    def set_name(self,name):
        self.__name = name
        return

    def set_age(self,age):
        self.__age = age
        return

e1 = Employee(name='Raju', age=22)
print('Name : ',e1.get_name(), '\nAge : ',e1.get_age())
e1.set_name('Dugu')
e1.set_age(23)
print('Name : ',e1.get_name(), '\nAge : ',e1.get_age())
