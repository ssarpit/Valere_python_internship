class Employee():
    def __init__(self, a, b):
        self.name = a
        self.occ = b
        print("Hey iam a engineer")

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Employee("arpit", "aiml enginner")
a.info()
