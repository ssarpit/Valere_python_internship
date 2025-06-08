class Employee:
    def __init__(self,a,b):
        self.name=a
        self.id=b
    def show_details(self):
        print(f"{self.name} having this {self.id} id")
class Programmar(Employee):
    def showinformation(self):
        print(f"Programmer is smart and he is very intelligent ,his name is {self.name}")
e1=Employee("aj",101)
e1.show_details()
e2=Programmar('arpit',1)
e2.showinformation()
