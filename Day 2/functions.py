# FUNCTIONS IN PYTHON
num = int(input("enter number: "))
fact = 1


def factorial(num):
    fact = 1
    for i in range(2, num + 1):
        fact = fact * i
    return fact


print(f"factorial of number {num} is {factorial(num)}")
