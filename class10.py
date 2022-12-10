class A:
    def _init_(self):
        print(self)
        print("initialised")
    def _del_(self):
        print(self)
        print("i am dying")
a =1
print(type(a))
print(a.__add__(5))
print(a.__mul__(5))

class A:
    a=1
    b=2
    def __add__(self,x):
        return self.a + self.b +x