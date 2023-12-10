class Car :
    model = " "
    color = " "

car = Car()
car.color = "Red"
car.model = "Volvo"

print(car.model)
print(car.color)


car2 = Car()
car2.color = "Blue"
car2.model = "Audi"

print(car2.model)
print(car2.color)

#
class bike:
    def __init__(self,color, model):
        self.color = color
        self.model = model

    def displayBike(self):
        print(self.color)
        print(self.model)
        return 10

b1 = bike("Red", "Achi wala")
b1.displayBike()
print("------------------------------")
b2 = bike("Blue", "Sasti wali")

class const :
    def __init__(self):
        print("Constructor is Created :) ")
        name = "Ram"
        age = 18

c = const()
