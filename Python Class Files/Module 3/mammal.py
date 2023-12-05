class mammal:
    def mammal_info(self):
        print("Mammal can give birth")

class wingedAnimal:
    def winged_animal_info(self):
        print("Winged animal can flap")
class bat(mammal,wingedAnimal):
    pass

b1 = bat()
b1.mammal_info()
b1.winged_animal_info()
