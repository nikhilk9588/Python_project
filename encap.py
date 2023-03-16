# encapsulation or abstraction
class A:
    a = 10
    __b = 20

    def __add(self, x, y):
        return x + y


obj = A()
print(obj.a)
# print(obj.b)
print(obj._A__b)  # to access encpulated property
print(obj._A__add(10, 30))
