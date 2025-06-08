# class Vehicle:
#     def start(self):
#         return 'starting'
# class Car:
#     def start(self):
#         return "Driving"
# v1=Vehicle()
# c1=Car()
# # print(v1.start())
# for i in (v1,c1):
#     print(i.start())

# USING INHERITANCE
class Employee:
    def Vehicle(self):
        print('starting')
class Car(Employee):
    def Vehicle(self):
        print('bike starts')
e1=Employee()
e2=Car()
for i in (e1,e2):
    i.Vehicle()