class Add:
    def __init__(self,a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

ob1 = Add(1)
ob2 = Add(1)
ob3 = Add("VIT ")
ob4 = Add("University Bhopal")

print(ob1+ob2)
print(ob3+ob4)
print('')
print(Add.__add__(ob1,ob2))
print(Add.__add__(ob3,ob4))
print('')
print(ob1.__add__(ob2))
print(ob3.__add__(ob4))