class Person():
    name="arpit"
    occupation="Aiml engineer"
    def info(self):                                   #self is used as the first parameter in instance methods to refer to the current object
        print(f"{self.name} is a {self.occupation}")
a=Person()  #objects
# a.name='iamarpit'
# a.occupation='ai intern'
# print(a.name+"\n"+a.occupation)
b=Person()
b.name='aj'
b.occupation='ai'
b.info()
c=Person()
c.name='my'
c.info()