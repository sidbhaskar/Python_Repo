#WAP to implement data hiding and encapsulation properties and fix marks to 100 to create a

class Subject :
    def __init__(self):
        self.__maxmarks = 100

    def marks(self):
        print("Marks: {}".format(self.__maxmarks))

    def setMaxMarks(self,m):
        self.__maxmarks = m

s = Subject()
s.marks()

s.setMaxMarks(200)
s.marks()

