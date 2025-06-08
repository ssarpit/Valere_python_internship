class Employee:
    def __init__(self,name,emp_id,salary,age):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
        self.age=age
    def show_details(self):
        print(f"Employee details are mentioned here :Name:{self.name} and Salary:{self.salary}")
class Manager(Employee):
    def __init__(self, name, emp_id, salary, age,department):
        super().__init__(name, emp_id, salary, age)
        self.department=department
    def show_details(self):
        print(f"Name :{self.name} and Department:{self.department}")
class Developer(Employee):
    def __init__(self,name,emp_id,salary,age,tech_stack):
         super().__init__(name, emp_id, salary, age)
         self.tech_stack=tech_stack
    def show_details(self):
        print(f"Person Name is {self.name} and skilled in {self.tech_stack}")
employees=[Manager('Arpit',101,50000,22,'Aiml'),
           Developer('Aj',102,40000,22,'Python')]
for em in employees:
    em.show_details()
        