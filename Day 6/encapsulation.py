# ENCAPSULATION:  Binding up of data members and member function such that
# data gets protected in it
class Employee:
    def __init__(self, a):
        self.__name = a

    def show(self):
        print(f"name is {self.__name}")


e1 = Employee('aj')
print(e1._Employee__name)
