class A:
    def __init__(self,a):
        self.a =a

    def __gt__(self, other):

        if ( self.a > other.a):
            return True
        else:
            return False

ob1 = A(2)
ob2 = A(4)

print(ob1 > ob2)