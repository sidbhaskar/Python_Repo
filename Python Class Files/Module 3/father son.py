#create a son and father class, son is derived form father, write attributes name of the father , age of the father and fathers account number, same three attributes for the son

class father:
    def info(self):
        print("Father Name")
class son(father) :
    def info(self):
        print("Son details")
s1 = son()
s1.info()

f=father().info()

