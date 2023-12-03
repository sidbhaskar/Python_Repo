class students():
    def __init__(self,name,registration,age):
        self.name = name
        self.registration = registration
        self.age = age

stud1=students('Ram','252234',20)
stud2=students('Sham','252245',19)
stud3=students('Aaam','252212',21)

print(stud1.__dict__)
print(stud2.__dict__)
print(stud3.__dict__)

