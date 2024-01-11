class empl :
    def __init__(self,name,age ):
        self.name = name
        self._age= age
    def show(self):
        print("Name is ",self.name, "Age is " , self._age)

e1 = empl('Ram', 18)
e1.show()

print(e1.name)
print(e1._age)