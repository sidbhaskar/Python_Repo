class students():
    def __init__(self,name,registration,age):
        self.name = name
        self.registration = registration
        self.age = age

stud1=students('Ram','252252',20)
stud2=students('Ram','252252',20)
stud3=students('Ram','252252',20)

print(stud1.__dict__)
print(stud2.__dict__)
print(stud3.__dict__)