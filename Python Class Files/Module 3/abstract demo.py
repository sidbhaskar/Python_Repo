from abc import abstractmethod


class demo:
    @abstractmethod
    def one(self):
        pass

    def two(self):
        print("Implimented Method")

d = demo()
print(d.one())
print(d.two())

