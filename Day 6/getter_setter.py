class Employee:
    def __init__(self, a):
        self.name = a

    def show(self):
        print(f"Name of Employee is {self.name}")

    @property
    def employee(self,):
        self.name = "aj"


obj = Employee("aj")
# obj=Employee
obj.show()


#   SETTER
class Employee:
    def __init__(self, a):
        self._name = a  # Use _name to follow convention for properties

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def show(self):
        print(f"Name of Employee is {self._name}")


# Create object
obj = Employee("aj")

# Show original name
obj.show()  # Output: Name of Employee is aj

# Set new name using property
obj.name = "arpit"

# Show updated name
obj.show()  # Output: Name of Employee is arpit
