# SIMPLE CALCULATOR IN PYTHON

num1 = float(input("enter number_1 "))
op = input("enter operation: ")
num2 = float(input("enter number_2 "))
if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(f"Result:{num1*num2}")
elif op == "/":
    try:
        result = num1/num2
        print(f"Result: {result}")
    except Exception as e:
        print(e)
elif op == "%":
    try:
        result = num1 % num2
        print(f"Result is: {result}")
    except ZeroDivisionError:
        print(f"Modulo operator does not work for zero denominator ")
else:
    print("INVALID OPERATION ")


# calculator without using if else statement
num1 = float(input("enter number_1 "))
num2 = float(input("enter number_2 "))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
